# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0234_auto_20180502_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filplastique',
            name='section',
            field=models.CharField(choices=[('4', '4'), ('6', '6'), ('10', '10'), ('16', '16'), ('25', '25'), ('35', '35'), ('50MM2', '50MM2'), ('3X2,5MM2', '3X2,5MM2'), ('3X1,5MM2', '3X1,5MM2')], max_length=20, verbose_name='SECTION(MILLIMETRE CARRÉ)'),
        ),
        migrations.AlterField(
            model_name='locationstand',
            name='surface_stand',
            field=models.CharField(choices=[('6M2', '6M2'), ('9M2', '9M2'), ('12M2', '12M2')], max_length=100, verbose_name='SURFACE (M²)'),
        ),
        migrations.AlterField(
            model_name='onduleur',
            name='puissance',
            field=models.CharField(choices=[('110VA', '110VA'), ('650VA', '650VA'), ('600VA', '600VA'), ('700VA', '700VA'), ('1200VA', '1200VA'), ('900VA', '900VA'), ('1500VA', '1500VA'), ('110VA', '110VA'), ('2000VA', '2000VA'), ('200VA', '200VA'), ('750VA', '750VA'), ('1000VA', '1000VA'), ('1100VA', '1100VA')], max_length=20, verbose_name='PUISSANCE'),
        ),
    ]
