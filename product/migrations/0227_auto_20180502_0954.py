# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0226_auto_20180502_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproduction',
            name='nombre_minute',
            field=models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-40', '20-40'), ('40-80', '40-80')], max_length=20, verbose_name='DUREE DE LA PRODUCTION(MINUTE)'),
        ),
    ]
