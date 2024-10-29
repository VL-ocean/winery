from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.ProductSearchView.as_view(), name='product_search'),
]