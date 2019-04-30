from rest_framework import serializers

from discounts.models import Discount, SerialNumber


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discount
        fields = ('url', 'code', 'created')


class SerialNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SerialNumber
        fields = ('url', 'serial', 'discount', 'created')


class SerialNumberDiscountSerializer(serializers.Serializer):
    serial = serializers.CharField()

    def validate(self, data):
        self.serial_number = SerialNumber.objects.filter(
            serial=data.get('serial')
        ).first()
        if not self.serial_number:
            raise serializers.ValidationError(
                'You have provided an invalid serial number'
            )

        if self.serial_number.discount is None:
            self.discount = Discount.objects.filter(serial_number=None).first()
            if not self.discount:
                raise serializers.ValidationError(
                    'Unfortunately, no discount available for the provided serial number'
                )

        return data

    def create(self, data):
        if not self.serial_number.discount:
            self.serial_number.discount = self.discount
            self.serial_number.save()
        return self.serial_number
