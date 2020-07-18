from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import CondimentsView, PizzaTypeView, PizzaView, OrderView, CartView
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .serializers \
    import PizzaTypeSerializer, \
    CondimentSerializer, PizzaSerializer, OrderSerializer, CartSerializer

urlpatterns = [
    path('condiments/', CondimentsView.as_view(), name='condiments'),
    path('pizza-types/', PizzaTypeView.as_view(), name='pizzatypes'),
    path('pizza/', PizzaView.as_view(), name='pizzas'),
    path('order/', OrderView.as_view(), name='order'),
    path('cart/', CartView.as_view(), name='cart'),
]

urlpatterns = format_suffix_patterns(urlpatterns)