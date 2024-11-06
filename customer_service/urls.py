from django.urls import path
from . import views


urlpatterns = [
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    # path(
    #     'terms-of-service/',
    #     views.terms_of_service_view, name='terms-of-service'),
]