from django.urls import path
from .views import PurchaseListView, PurchaseDetailView


app_name = 'purchases'

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
]