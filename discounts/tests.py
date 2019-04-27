# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from discounts.models import Discount, SerialNumber


class ModelTests(TestCase):

    def test_discount_model_string(self):
        discount = Discount(code="test")
        assert str(discount) == "test"

    def test_serial_number_model_string(self):
        discount = SerialNumber(serial="1234")
        assert str(discount) == "1234"
