from django.db import models
from users.models import UserModel


class Shop(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductSales(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    sell = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)


