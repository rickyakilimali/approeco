# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-16 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0179_produitpharmaceutique_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitpharmaceutique',
            name='produit',
            field=models.CharField(choices=[('BLUMOX', 'BLUMOX'), ('CEBRAN 500', 'CEBRAN 500'), ('EKON-DT', 'EKON-DT'), ('MEFTAL 500', 'MEFTAL 500'), ('MEFTAL FORTE', 'MEFTAL FORTE'), ('MEFTAL FORTE CREME', 'MEFTAL FORTE CREME'), ('MEFTAL P', 'MEFTAL P'), ('MEFTAL P SUSP', 'MEFTAL P SUSP'), ('MEFTAL SPAS', 'MEFTAL SPAS'), ('MEFTAL SPAS DROPS', 'MEFTAL SPAS DROPS'), ('MEFTAL SPAS INJ', 'MEFTAL SPAS INJ'), ('OMEPREN 20', 'OMEPREN 20'), ('SONADERM', 'SONADERM'), ('TUSQ-DX CES', 'TUSQ-DX CES'), ('TUSQ-DX SIROP', 'TUSQ-DX SIROP'), ('TUSQ-X SIROP', 'TUSQ-X SIROP'), ('WOMIBAN', 'WOMIBAN')], max_length=50, verbose_name='PRODUIT'),
        ),
    ]