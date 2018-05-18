# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0231_auto_20180502_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boitederivation',
            name='dimension',
            field=models.CharField(choices=[('105X105X55MM', '105X105X55MM'), ('175X150X80MM', '175X150X80MM'), ('225X175X100MM', '225X175X100MM'), ('275X225X120MM', '275X225X120MM'), ('65X65X45MM', '65X65X45MM'), ('105X105X42MM', '105X105X42MM'), ('130X130X30MM', '130X130X30'), ('160X100X45MM', '160X100X45MM'), ('220X160X45MM', '220X160X45MM'), ('60X60X25MM', '60X60X25MM'), ('80X80X30MM', '80X80X30MM'), ('80X80MM', '80X80MM'), ('100X100MM', '100X100MM'), ('150X150MM', '150X150MM'), ('200X150MM', '200X150MM')], max_length=20, verbose_name='DIMENSION(MILLIMETRES)'),
        ),
        migrations.AlterField(
            model_name='ciseau',
            name='taille',
            field=models.CharField(choices=[('22CM', '22CM')], max_length=100, verbose_name='TAILLE(CENTIMETRE)'),
        ),
    ]