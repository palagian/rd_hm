from django.views.generic import ListView, DetailView
from .models import Purchase


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase_list.html'
    context_object_name = 'purchases'


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'
    context_object_name = 'purchase'