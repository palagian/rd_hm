import django_filters

from purchases.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'id': ['exact', 'gte', 'lte'],
            'purchase_date': ['exact', 'gte', 'lte'],
        }