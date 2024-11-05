from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.db.models import Avg
from django_filters.views import FilterView
from profiles.models import  Wishlist, UserProfile
from reviews.models import Review
from reviews.forms import ReviewProductForm
from checkout.models import OrderLineItem

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
from .filters import ProductFilter
from .mixins import SortingMixin


# Create your views here.
class ProductListView(SortingMixin, ListView):
    """A view to show all products, including sorting and filtering functionality"""

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
    reviews = Review.objects.filter(
        product=product).order_by('-created_on')
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    is_favourited = False
    can_review = False

    if request.user.is_authenticated:

        user_profile = UserProfile.objects.get(user=request.user)

        is_favourited = Wishlist.objects.filter(
            user=request.user, product=product).exists()

        user_has_purchased = OrderLineItem.objects.filter(
            order__user_profile=user_profile, product=product
        ).exists()

        if user_has_purchased or request.user.is_superuser:
            can_review = True
        
        if request.method == 'POST' and can_review:
            review_form = ReviewProductForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                messages.success(
                    request, "Your review has been submitted successfully")
                return redirect('product_detail', product_id=product_id)
        else:
            review_form = ReviewProductForm()
    else:
        review_form = None

    context = {
        'product': product,
        'is_favourited': is_favourited,
        'review_form': review_form,
        'reviews': reviews,
        'average_rating': round(average_rating, 1),
        'can_review': can_review,
    }

    return render(request, 'products/product_detail.html', context)


class ProductFilterView(SortingMixin, FilterView):
    """
    View to display search results
    with filtering and sorting functionality
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


class ProductSearchView(FilterView):
    """
    A class-based view for displaying search results
    """
    model = Product
    template_name = 'products/search_results.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    paginate_by = 12

    def get_queryset(self):
        """
        Filters the products based on the search query
        """
        query = self.request.GET.get("q", "")
        products = Product.objects.all()

        if query:
            products = products.filter(
                Q(name__icontains=query)
                | Q(sku__icontains=query)
                | Q(description__icontains=query)
                | Q(tasting_notes__icontains=query)
                | Q(origin__icontains=query)
                | Q(price__icontains=query)
                | Q(sale_price__icontains=query)
            )
        else:
            messages.error(self.request, "No keywords entered")

        return products

    def get_context_data(self, **kwargs):
        """
        Adds search query to context data
        """
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get("q", "")

        return context


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))