# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-10 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0299_auto_20180510_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pausecafe',
            old_name='sur_place',
            new_name='lieu',
        ),
    ]
