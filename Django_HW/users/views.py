from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import User
from .tasks import print_users_purchases


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


def user_list(request):
    users = User.objects.all()
    user_ids = [user.id for user in users]
    print_users_purchases.delay(user_ids)

    return render(request, 'user_list.html', {'users': users})
