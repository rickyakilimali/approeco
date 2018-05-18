# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0347_burineur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boulonneuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_outillage', models.CharField(choices=[('DEWALT', 'DEWALT')], max_length=100, verbose_name='MARQUE')),
                ('puissance_outillage', models.CharField(choices=[('710W', '710W')], max_length=100, verbose_name='TRANSMISSION')),
                ('transmission', models.CharField(choices=[('1 VITESSE', '1 VITESSE')], max_length=100, verbose_name='ALIMENTATION')),
                ('porte_outils', models.CharField(choices=[('EMMANCHEMENT CARRÉ 1/2 POUCE', 'EMMANCHEMENT CARRÉ 1/2 POUCE'), ('710W', '710W')], max_length=100, verbose_name="CONSOMMATION D'AIR")),
                ('tension_fonctionnement', models.CharField(choices=[('220V', '220V')], max_length=100, verbose_name="PRESSION D'AIR")),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Rainureuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_marchine', models.CharField(choices=[('EINHELL', 'EINHELL')], max_length=100, verbose_name='MARQUE')),
                ('puissance_machine', models.CharField(choices=[('1320W', '1320W'), ('350W', '350W')], max_length=100, verbose_name='TRANSMISSION')),
                ('largeur_de_coupe', models.CharField(choices=[('26MM', '26MM')], max_length=100, verbose_name='ALIMENTATION')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='TourABois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_marchine', models.CharField(choices=[('EINHELL', 'EINHELL')], max_length=100, verbose_name='MARQUE')),
                ('puissance_machine', models.CharField(choices=[('1320W', '1320W'), ('350W', '350W')], max_length=100, verbose_name='TRANSMISSION')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
