from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('book_list/', views.book_list),
    path('del_book/', views.del_book),
    path('edit_book/', views.Editbook.as_view()),
    path('add_book/', views.Addbook.as_view()),
]