from rest_framework.viewsets import ModelViewSet

from purchases.api.filters import PurchaseFilter
from purchases.api.serializers import PurchaseSerializer
from purchases.models import Purchase


class PurchaseModelViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter