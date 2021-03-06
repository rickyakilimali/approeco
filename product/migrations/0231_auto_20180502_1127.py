# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0230_auto_20180502_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boitederivation',
            name='dimension',
            field=models.CharField(choices=[('105X105X55', '105X105X55'), ('175X150X80', '175X150X80'), ('225X175X100', '225X175X100'), ('275X225X120', '275X225X120'), ('65X65X45', '65X65X45'), ('105X105X42', '105X105X42'), ('130X130X30', '130X130X30'), ('160X100X45', '160X100X45'), ('220X160X45', '220X160X45'), ('60X60X25', '60X60X25'), ('80X80X30', '80X80X30'), ('80X80MM', '80X80MM'), ('100X100MM', '100X100MM'), ('150X150MM', '150X150MM'), ('200X150MM', '200X150MM')], max_length=20, verbose_name='DIMENSION(MILLIMETRES)'),
        ),
    ]
