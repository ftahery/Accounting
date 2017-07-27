# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 17:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountingApp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='new_item',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+1234567890'. Up to 10 digits allowed", regex=b'^\\+?1?\\d{9,10}$')]),
        ),
    ]