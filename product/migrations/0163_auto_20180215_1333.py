# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0162_auto_20180215_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbonne',
            name='quantite',
        ),
        migrations.AddField(
            model_name='carbonne',
            name='quantite_par_paquet',
            field=models.CharField(choices=[('12', '12'), ('50', '50'), ('100', '100'), ('500', '500')], default=1, max_length=100, verbose_name='QUANTITE'),
            preserve_default=False,
        ),
    ]
