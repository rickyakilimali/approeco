# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0205_auto_20180424_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreposage',
            name='type_entreposage',
            field=models.CharField(choices=[('ENTREPOSAGE SIMPLE', 'ENTREPOSAGE SIMPLE'), ('GESTION ENTREPOSAGE', 'GESTION ENTREPOSAGE')], max_length=50, verbose_name='TYPE ENTREPOSAGE'),
        ),
    ]
