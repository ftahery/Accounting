# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+1234567890'. Up to 10 digits allowed")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=10)
    email = models.EmailField()
    billing_address = models.CharField(max_length=500)
    shipping_address = models.CharField(max_length=500)

class Item(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=10)
    retail_price = models.FloatField()
    selling_price = models.FloatField()
    color = models.CharField(max_length=10)
    new_item = models.BooleanField()

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    order_date = models.DateField()
    order_status = models.CharField(max_length=20)
    total_price = models.FloatField()

class OrderItems(models.Model):
    order = models.ForeignKey(Order)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=10)
    email = models.EmailField()
    joining_date = models.DateField();
    salary = models.FloatField()
    role = models.CharField(max_length=50)


