# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-19 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0380_auto_20180519_1205'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pondu',
            new_name='LegumeSeche',
        ),
        migrations.AlterField(
            model_name='arachide',
            name='caracteristique',
            field=models.CharField(choices=[('DECORTIQUE', 'DECORTIQUE')], max_length=100, verbose_name='CARACTERISTIQUE'),
        ),
    ]
