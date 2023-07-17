from django.http import JsonResponse
from .models import Purchase


def get_purchases(request):
    purchases = Purchase.objects.all().values()
    return JsonResponse(list(purchases), safe=False)
