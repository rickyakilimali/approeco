# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0145_interrupteursectionneur_marque'),
    ]

    operations = [
        migrations.AddField(
            model_name='minuteurcontacteur',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('TELEMECA', 'TELEMECA')], default=1, max_length=50, verbose_name='MARQUE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appareildemesure',
            name='tension',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('415V', '415V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], max_length=20, verbose_name='TENSION'),
        ),
        migrations.AlterField(
            model_name='appareilmesure',
            name='tension',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('415V', '415V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], max_length=20, verbose_name='TENSION'),
        ),
        migrations.AlterField(
            model_name='contacteur',
            name='puissance',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('415V', '415V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], max_length=100, verbose_name='PUISSANCE(KILOWATT)'),
        ),
        migrations.AlterField(
            model_name='contacteur',
            name='tension',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('415V', '415V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], max_length=100, verbose_name='TENSION(VOLT)'),
        ),
        migrations.AlterField(
            model_name='interrupteursectionneur',
            name='tension',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('415V', '415V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], max_length=100, verbose_name='TENSION(VOLT)'),
        ),
        migrations.AlterField(
            model_name='plafonnierled',
            name='tension',
            field=models.CharField(choices=[('110V', '110V'), ('230V', '230V'), ('24V', '24V'), ('24VCC', '24VCC'), ('380V', '380V'), ('400V', '400V'), ('415V', '415V'), ('48V', '48V'), ('220V', '220V'), ('250V', '250V'), ('500V', '500V'), ('1000V', '1000V')], max_length=20, verbose_name='TENSION'),
        ),
    ]
