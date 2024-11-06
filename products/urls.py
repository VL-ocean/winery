from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('filter/', views.ProductFilterView.as_view(), name='product_filter'),
    path('search/', views.ProductSearchView.as_view(), name='product_search'),
    path('offers/', views.PromotionsView.as_view(), name='promotions'),
]