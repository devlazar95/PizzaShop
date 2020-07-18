import uuid

from django.db import models


class Condiment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='')


class PizzaType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='')


class Pizza(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE, related_name='pizza', blank=False, null=True)
    size = models.FloatField(default=0)
    price = models.FloatField(default=0)
    weight = models.FloatField(default=0, null=True, blank=True)
    home_special_offer = models.BooleanField(default=False)


class Cart(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='pizzas', blank=False, null=True)


class Order(models.Model):
    order_no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='pizza', blank=False, null=True)