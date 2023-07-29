from rest_framework.viewsets import ModelViewSet

from books.api.filters import BookFilter
from books.api.serializers import BookSerializer
from books.models import Book


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter