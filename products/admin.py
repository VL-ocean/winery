from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Category, Variety, Vintage, Country, Brand, BottleSize, Product
)

class ProductAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage stock via the admin panel
    """
    list_display = ['name', 'variety', 'vintage', 'origin', 'price', 'stock_amount']
    list_filter = ['category', 'variety', 'vintage', 'country', 'brand', 'bottle_size']
    search_fields = ['name', 'description',  'tasting_notes',  'origin', ]
    summernote_fields = ('description', 'tasting_notes',)
    ordering = ('-added',)


# class ReviewAdmin(admin.ModelAdmin):
#     """Allows admin to manage reviews on products via the admin panel"""
#     list_display = ['user', 'product', 'content', 'created_at']
#     list_filter = ('created_at',)
#     search_fields = ['user', 'content', 'product']


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Variety)
admin.site.register(Vintage)
admin.site.register(Country)
admin.site.register(Brand)
admin.site.register(BottleSize)
