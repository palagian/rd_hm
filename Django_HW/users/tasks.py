from celery import shared_task
from celery.schedules import crontab
from datetime import timedelta

from Django_HW.celery import app
from .models import User
from purchases.models import Purchase


@shared_task
def print_hello_celery():
    print("This is my first celery task")


@shared_task
def print_users_purchases(user_id):
    try:
        user = User.objects.get(pk=user_id)
        purchase_count = Purchase.objects.filter(user=user).count()
        print(f"Purchase count for user {user.username}: {purchase_count}")
    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist")


@shared_task
def print_user_count():
    user_count = User.objects.count()
    print(f"Number of users in the database: {user_count}")
