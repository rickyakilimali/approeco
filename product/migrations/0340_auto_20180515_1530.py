# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-15 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0339_auto_20180515_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baredemine',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='rollup',
            name='quantite',
            field=models.CharField(choices=[('1-20', '1-20'), ('21-50', '21-50'), ('51-100', '51-100'), ('101<', '101<'), ('1-19', '1-19'), ('20-49', '20-49'), ('50-99', '50-99'), ('100<', '100<')], max_length=50, verbose_name='QUANTITE'),
        ),
    ]
