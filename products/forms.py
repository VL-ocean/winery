from django import forms
from .widgets import CustomClearableFileInput
from .models import (
    Product, Category, Variety, Vintage, Country, Brand, BottleSize
)


class SortForm(forms.Form):
    """
    Form to allow users to sort products

    """

    SORT_CHOICES = [
        ("", "Sort by"),
        ("price_asc", "Price: low to high"),
        ("price_desc", "Price: high to low"),
        ("name_asc", "Name: A to Z"),
        ("name_desc", "Name: Z to A"),
    ]

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        varieties = Variety.objects.all()
        vintages = Vintage.objects.all()
        countries = Country.objects.all()
        brands = Brand.objects.all()
        bottle_size = BottleSize.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_variety = [(
            c.id, c.get_friendly_name()
        ) for c in varieties]
        friendly_names_country = [(
            c.id, c.get_friendly_name()
        ) for c in countries]
        friendly_names_brand = [(
            c.id, c.get_friendly_name()
        ) for c in brands]

        self.fields["category"].choices = friendly_names
        self.fields["variety"].choices = friendly_names_variety
        self.fields["country"].choices = friendly_names_country
        self.fields["brand"].choices = friendly_names_brand
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-dark"
