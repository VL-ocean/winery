from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django_filters.views import FilterView
from .models import Product
from .filters import ProductFilter
from .mixins import SortingMixin


# Create your views here.
class ProductListView(SortingMixin, ListView):
    """A view to show all products, including sorting and search queries"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):

        queryset = super().get_queryset()
        product_filter = ProductFilter(
            self.request.GET or None, queryset=queryset)
        queryset = product_filter.qs

        queryset = self.apply_sorting(queryset)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product_filter = ProductFilter(
            self.request.GET or None, queryset=self.get_queryset())
        context['filter'] = product_filter

        get_params = self.request.GET.copy()
        if 'page' in get_params:
            get_params.pop('page')

        context['query_string'] = get_params.urlencode()
        return context


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


class ProductSearchView(SortingMixin, FilterView):
    """
    View to display search results
    with filtering and sorting functionality.
    """
    model = Product
    template_name = 'products/search_results.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        queryset = self.filterset.qs

        return self.apply_sorting(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form

        get_params = self.request.GET.copy()
        if 'page' in get_params:
            get_params.pop('page')

        context['query_string'] = get_params.urlencode()
        return context