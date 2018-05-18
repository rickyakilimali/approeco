# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0223_auto_20180502_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachet',
            name='dimension_cachet',
            field=models.CharField(choices=[('30MMx30MM', '30MMx30MM'), ('30MMx38MM', '30MMx38MM'), ('38MMx38MM', '38MMx38MM'), ('40MMx40MM', '40MMx40MM'), ('45MMx45MM', '45MMx45MM'), ('50MMx50MM', '50MMx50MM')], max_length=50, verbose_name='DIMENSION DE CACHET(MILLIMETRE)'),
        ),
    ]