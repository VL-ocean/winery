from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("order_history/<order_number>", views.order_history, name="order_history"),
    path(
        "user/wishlist_add/<str:pk>/",
        views.add_remove_wishlist_items,
        name="manage-wishlist",
    ),
    path("user/<int:pk>/wishlist/", views.MyWishlistView.as_view(), name="my-wishlist"),
]
