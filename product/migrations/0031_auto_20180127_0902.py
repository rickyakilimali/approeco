# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-27 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_auto_20180127_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insertionpublicitaire',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
    ]