# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0236_auto_20180502_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirene',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=100, verbose_name='MARQUE'),
        ),
    ]
