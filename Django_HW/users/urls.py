from django.urls import path
from users import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
]
