from discounts.models import Discount, SerialNumber
from rest_framework import serializers


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discount
        fields = ('url', 'code', 'created')


class SerialNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SerialNumber
        fields = ('url', 'serial', 'created')
