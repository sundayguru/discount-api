from rest_framework import viewsets, permissions
from api.discounts.serializers import DiscountSerializer, SerialNumberSerializer
from discounts.models import Discount, SerialNumber


class DiscountViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class SerialNumberViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = SerialNumber.objects.all()
    serializer_class = SerialNumberSerializer
