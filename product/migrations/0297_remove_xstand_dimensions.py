# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-10 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0296_auto_20180510_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xstand',
            name='dimensions',
        ),
    ]