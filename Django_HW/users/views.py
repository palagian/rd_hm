from django.http import JsonResponse
from .models import User


def get_users(request):
    users = User.objects.all().values()
    return JsonResponse(list(users), safe=False)
