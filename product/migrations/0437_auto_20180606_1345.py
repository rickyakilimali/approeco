# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-06 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0436_auto_20180606_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baguette',
            name='taille_baguette',
            field=models.CharField(choices=[('6MM', '6MM'), ('8MM', '8MM'), ('10MM', '10MM'), ('12MM', '12MM'), ('15MM', '15MM')], max_length=100, verbose_name='TAILLE BAGUETTE'),
        ),
    ]