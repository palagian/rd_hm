from django.db import models

class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()

    class Meta:
        db_table = 'book'
        unique_together = ['title', 'author']

    def __str__(self):
        return f"{self.id}: {self.title} - {self.author}"
