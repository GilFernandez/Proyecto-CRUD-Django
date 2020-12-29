from . import views
from django.urls import path

urlpatterns = [     
    path('welcome', views.welcome),
    path('register', views.register),
    path('', views.login),
    path('logout', views.logout),
    path('book-list', views.bookList, name='book-list'),
    path('book-create', views.bookCreate, name='book-create'),
    path('book-update/<int:id>', views.bookUpdate, name='book-update'),
    path('book-delete/<int:id>', views.bookDelete, name='book-delete'),
]