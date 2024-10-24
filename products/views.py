from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product


# Create your views here.
class ProductListView(ListView):
    """A view to show all products, including sorting and search queries"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 12