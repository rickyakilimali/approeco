# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0235_auto_20180502_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxde10kg',
            name='category',
        ),
        migrations.RemoveField(
            model_name='boxde10kg',
            name='vendeur',
        ),
        migrations.DeleteModel(
            name='Boxde10kg',
        ),
    ]