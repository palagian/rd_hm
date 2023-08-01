from rest_framework import serializers
from purchases.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    user_display = serializers.CharField(source='user.username', read_only=True)
    book_display = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'user_display', 'book', 'book_display', 'purchase_date']
        read_only_fields = ('purchase_date', 'id', )
