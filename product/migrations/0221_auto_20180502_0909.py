# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0220_auto_20180430_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureau',
            name='longueur',
            field=models.CharField(choices=[('40CM', '40CM'), ('92CM', '92CM'), ('91CM', '91CM'), ('120CM', '120CM'), ('150CM', '150CM'), ('170CM', '170CM'), ('140CM', '140CM'), ('160CM', '160CM'), ('180CM', '180CM'), ('120CM', '120CM'), ('150CM', '150CM'), ('170CM', '170CM'), ('1.40 MTR', '1.40 MTR'), ('1.60 MTR', '1.60 MTR'), ('1.80 MTR', '1.80 MTR'), ('1.20 MTR', '1.20 MTR'), ('2.4 MTR', '2.4 MTR'), ('3.5 MTR', '3.5 MTR')], max_length=20, verbose_name='LONGUEUR(CENTIMETRE)'),
        ),
    ]
