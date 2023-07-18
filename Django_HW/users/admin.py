from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'age', 'email', 'password', 'date_joined')


admin.site.register(User, UserAdmin)
