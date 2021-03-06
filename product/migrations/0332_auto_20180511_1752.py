# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0331_auto_20180511_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendrier',
            name='quantite',
            field=models.CharField(choices=[('1-1000', '1-1000'), ('1001-5000', '1001-5000'), ('5001-10000', '5001-10000'), ('10001-20000', '10001-20000'), ('20000<', '20000<')], max_length=50, verbose_name='QUANTITE DE CALENDRIER'),
        ),
        migrations.AlterField(
            model_name='flyer',
            name='quantite',
            field=models.CharField(choices=[('20000<', '20000<'), ('10001-20000', '10001-20000'), ('5001-10000', '5001-10000'), ('4001-5000', '4001-5000'), ('3001-4000', '3001-4000'), ('2001-3000', '2001-3000'), ('1001-2000', '1001-2000'), ('501-1000', '501-1000'), ('1-500', '1-500')], max_length=50),
        ),
    ]
