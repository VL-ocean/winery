from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from products.mixins import SortingMixin
from products.models import Product

from .models import UserProfile, Wishlist
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_remove_wishlist_items(request, pk):
    """
    Add or remove a product from the wishlist.
    """
    product = get_object_or_404(Product, pk=pk)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)

    if not created:

        wishlist_item.delete()
        messages.success(
            request, f"{product.name} has been removed from your wishlist")
    else:

        messages.success(
            request, f"{product.name} has been added to your wishlist")

    return redirect(request.META.get('HTTP_REFERER', 'home'))


class MyWishlistView(LoginRequiredMixin, SortingMixin, ListView):
    """
    Class-based view to display user's wishlist with sorting and pagination.
    """
    model = Wishlist
    template_name = 'profiles/wishlist.html'
    context_object_name = 'wishlist'
    paginate_by = 12

    def get_queryset(self):
        """
        Get the user's wishlist items and apply sorting.
        """
        profile = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        queryset = Wishlist.objects.filter(
            user=profile.user
        ).select_related('product')

        queryset = self.apply_sorting(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add the query string to the context
        to preserve sorting during pagination.
        """
        context = super().get_context_data(**kwargs)

        get_params = self.request.GET.copy()
        if 'page' in get_params:
            get_params.pop('page')

        context['query_string'] = get_params.urlencode()

        return context