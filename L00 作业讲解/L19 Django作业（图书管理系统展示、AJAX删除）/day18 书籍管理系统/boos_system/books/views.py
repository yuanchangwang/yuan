import time

from django.shortcuts import render
from books import models
from django.http import JsonResponse


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
    print(books)
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


def edit_book(request):
    pass


def add_book(request):
    ...
