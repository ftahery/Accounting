# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer,Order,OrderItems,Item
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Item)
