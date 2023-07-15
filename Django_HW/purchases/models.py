from django.db import models
from users.models import User
from books.models import Book

class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'
        ordering = ['-purchase_date']

