# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-19 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0195_auto_20180419_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poisson',
            name='category',
        ),
        migrations.RemoveField(
            model_name='poisson',
            name='vendeur',
        ),
        migrations.DeleteModel(
            name='Poisson',
        ),
    ]