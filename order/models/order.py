from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeingKey(User, on_delete=models.CASCADE)



