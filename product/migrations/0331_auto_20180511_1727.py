# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0330_auto_20180511_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autocollantvinyleadhesif',
            name='quantite',
            field=models.CharField(choices=[('1-500M2', '1-500M2'), ('501-1000M2', '501-1000M2'), ('1001-2000M2', '1001-2000M2'), ('2000M2<', '2000M2<')], max_length=50, verbose_name='QUANTITE'),
        ),
    ]
