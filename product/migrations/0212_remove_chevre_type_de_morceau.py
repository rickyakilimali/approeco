# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0211_auto_20180425_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chevre',
            name='type_de_morceau',
        ),
    ]
