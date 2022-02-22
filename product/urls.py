from django.urls import path, include
from rest_framework import routers

from product import viewset

route = routers.SimpleRouter()
route.register(r'product', viewset.ProductViewset, basename='product')
route.register(r'category', viewset.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(route.urls)),
]