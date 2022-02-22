


from rest_framework.views import ModelViewset

from order.models import Order
from order.serializers import order_serializer


class OrderViewset(ModelViewset):

    serializer_class = OrderSerializer
    queryset = Order.object.all()
