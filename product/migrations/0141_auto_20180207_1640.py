# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0140_auto_20180207_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacteur',
            name='puissance',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], default=1, max_length=100, verbose_name='PUISSANCE(KILOWATT)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffretjeubarre',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='contacteur',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=100, verbose_name='INTENSITE(AMPERE)'),
        ),
        migrations.AlterField(
            model_name='contacteur',
            name='nombre_phase',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100, verbose_name='NOMBRE DE PHASES'),
        ),
        migrations.AlterField(
            model_name='disjoncteur',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=50, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteur',
            name='nombre_phase',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=50, verbose_name='NOMBRE DE PHASE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurcompact',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurcontacteur',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=100, verbose_name='INTENSITE(AMPERE)'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='nombre_phase',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100, verbose_name='NOMBRE DE PHASES'),
        ),
        migrations.AlterField(
            model_name='fusible',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=50, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='interrupteurdifferentiel',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=50, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='interrupteursectionneur',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=100, verbose_name='INTENSITE(AMPERE)'),
        ),
        migrations.AlterField(
            model_name='interrupteursectionneur',
            name='nombre_phase',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100, verbose_name='NOMBRE DE PHASES'),
        ),
        migrations.AlterField(
            model_name='inverseurcoffret',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('9A', '9A'), ('1000A', '1000A'), ('115A', '115A'), ('12A', '12A'), ('150A', '150A'), ('185A', '18A'), ('225A', '225A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('80A', '80A'), ('250A', '250A'), ('32A', '32A'), ('400A', '400A'), ('64A', '64A'), ('18A', '18A'), ('10A', '10A'), ('16A', '16A'), ('1A', '1A'), ('20A', '20A'), ('2A', '2A'), ('50A', '50A'), ('6A', '6A')], max_length=20, verbose_name='INTENSITE'),
        ),
    ]