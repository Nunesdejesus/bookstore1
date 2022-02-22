


from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategoyViewset(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.object.all()
