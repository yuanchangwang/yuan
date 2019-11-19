from django.shortcuts import render


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

book_list = [book1, book2, book3, book4]


def books_list(request):
    return render(request, 'books_list.html', {'books_list': book_list})
