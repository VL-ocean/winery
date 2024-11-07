from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Category, Variety, Vintage, Country, Brand, BottleSize, Product
)


class ProductAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage stock via the admin panel
    """

    list_display = [
        "sku",
        "name",
        "category",
        "variety",
        "vintage",
        "origin",
        "price",
        "stock_amount",
    ]
    list_filter = [
        "category",
        "variety",
        "vintage",
        "country",
        "brand",
        "bottle_size",
        "price",
        "stock_amount",
    ]
    search_fields = [
        "name",
        "description",
        "tasting_notes",
        "origin",
    ]
    summernote_fields = (
        "description",
        "tasting_notes",
    )
    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    """
    Allows admin to manage categories via the admin panel
    """

    list_display = ["friendly_name", "name"]


class VarietyAdmin(admin.ModelAdmin):
    """
    Allows admin to manage varieties via the admin panel
    """

    list_display = ["friendly_name", "name"]


class CountryAdmin(admin.ModelAdmin):
    """
    Allows admin to manage countries via the admin panel
    """

    list_display = ["friendly_name", "name"]


class BrandAdmin(admin.ModelAdmin):
    """
    Allows admin to manage brands via the admin panel
    """

    list_display = ["friendly_name", "name"]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Vintage)
admin.site.register(Country, CountryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(BottleSize)
