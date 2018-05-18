# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0322_calendrier_quantite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casquette',
            name='quantite',
            field=models.CharField(choices=[('1-100', '1-100'), ('201-500', '201-500'), ('501-1000', '501-1000'), ('1001-2000', '1001-2000'), ('2001-5000', '2001-5000'), ('5001-10000', '5001-10000'), ('10000<', '10000<')], max_length=50),
        ),
    ]
