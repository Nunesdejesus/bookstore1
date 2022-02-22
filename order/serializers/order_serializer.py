from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, Many=True)
    total = serializers.SerializerMethodField()


    def get_total(self, instance):
        total = sum([product.price for product in instance.produt..all()])
        return total

    class Meta:
        model = Order
        fields = ['product', 'total','User', 'products_id']
        extra_kwargs = {'product': {'required': False}}

    def creat(self, validade_data):
        product_data = validade_data.pop(products_id)
        user_data = validade_data.pop('user')

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)

            return order
