# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0118_auto_20180201_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batteriesolaire',
            name='capacite',
            field=models.CharField(choices=[('102Ah', '102Ah'), ('100Ah', '100Ah'), ('200Ah', '200Ah'), ('1130Ah', '1130Ah')], max_length=20, verbose_name='CAPACITE'),
        ),
        migrations.AlterField(
            model_name='batteriesolaire',
            name='tension',
            field=models.CharField(choices=[('2V', '2V'), ('12V', '12V')], max_length=20, verbose_name='TENSION'),
        ),
        migrations.AlterField(
            model_name='transportbienintrakinshasa',
            name='assurance',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=100, verbose_name='ASSURANCE'),
        ),
        migrations.AlterField(
            model_name='transportbienintrakinshasa',
            name='duree_location',
            field=models.CharField(choices=[('DEMI-JOURNEE(4H)', 'DEMI-JOURNEE(4H)'), ('JOURNEE(8H)', 'JOURNEE(8H)')], max_length=100, verbose_name='DUREE LOCATION'),
        ),
    ]
