from django.urls import path
from . import views


urlpatterns = [
    # path('', views.all_products, name='products')
    path('', views.ProductListView.as_view(), name='all_products'),
]