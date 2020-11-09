from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.PositiveIntegerField(default=1)


class Coupon(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    discount = models.FloatField()
