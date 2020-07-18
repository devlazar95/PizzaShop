from django.contrib import admin

from .models import PizzaType, Pizza, Order, Cart, Condiment

admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Condiment)
