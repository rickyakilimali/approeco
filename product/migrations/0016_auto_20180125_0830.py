# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_coursanglais_langue_cours'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoursAnglais',
            new_name='CoursLangue',
        ),
    ]