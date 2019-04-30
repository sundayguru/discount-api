import factory
from discounts.models import Discount, SerialNumber
from django.contrib.auth.models import User


class DiscountFactory(factory.Factory):
    class Meta:
        model = Discount

    code = factory.Faker('first_name')


class SerialNumberFactory(factory.Factory):
    class Meta:
        model = SerialNumber

    serial = factory.Faker('name')


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = factory.Faker('email')
    password = factory.Faker('name')