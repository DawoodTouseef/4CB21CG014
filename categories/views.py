from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from django.http import HttpResponse,JsonResponse
from .serializers import *


# Create your views here.

class Categories(APIView):
    def get(self,request,*arg,**kwargs):
        category_name=kwargs.get("category_name")
        model=Categoris.objects.filter(id__range=(1,10))
        ser=CategeroiesSerlializer(data=model)
        if ser.is_valid():
            return JsonResponse(ser.data)
        return JsonResponse({"message":"No Products Found"})

class Product(APIView):
    def get(self,request,*arg,**kwargs):
        product_id=kwargs.get("product_id")
        max_price=kwargs.get("max_price")
        min_price=kwargs.get("min_price")
        top=kwargs.get("n")
        if max_price and min_price:
            products=Product_table.objects.filter(pk=product_id,price__range=(max_price,min_price))
        elif top and max_price and min_price:
            products=Product_table.objects.filter(pk__range=(1,top),price__range=(max_price,min_price))
        else:
            products=Product_table.objects.filter(pk=product_id)
        
        p=ProductsSerlializer(products)
        content={"Product_name":p.data}
        return JsonResponse(content)

