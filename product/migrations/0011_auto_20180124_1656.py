# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20180124_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='imprimante',
            name='recto_verso',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], default=1, max_length=50, verbose_name='RECTO VERSO'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imprimante',
            name='modele',
            field=models.CharField(choices=[('LASERJET PRO N20', 'LASERJET PRO N20'), ('LASERJET PRO 400', 'LASERJET PRO 400'), ('COLOR LASERJET', 'COLOR LASERJET'), ('DESKJET 2130', 'DESKJET 2130'), ('XPRESS M2020', 'XPRESS M2020'), ('OFFICE JET 4610', 'OFFICE JET 4610'), ('XPRESS M 2835', 'XPRESS M 2835'), ('XPRESS M 2835', 'XPRESS M 2835'), ('DESKJET 3630', 'DESKJET 3630'), ('M102W PRO', 'M102W PRO'), ('M277 PRO', 'M277 PRO'), ('M477 PRO', 'M477 PRO')], max_length=50, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='imprimante',
            name='multifonction',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=50, verbose_name='MULTIFONCTION'),
        ),
        migrations.AlterField(
            model_name='unite_stockage',
            name='capacite_memoire',
            field=models.CharField(choices=[('1GB', '1GB'), ('2GB', '2GB'), ('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB'), ('12GB', '12GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB'), ('320GB', '320GB'), ('500GB', '500GB'), ('1TB', '1TB'), ('2TB', '2TB'), ('3TB', '3TB'), ('4TB', '4TB')], max_length=50, verbose_name='CAPAPCITE DE STOCKAGE'),
        ),
    ]
