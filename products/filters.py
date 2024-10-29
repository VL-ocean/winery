import django_filters
from django.db.models import Q
from django import forms
from .models import Category, Variety, Vintage, Country, Brand, BottleSize, Product


class ProductFilter(django_filters.FilterSet):
    """
    Fields for product filters
    """
    PRICE_RANGE_CHOICES = [
        ('up_to_20', 'Up to €20'),
        ('20_50', '€20 - €50'),
        ('50_100', '€50 - €100'),
        ('over_100', 'Over €100'),
    ]


    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        label='Category',
        widget=forms.CheckboxSelectMultiple
    )
    variety = django_filters.ModelMultipleChoiceFilter(
        queryset=Variety.objects.all(),
        label='Variety',
        widget=forms.CheckboxSelectMultiple
    )
    vintage = django_filters.ModelMultipleChoiceFilter(
        queryset=Vintage.objects.all(),
        label='Vintage',
        widget=forms.CheckboxSelectMultiple
    )
    country = django_filters.ModelMultipleChoiceFilter(
        queryset=Country.objects.all(),
        label='Country',
        widget=forms.CheckboxSelectMultiple
    )
    brand = django_filters.ModelMultipleChoiceFilter(
        queryset=Brand.objects.all(),
        label='Brand',
        widget=forms.CheckboxSelectMultiple
    )
    bottle_size = django_filters.ModelMultipleChoiceFilter(
        queryset=BottleSize.objects.all(),
        label='Bottle Size',
        widget=forms.CheckboxSelectMultiple
    )

    price_ranges = django_filters.MultipleChoiceFilter(
        label='Price Ranges',
        choices=PRICE_RANGE_CHOICES,
        method='filter_multiple_price_ranges',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        """
        Meta class for the filter
        """
        model = Product
        fields = [
            'category', 'variety', 'vintage',
            'country', 'brand', 'bottle_size', 'price_ranges']


    def filter_multiple_price_ranges(self, queryset, name, value):
        """
        Filters the queryset based on selected price ranges.
        Supports multiple selections and
        includes both price and sale_price.
        """
        queries = Q()
        if 'up_to_20' in value:
            queries |= (
                Q(sale_price__lte=20)
                | Q(sale_price__isnull=True, price__lte=20)
            )
        if '20_50' in value:
            queries |= (
                Q(sale_price__gte=20, sale_price__lte=50) |
                Q(sale_price__isnull=True, price__gte=20, price__lte=50)
            )
        if '50_100' in value:
            queries |= (
                Q(sale_price__gte=50, sale_price__lte=100) |
                Q(sale_price__isnull=True, price__gte=50, price__lte=100)
            )
        if 'over_100' in value:
            queries |= (
                Q(sale_price__gte=100)
                | Q(sale_price__isnull=True, price__gte=100)
            )

        return queryset.filter(queries).distinct()
