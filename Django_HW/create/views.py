from django.views.generic import ListView, CreateView
from users.models import User
from books.models import Book
from purchases.models import Purchase
from .forms import UserForm, BookForm, PurchaseForm


class CreateListView(ListView):
    template_name = 'create_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return ['User', 'Book', 'Purchase']


class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = '/users/'


class CreateBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create_book.html'
    success_url = '/books/'


class CreatePurchaseView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'create_purchase.html'
    success_url = '/purchases/'
