from django import forms
from django.contrib.auth import get_user_model

from users.models import User
from books.models import Book
from purchases.models import Purchase
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('age', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['user', 'book']
