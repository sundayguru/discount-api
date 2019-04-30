from rest_framework import permissions, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.discounts.serializers import (DiscountSerializer,
                                       SerialNumberDiscountSerializer,
                                       SerialNumberSerializer)
from discounts.models import Discount, SerialNumber


class DiscountViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class SerialNumberViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = SerialNumber.objects.all()
    serializer_class = SerialNumberSerializer

    @list_route(methods=['POST'], permission_classes=(permissions.AllowAny,), serializer_class=SerialNumberDiscountSerializer)
    def discount(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response({"discount": instance.discount.code})
