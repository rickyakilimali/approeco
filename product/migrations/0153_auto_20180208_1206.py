# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0152_auto_20180208_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detecteurintrusion',
            name='adressable',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=100, verbose_name='ADRESSABLE'),
        ),
        migrations.AlterField(
            model_name='detecteurintrusion',
            name='marque_detecteur',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA')], max_length=100, verbose_name='MARQUE DETECTEUR'),
        ),
        migrations.AlterField(
            model_name='detecteurintrusion',
            name='type_detecteur',
            field=models.CharField(choices=[('DETECTEUR DE MOUVEMENT', 'DETECTEUR DE MOUVEMENT'), ('DETECTEUR DE CHOC', 'DETECTEUR DE CHOC'), ('DETECTEUR DE FUMEE', 'DETECTEUR DE FUMEE'), ('DETECTEUR DE CHALEUR', 'DETECTEUR DE CHALEUR'), ('DETECTEUR MANUEL', 'DETECTEUR MANUEL')], max_length=100, verbose_name='TYPE DE DETECTEUR'),
        ),
    ]
