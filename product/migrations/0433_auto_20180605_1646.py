# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-05 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0432_auto_20180605_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationhoteletranger',
            name='units',
            field=models.CharField(choices=[('USD/CHAMBRE', 'USD/CHAMBRE')], max_length=50, verbose_name='UNITÉ'),
        ),
    ]