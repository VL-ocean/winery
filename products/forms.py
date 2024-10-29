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
        ('vintage_asc', 'Vintage: old to new'),
        ('vintage_desc', 'Vintage: new to old'),
        ('added_desc', 'Newest'),
    ]

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
