from django.urls import path
from purchases import views


urlpatterns = [
    path('', views.get_purchases, name='get_purchases')
]