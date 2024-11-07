from django.shortcuts import render


# Create your views here.
def privacy_policy_view(request):
    """
    View to render the Privacy Policy page.
    """
    return render(request, "customer_service/privacy_policy.html")


def terms_n_conditions_view(request):
    """
    View to render the Terms of Service page.
    """
    return render(request, "customer_service/terms_n_conditions.html")
