


from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return product.object.all()
