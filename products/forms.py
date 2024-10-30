from django import forms


class SortForm(forms.Form):
    """
    Form to allow users to sort products

    """

    SORT_CHOICES = [
        ('', 'Sort by'),
        ('price_asc', 'Price: low to high'),
        ('price_desc', 'Price: high to low'),
        ('name_asc', 'Name: A to Z'),
        ('name_desc', 'Name: Z to A'),
    ]

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
