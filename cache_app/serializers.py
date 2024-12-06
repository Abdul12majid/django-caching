from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Product



class ShowProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'serial_number',)