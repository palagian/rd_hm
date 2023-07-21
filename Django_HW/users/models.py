from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)


    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.id}: {self.username}"