# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-30 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemprice',
            name='price2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Prix moins de 250 employés'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix moins de 250 employés'),
        ),
    ]