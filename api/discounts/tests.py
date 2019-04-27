# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from factories import DiscountFactory, UserFactory, SerialNumberFactory


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
        self.user = UserFactory(username="test", password="test")

    def test_guest_cannot_list_serialnumber(self):
        resp = self.client.get('/api/v1/serialnumbers/')
        assert resp.status_code == 403

    def test_user_can_list_serialnumber(self):
        serials = SerialNumberFactory.create_batch(size=2)
        for s in serials:
            s.save()
        self.client.force_authenticate(user=self.user)
        resp = self.client.get('/api/v1/serialnumbers/')
        assert resp.status_code == 200
        assert len(resp.data) == 2
