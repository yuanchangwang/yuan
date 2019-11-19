import time
from django.shortcuts import render, redirect
from books import models
from django.http import JsonResponse
from django.views import View


# Create your views here.


class Book:
    def __init__(self, title, price, author, publisher):
        self.title = title
        self.price = price
        self.author = author
        self.publisher = publisher


book1 = Book("三国演义", 200, "罗贯中", "南山出版社")
book2 = Book("红楼梦", 130, "曹雪芹", "东莞出版社")
book3 = Book("西游记", 150, "吴承恩", "南山出版社")
book4 = Book("水浒传", 180, "施耐庵", "宝安出版社")

books_list = [book1, book2, book3, book4]


def index(request):
    return render(request, 'index.html', {'books_list': books_list})


def book_list(request):
    # 获取所有的书籍对象
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_list': books})


def del_book(request):
    # 获取到要删除的图书id
    nid = request.POST.get('pk')
    res = {'status': 1, 'msg': '删除成功'}
    try:
        time.sleep(2)  # 模拟网络延时
        # 通过id去数据库找到对应的数据给删掉
        models.Book.objects.get(id=nid).delete()
    except Exception as e:
        # 如果找不到这条数据，则把错误信息返回给前端
        res['status'] = 0
        res['msg'] = '删除失败:' + str(e)
    # 最后返回结果
    return JsonResponse(res)


class Addbook(View):
    def get(self, request):
        # 获取所有作者对象
        author_list = models.Author.objects.all()
        # 获取所有出版社对象
        publisher_list = models.Publisher.objects.all()
        return render(request, 'add_book.html', {'author_list': author_list, 'publisher_list': publisher_list})

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors = request.POST.getlist('authors')
        publisher = request.POST.get('publisher')
        # 把前端获取的值新增到数据库中
        books = models.Book.objects.create(title=title, price=price, pub_date=pub_date, publisher_id=publisher)
        # 作者可能有多个，所以要打散添加
        books.authors.add(*authors)
        return redirect('/books/book_list/')


class Editbook(View):
    def get(self, request):
        # 根据书籍id去数据库找到对应的书籍
        pk = request.GET.get('pk')
        book = models.Book.objects.get(id=pk)
        # 获取所有的作者对象
        author_list = models.Author.objects.all()
        # 获取所有的出版社对象
        publisher_list = models.Publisher.objects.all()
        return render(request, 'edit_book.html', 
                      {'book': book, 'author_list': author_list, 'publisher_list': publisher_list})
    
    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors = request.POST.getlist('authors')
        publisher = request.POST.get('publisher')
        pk = request.GET.get('pk')
        print(123, pk)
        # 把前端获取的数据更新到书籍表
        books = models.Book.objects.filter(id=pk)
        books.update(title=title, price=price, pub_date=pub_date, publisher_id=publisher)
        # 作者可能有多个，set方法需要传一个列表，所以不能打散
        books.first().authors.set(authors)
        return redirect('/books/book_list/')
