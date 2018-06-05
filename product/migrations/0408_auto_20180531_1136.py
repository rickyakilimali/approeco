# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-31 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0407_auto_20180531_1123'),
    ]

    operations = [

        migrations.AlterField(
            model_name='cableinformatique',
            name='longueur',
            field=models.CharField(choices=[('2M', '2M'), ('5M', '5M'), ('10M', '10M'), ('20M', '20M'), ('100M', '100M'), ('300M', '300M'), ('305M', '305M'), ('30CM', '30CM')], max_length=50, verbose_name='LONGUEUR'),
        ),
        migrations.AlterField(
            model_name='cableinformatique',
            name='type_cable',
            field=models.CharField(choices=[('HDMI', 'HDMI'), ('VGA', 'VGA'), ('FIREWARE', 'FIREWARE'), ('OPTICAL', 'OPTICAL'), ('CAT 6', 'CAT 6'), ('COAXIAL', 'COAXIAL'), ('MICRO', 'MICRO'), ('BAFFLE', 'BAFFLE'), ('SON (1*1)', 'SON (1*1)'), ('MAC THUNDER', 'MAC THUNDER')], max_length=50, verbose_name='TYPE DE CABLE'),
        ),
    ]