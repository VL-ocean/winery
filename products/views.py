from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product


# Create your views here.
# def all_products(request):
#     """A view to show all products, including sorting and search queries"""

#     products = Product.objects.all()

#     paginator = Paginator(products, 12)  # Show 12 products per page.

#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     context = {
#         "products": products,
#         "page_obj": page_obj,
#     }

#     return render(request, "products/products.html", context)


class ProductListView(ListView):
    """A view to show all products, including sorting and search queries"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 12