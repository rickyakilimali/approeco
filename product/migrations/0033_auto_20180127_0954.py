# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-27 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_auto_20180127_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photocopieuse',
            name='marque_photocopieuse',
        ),
        migrations.AddField(
            model_name='photocopieuse',
            name='marque_imprimante',
            field=models.CharField(choices=[('HP', 'HP'), ('CANON', 'CANON'), ('EPSON', 'EPSON'), ('SAMSUNG', 'SAMSUNG'), ('BROTHER', 'BROTHER')], default=1, max_length=50, verbose_name='MARQUE PHOTOCOPIEUSE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='insertionpublicitaire',
            name='dimension',
            field=models.CharField(choices=[('1 PAGE COULEUR', '1 PAGE COULEUR'), ('1 PAGE NB', '1 PAGE NB'), ('1/2 PAGE COULEUR', '1/2 PAGE COULEUR'), ('1/2 PAGE NB', '1/2 PAGE NB'), ('1/4 PAGE NB', '1/4 PAGE NB'), ('LA UNE', 'LA UNE'), ('PUBLI REPORTAGE (PAGE)', 'PUBLI REPORTAGE (PAGE)'), ('PUBLICATION DOCUMENT (PAGE)', 'PUBLICATION DOCUMENT (PAGE)')], max_length=100, verbose_name='DIMENSION INSERTION'),
        ),
    ]
