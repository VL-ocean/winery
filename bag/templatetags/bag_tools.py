from django import template
from decimal import Decimal


register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(product, quantity):
    """
    Calculate the subtotal for a product.
    """
    price = product.sale_price if product.sale_price else product.price
    return price * quantity
