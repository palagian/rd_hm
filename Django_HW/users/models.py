from django.db import models

class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

