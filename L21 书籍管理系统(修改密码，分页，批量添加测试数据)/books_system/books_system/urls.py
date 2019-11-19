"""books_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # 书籍APP， 二级路由
    path('register/', views.Register.as_view()),  # 注册
    path('login/', views.Login.as_view()),  # 登录
    path('logout/', views.logout),  # 退出登录
    path('v_code/', views.v_code, name='code'),  # 验证码
    path('edit_pwd/', views.EditPwd.as_view()),  # 修改密码
    path('add_ceshi/', views.add_ceshi),  # 修改密码
]
