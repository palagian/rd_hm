from django.urls import path
from . import views

app_name = 'create'

urlpatterns = [
    path('', views.CreateListView.as_view(), name='create-list'),
    path('user/', views.CreateUserView.as_view(), name='create-user'),
    path('book/', views.CreateBookView.as_view(), name='create-book'),
    path('purchase/', views.CreatePurchaseView.as_view(), name='create-purchase'),
]
