# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient

from factories import DiscountFactory, SerialNumberFactory, UserFactory


class DiscountViewTests(TestCase):

    def setUp(self):
        self.user = UserFactory(username="test", password="test")
        self.client = APIClient()

    def test_guest_cannot_list_discount(self):
        resp = self.client.get('/api/v1/discounts/', format='json')
        assert resp.status_code == 403

    def test_user_can_list_discount(self):
        discounts = DiscountFactory.create_batch(size=2)
        for d in discounts:
            d.save()
        self.client.force_authenticate(user=self.user)
        resp = self.client.get('/api/v1/discounts/')
        assert resp.status_code == 200
        assert len(resp.data) == 2


class SerialNumberViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_guest_cannot_list_serialnumber(self):
        resp = self.client.get('/api/v1/serialnumbers/')
        assert resp.status_code == 403

    def test_user_can_list_serialnumber(self):
        user = UserFactory(username="test", password="test")
        serials = SerialNumberFactory.create_batch(size=2)
        for s in serials:
            s.save()
        self.client.force_authenticate(user=user)
        resp = self.client.get('/api/v1/serialnumbers/')
        assert resp.status_code == 200
        assert len(resp.data) == 2

    def test_guest_get_discount_serialnumber(self):
        serial = SerialNumberFactory()
        discount = DiscountFactory()
        serial.save()
        discount.save()
        resp = self.client.post(
            '/api/v1/serialnumbers/discount/', {'serial': serial.serial}
        )
        assert resp.status_code == 200
        assert resp.data['discount'] == discount.code

    def test_returns_arleady_assigned_discount_serialnumber(self):
        discount = DiscountFactory()
        discount.save()
        serial = SerialNumberFactory(discount=discount)
        serial.save()
        another_discount = DiscountFactory()
        another_discount.save()
        resp = self.client.post(
            '/api/v1/serialnumbers/discount/', {'serial': serial.serial}
        )
        assert resp.status_code == 200
        assert resp.data['discount'] == discount.code

    def test_serialnumber_no_discount_available(self):
        serial = SerialNumberFactory()
        serial.save()
        resp = self.client.post(
            '/api/v1/serialnumbers/discount/', {'serial': serial.serial}
        )
        assert resp.status_code == 400
        assert "Unfortunately, no discount available for the provided serial number" in resp.data['non_field_errors']

    def test_wrong_serialnumber(self):
        resp = self.client.post('/api/v1/serialnumbers/discount/', {'serial': 'wrong'})
        assert resp.status_code == 400
        assert "You have provided an invalid serial number" in resp.data['non_field_errors']

    def test_serial_field_required(self):
        resp = self.client.post('/api/v1/serialnumbers/discount/')
        print("RR", resp.data)
        assert resp.status_code == 400
        assert "This field is required." in resp.data['serial']
