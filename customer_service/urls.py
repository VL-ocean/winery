from django.urls import path
from . import views


urlpatterns = [
    path("privacy-policy/", views.privacy_policy_view, name="privacy_policy"),
    path(
        "terms-n-conditions/",
        views.terms_n_conditions_view, name="terms_n_conditions"
    ),
]
