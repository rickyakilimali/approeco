# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-10 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0288_auto_20180507_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filbarbele',
            name='category',
        ),
        migrations.RemoveField(
            model_name='filbarbele',
            name='vendeur',
        ),
        migrations.RemoveField(
            model_name='paquetclouabeton',
            name='category',
        ),
        migrations.RemoveField(
            model_name='paquetclouabeton',
            name='vendeur',
        ),
        migrations.RemoveField(
            model_name='pinceau',
            name='category',
        ),
        migrations.RemoveField(
            model_name='pinceau',
            name='vendeur',
        ),
        migrations.RemoveField(
            model_name='plantoir',
            name='category',
        ),
        migrations.RemoveField(
            model_name='plantoir',
            name='vendeur',
        ),

        migrations.DeleteModel(
            name='FilBarbele',
        ),
        migrations.DeleteModel(
            name='PaquetClouABeton',
        ),
        migrations.DeleteModel(
            name='Pinceau',
        ),
        migrations.DeleteModel(
            name='Plantoir',
        ),
    ]
