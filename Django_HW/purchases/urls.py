from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PurchaseListView, PurchaseDetailView
from purchases.api import views as api_views


app_name = 'purchases'

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
]

router = SimpleRouter()
router.register('api', api_views.PurchaseModelViewSet)

urlpatterns += router.urls