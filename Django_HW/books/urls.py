from django.urls import path
from books import views


urlpatterns = [
    path('', views.get_books, name='get_books')
]