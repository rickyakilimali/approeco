# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0222_auto_20180502_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cablesouple',
            name='section',
            field=models.CharField(choices=[('4', '4'), ('6', '6'), ('10', '10'), ('16', '16'), ('25', '25'), ('35', '35'), ('50MM2', '50MM2'), ('3X2,5MM2', '3X2,5MM2'), ('3X1,5MM2', '3X1,5MM2')], max_length=20, verbose_name='SECTION(MILLIMETRE CARRÉ)'),
        ),
    ]