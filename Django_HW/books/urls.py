from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListView, BookDetailView
from books.api import views as api_views


app_name ='books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail')
]

router = SimpleRouter()
router.register('api', api_views.BookModelViewSet)

urlpatterns += router.urls