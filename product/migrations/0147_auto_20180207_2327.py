# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0146_auto_20180207_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupeelectrogene',
            name='marque',
            field=models.CharField(blank=True, choices=[('EINHELL', 'EINHELL'), ('EMERGY', 'EMERGY'), ('DEWALT', 'DEWALT'), ('IMO ITALIA', 'IMO ITALIA'), ('MAKITA', 'MAKITA'), ('STIHL', 'STIHL'), ('ROBEN', 'ROBEN'), ('SACO', 'SACO'), ('TALA', 'TALA'), ('DEUTZ', 'DEUTZ'), ('PERKINS', 'PERKINS')], max_length=20, null=True, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='groupeelectrogene',
            name='puissance_groupe',
            field=models.CharField(choices=[('720W', '720W'), ('3100W', '3100W'), ('3500W', '3500W'), ('4875W', '4875W'), ('5000W', '5000W'), ('5500W', '5500W'), ('7500W', '7500W'), ('10000W', '10000W'), ('1KVA', '1KVA'), ('10KVA', '10KVA'), ('2,5KVA', '2,5KVA'), ('5,5KVA', '5,5KVA'), ('3,5KVA', '3,5KVA'), ('5KVA', '5KVA'), ('2KVA', '2KVA'), ('3KVA', '3KVA'), ('6,5KVA', '6,5KVA'), ('7,5KVA', '7,5KVA'), ('12,5KVA', '12,5KVA'), ('15KVA', '15KVA'), ('20KVA', '20KVA'), ('38KVA', '38KVA'), ('27KVA', '27KVA'), ('225KVA', '225KVA'), ('30KVA', '30KVA'), ('40KVA', '40KVA'), ('60KVA', '60KVA'), ('50KVA', '50KVA'), ('100KVA', '100KVA')], max_length=20, verbose_name='PUISSANCE'),
        ),
    ]
