# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from discounts.models import Discount, SerialNumber


class DiscounAdmin(admin.ModelAdmin):
    list_display = ('code', 'created')


class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ('serial', 'created')


admin.site.register(Discount, DiscounAdmin)
admin.site.register(SerialNumber, SerialNumberAdmin)