from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Products
        fields = '__all__'


class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class AuctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
