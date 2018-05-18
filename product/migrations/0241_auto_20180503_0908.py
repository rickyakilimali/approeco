# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0240_auto_20180503_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compresseur',
            name='capacite_compresseur',
            field=models.CharField(choices=[('6 LITRES', '6 LITRES'), ('24 LITRES', '24 LITRES'), ('50 LITRES', '50 LITRES'), ('100 LITRES', '100 LITRES'), ('200 LITRES', '200 LITRES'), ('300 LITRES', '300 LITRES')], max_length=20, verbose_name='CAPACITE (LITRE)'),
        ),
        migrations.AlterField(
            model_name='compresseur',
            name='marque_marchine',
            field=models.CharField(choices=[('EINHELL', 'EINHELL')], max_length=20, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='compresseurair',
            name='capacite_compresseur',
            field=models.CharField(choices=[('6 LITRES', '6 LITRES'), ('24 LITRES', '24 LITRES'), ('50 LITRES', '50 LITRES'), ('100 LITRES', '100 LITRES'), ('200 LITRES', '200 LITRES'), ('300 LITRES', '300 LITRES')], max_length=100, verbose_name='CAPACITE COMPRESSEUR'),
        ),
    ]
