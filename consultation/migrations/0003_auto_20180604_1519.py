# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0002_auto_20180530_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Moins de 250 employés'),
        ),
        migrations.AlterField(
            model_name='itemprice',
            name='price2',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Moins de 250 employés'),
        ),
    ]
