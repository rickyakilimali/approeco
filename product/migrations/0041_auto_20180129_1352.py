# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-29 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_installationlogicielserveur'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cahiercharges',
            options={'ordering': ['prix']},
        ),
        migrations.AlterModelOptions(
            name='helpdesk',
            options={'ordering': ['prix']},
        ),
        migrations.AlterModelOptions(
            name='installationlogicielserveur',
            options={'ordering': ['prix']},
        ),
    ]