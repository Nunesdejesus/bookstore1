from django.urls import path, include
from rest_framework import routers

from order import viewsets

route = routers.SimpleRouter()
router.register(r'order', viewsets.order_viewset, basename='order')


urlpatterns =[
    path('', include(router.urls)),
]