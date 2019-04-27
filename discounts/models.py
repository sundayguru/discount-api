# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Discount(models.Model):
    code = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class SerialNumber(models.Model):
    serial = models.CharField(max_length=200)
    discount = models.OneToOneField(
        Discount, related_name="serial_number", null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial
