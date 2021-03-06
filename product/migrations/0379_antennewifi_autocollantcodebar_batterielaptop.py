# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-19 11:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0378_adapteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntenneWifi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_antenne', models.CharField(choices=[('TP-LINK', 'TP-LINK'), ('UBIQUITI', 'UBIQUITI')], max_length=100, verbose_name='MARQUE ANTENNE')),
                ('modele_antenne', models.CharField(choices=[('TL-ANT2415D', 'TL-ANT2415D'), ('TL-ANT2424B', 'TL-ANT2424B'), ('M5 NBE-M5-1', 'M5 NBE-M5-1')], max_length=100, verbose_name='MODELE ANTENNE ')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='AutocollantCodeBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('dimension_autocollant', models.CharField(choices=[('102x76 MM', '102x76 MM'), ('50x30 MM', '50x30 MM'), ('60x30 MM', '60x30 MM')], max_length=100, verbose_name='DIMENSION AUTOCOLLANT')),
                ('quantite_autocollant', models.CharField(choices=[('1500', '1500'), ('5000', '5000'), ('4000', '4000')], max_length=100, verbose_name='QUANTITE AUTOCOLLANT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='BatterieLaptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_laptop', models.CharField(choices=[('HP', 'HP')], max_length=100, verbose_name='MARQUE LAPTOP')),
                ('modeles_laptop', models.CharField(choices=[('530/510', '530/510'), ('6720/6730', '6720/6730'), ('DV4/DV5/DV6', 'DV4/DV5/DV6'), ('G62', 'G62'), ('NX6120', 'NX6120'), ('PROBOOK 4520/620', 'PROBOOK 4520/620')], max_length=100, verbose_name='MODELE LAPTOP')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
