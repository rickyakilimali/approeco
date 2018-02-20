# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0129_minuteurcontacteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disjoncteurdifferentiel',
            name='marque',
        ),
        migrations.RemoveField(
            model_name='disjoncteurdifferentiel',
            name='nombre_pole',
        ),
        migrations.AddField(
            model_name='disjoncteurdifferentiel',
            name='nombre_phase',
            field=models.CharField(choices=[('2P', '2P'), ('4P', '4P')], default=1, max_length=100, verbose_name='NOMBRE DE PHASES'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('40A', '40A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A')], max_length=100, verbose_name='INTENSITE(AMPERE)'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='sensibilite',
            field=models.CharField(choices=[('30MA', '30MA'), ('300MA', '300MA')], max_length=100, verbose_name='ISENSIBILITE(MILLIAMPERE)'),
        ),
    ]
