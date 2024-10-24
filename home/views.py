from django.views.generic import ListView
from products.models import Product


# Create your views here.
class Index(ListView):
    """ View home page """

    template_name = 'home/index.html'
    model = Product
    context_object_name = 'products'

    queryset = Product.objects.filter(has_promotion=True).order_by('-added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_sellers'] = self.queryset[:4]
        return context