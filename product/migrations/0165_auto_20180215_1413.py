# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0164_auto_20180215_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classeur',
            name='type_classeur',
        ),
        migrations.AddField(
            model_name='classeur',
            name='format_classeur',
            field=models.CharField(choices=[('PETIT FORMAT', 'PETIT FORMAT'), ('GRAND FORMAT', 'GRAND FORMAT')], default=1, max_length=100, verbose_name='FORMAT'),
            preserve_default=False,
        ),
    ]