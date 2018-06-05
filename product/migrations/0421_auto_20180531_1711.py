# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-31 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0420_auto_20180531_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancecuisine',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='balancecuisine',
            name='poids',
            field=models.CharField(choices=[('8 KG', '8 KG'), ('30 KG', '30 KG'), ('100 KG', '100 KG'), ('150 KG', '150 KG')], max_length=100, verbose_name='POIDS '),
        ),
        migrations.AlterField(
            model_name='comptoire',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='couvercleoval',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='fourpizza',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='machinecreme',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='plateaunourriture',
            name='format',
            field=models.CharField(choices=[('20 CM', '20 CM'), ('22 CM', '22 CM'), ('24 CM', '24 CM'), ('26 CM"', '26 CM'), ('28 CM', '28 CM'), ('30 CM', '30 CM'), ('40 CM', '40 CM')], max_length=100, verbose_name='FORMAT'),
        ),
        migrations.AlterField(
            model_name='plateaunourriture',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='poele',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='tablier',
            name='couleur',
            field=models.CharField(choices=[('BLANC/NOIR', 'BLANC/NOIR')], max_length=100, verbose_name='COULEUR'),
        ),
        migrations.AlterField(
            model_name='tassemesure',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='tassemesure',
            name='volume',
            field=models.CharField(choices=[('0,5 L', '0,5 L'), ('1 L', '1 L')], max_length=100, verbose_name='VOLUME'),
        ),
        migrations.AlterField(
            model_name='vitrineboisson',
            name='marque',
            field=models.CharField(choices=[('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE'),
        ),
    ]