from rest_framework import serializers
from .models import *

class CategeroiesSerlializer(serializers.Serializer):
    class Meta:
        model=Categoris
        fields=["__all__"]

class ProductsSerlializer(serializers.Serializer):
    class Meta:
        model=Product_table
        fields=["__all__"]
