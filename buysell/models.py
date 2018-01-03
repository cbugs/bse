from django.db import models
from django.urls import reverse
# multiple select field contrib
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Product category such as shoes, clothes, tablets, etc...
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    # types of products: buy, sell, exchange
    BUY_SELL_EXCHANGE = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
        ('exchange', 'Exchange'),
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = MultiSelectField(choices=BUY_SELL_EXCHANGE, verbose_name="Product Type")
    description = models.TextField(verbose_name="Enter description and contact infos")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # where to redirect after model submit
    def get_absolute_url(self):
        return reverse('buysell:index')

    def __str__(self):
        return self.name