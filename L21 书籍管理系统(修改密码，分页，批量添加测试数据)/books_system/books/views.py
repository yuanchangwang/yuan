import random
import time
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.utils.decorators import method_decorator
from books import models
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from utils.paginator import Paginator


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


# 主页面
def index(request):
    return render(request, 'index.html', {'books_list': books_list})


from faker import Faker

fake = Faker(locale='zh_CN')


# 批量添加测试数据
def add_ceshi(request):
    for i in range(100):
        title = fake.name()
        price = fake.random.randint(1, 999)
        pub_date = fake.date()
        publisher = random.choice([1, 2, 3])
        authors = random.sample([1, 2, 3, 4], random.randint(1, 4))
        # todo 数据库批量添加数据 models.Book.objects.bulk_create()
        books = models.Book.objects.create(title=title, price=price, pub_date=pub_date, publisher_id=publisher)
        # 作者可能有多个，所以要打散添加
        books.authors.add(*authors)
    return HttpResponse('OK')


# 书籍展示
@login_required
def book_list(request):
    # 获取所有的书籍对象
    books = models.Book.objects.all()  # 这是queryset对象
    current_page = request.GET.get('page')
    paginator = Paginator(request, current_page, books.count(), 10, 7)
    books = books[paginator.start: paginator.end]
    return render(request, 'book_list.html', {'book_list': books, 'paginator': paginator, 'current_page': current_page})


# 删除书籍
@login_required
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


# 添加书籍
class Addbook(View):
    @method_decorator(login_required)
    def get(self, request):
        # 获取所有作者对象
        author_list = models.Author.objects.all()
        # 获取所有出版社对象
        publisher_list = models.Publisher.objects.all()
        return render(request, 'add_book.html', {'author_list': author_list, 'publisher_list': publisher_list})

    @method_decorator(login_required)
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


# 修改书籍
@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
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


# 注册
class Register(View):
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Register, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 判断是ajax请求还是form表单提交
        if request.is_ajax():
            res = {'msg': '该用户可以注册'}
            username = request.POST.get('username')
            if username:
                user = User.objects.filter(username=username).first()
                print(1111, user)
                if user is None:  # 用户不存在,校验两次密码是否一致
                    password = request.POST.get('password')
                    re_password = request.POST.get('re_password')
                    if password != re_password:
                        res = {'pwd': '两次密码不一致'}
                    return JsonResponse(res)
                else:
                    res = {'msg': '该用户已存在'}
                    return JsonResponse(res)
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            re_password = request.POST.get('re_password')
            if username and password and password == re_password:
                User.objects.create_user(username=username, password=password)
                return redirect('/login/')
            else:
                return redirect('/register/')


# 3个随机数（用于随机颜色）
def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# 验证码
def v_code(request):
    # 生成一个图片对象
    img_obj = Image.new('RGB', (150, 34), random_color())
    # 在该图片对象上生成一个画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 生成一个字体对象
    font_obj = ImageFont.truetype('static/font/kumo.ttf', 28)
    temp = []
    for i in range(6):
        l = chr(random.randint(97, 122))  # 小写字母
        b = chr(random.randint(65, 90))  # 大写字母
        n = str(random.randint(0, 9))  # 数字
        t = random.choice([l, b, n])  # 随机选一个
        temp.append(t)
        # 在图片上写入字体（（左右，上下），随机数，随机颜色，字体）
        draw_obj.text((i * 25 + 5, 0), t, fill=random_color(), font=font_obj)
    request.session['v_code'] = ''.join(temp).upper()  # 把生成的验证码保存到session中
    f1 = BytesIO()  # 创建一个内存中的对象
    img_obj.save(f1, format='PNG')  # 把生成的图片保存到内存中，并且指定为png格式
    img_data = f1.getvalue()  # 从对象中获取到这个文件
    return HttpResponse(img_data, content_type='image/png')  # 返回给前端渲染，并且指定格式


# 登录
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 1. 获取用户输入的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('v_code').upper()
        if code == request.session.get('v_code'):  # 校验验证码是否一致
            # 2. 校验用户的账户密码是否正确
            user = auth.authenticate(username=username, password=password)
            if user:
                # 可以登录
                auth.login(request, user)
                path = request.GET.get('next') or '/books/index/'
                return redirect(path)
            else:
                # 登录失败
                error_msg = '账户或密码错误'
        else:
            error_msg = '验证码错误'

        return render(request, 'login.html', {'error_msg': error_msg})


# 退出登录
def logout(request):
    auth.logout(request)
    return redirect('/login/')


# 修改密码
class EditPwd(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'edit_pwd.html')

    @method_decorator(login_required)
    def post(self, request):
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        re_password = request.POST.get('re_password')
        user = request.user
        if user.check_password(old_password):  # 旧密码通过校验
            if new_password == re_password:
                user.set_password(new_password)
                user.save()
                auth.login(request, user)  # 保存我们的登录状态
                return redirect('/books/book_list/')
            else:
                return render(request, 'edit_pwd.html', {'msg': '两次密码不一致'})
        else:
            return render(request, 'edit_pwd.html', {'msg': '输入的旧密码有误'})
