from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from pizzashop.shopapp.models import Condiment, PizzaType, Pizza, Cart, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CondimentSerializer(ModelSerializer):
    class Meta:
        model = Condiment
        fields = '__all__'


class PizzaTypeSerializer(ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
        depth = 2


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 2


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2