from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns=[
    path("categories/<str:category_name>/products/",Categories.as_view()),
    path("categories/<str:category_name>/products/<product_id>",Product.as_view()),
    path("categories/<str:category_name>/products?top=<n>&min_price=<min_price>&max_price=<max_price>/",Product.as_view())
]