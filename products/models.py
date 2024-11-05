from django.db import models

# Create your models here.


class Category(models.Model):
    """
    A model for categorising products
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Variety(models.Model):
    """
    A model for the allocation of products to varieties
    """

    class Meta:
        verbose_name_plural = "Varieties"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Vintage(models.Model):
    """
    A model to define production year
    """

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    A model to specify country of origin
    """

    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """
    A model to specify product brand
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class BottleSize(models.Model):
    """
    A model to specify bottle size of products
    """

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A model for products
    """

    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    tasting_notes = models.TextField(null=True, blank=True)
    variety = models.ForeignKey(
        Variety, null=True, blank=True, on_delete=models.SET_NULL
    )
    vintage = models.ForeignKey(
        Vintage, null=True, blank=True, on_delete=models.SET_NULL
    )
    origin = models.CharField(max_length=254)
    country = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    bottle_size = models.ForeignKey(
        BottleSize, null=True, blank=True, on_delete=models.SET_NULL
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.FileField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_promotion = models.BooleanField(default=False, null=True, blank=True)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    added = models.DateTimeField(auto_now_add=True)
    stock_amount = models.IntegerField(default=1)

    def get_final_price(self):
        """
        Returns the price of item based on sale price
        """
        return self.sale_price if self.sale_price else self.price

    def calc_average_rating(self):
        """
        Calculates average rating for reviews
        """
        reviews = self.review_set.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0

    def __str__(self):
        return f"{self.name}"
