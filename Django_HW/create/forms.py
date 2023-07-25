from django import forms
from users.models import User
from books.models import Book
from purchases.models import Purchase


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'password']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['user', 'book']
