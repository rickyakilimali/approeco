# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0242_auto_20180503_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compresseur',
            name='puissance_compresseur',
            field=models.CharField(choices=[('2 HP', '2 HP'), ('3 HP', '3 HP'), ('4 HP', '4 HP'), ('5,5 HP', '5,5 HP'), ('6,5 HP', '6,5 HP'), ('7,5 HP', '7,5 HP'), ('10 HP', '10 HP')], max_length=20, verbose_name='PUISSANCE (WATT)'),
        ),
    ]
