from django.urls import path
from . import views

urlpatterns = [
    path('books_list/', views.books_list),
    # path('add_book/', views.books_list),
    # path('edit_book/', views.books_list),
    # path('del_book/', views.books_list),
]