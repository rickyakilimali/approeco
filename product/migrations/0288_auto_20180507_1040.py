# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-07 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0287_auto_20180507_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineagricole',
            name='consommation',
            field=models.CharField(choices=[('0,7L/H', '0,7L/H')], max_length=100, verbose_name='CONSOMMATION(LITRE/HEURE)'),
        ),
        migrations.AlterField(
            model_name='machineagricole',
            name='puissance',
            field=models.CharField(choices=[('3,5 CV', '3,5 CV')], max_length=100, verbose_name='PUISSANCE (WATT)'),
        ),
        migrations.AlterField(
            model_name='machineagricole',
            name='rendement',
            field=models.CharField(choices=[('600KG/HEURE', '600KG/HEURE')], max_length=100, verbose_name='RENDEMENT (KILOGRAMME/HEURE)'),
        ),
        migrations.AlterField(
            model_name='machineagricole',
            name='type_machine_agricole',
            field=models.CharField(choices=[('DECORTIQUEUSE MAIS', 'DECORTIQUEUSE MAIS'), ('MOULIN CEREALES', 'MOULIN CEREALES')], max_length=100, verbose_name='TYPE MACHINE AGRICOLE'),
        ),
    ]
