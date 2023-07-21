from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('books/', include('books.urls', namespace='books')),
    path('purchases/', include('purchases.urls', namespace='purchases')),
    path('create/', include('create.urls', namespace='create'))
]
