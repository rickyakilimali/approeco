# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0343_reservationhoteletranger_sciecirculaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeusePerceuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('type_de_perceuse', models.CharField(choices=[('FOREUSE', 'FOREUSE'), ('FOREUSE A PERCUSSION', 'FOREUSE A PERCUSSION'), ('PERFORATEUR', 'PERFORATEUR'), ('BURINEUR', 'BURINEUR'), ('PERCEUSE A PERCUSSION', 'PERCEUSE A PERCUSSION'), ('FOREUSE PERFORATEUR BURINEUR', 'FOREUSE PERFORATEUR BURINEUR'), ('PERCEUSE DIAMANT', 'PERCEUSE DIAMANT'), ('PERCEUSE FOREUSE ANGLE', 'PERCEUSE FOREUSE ANGLE'), ('PERFORAEUR BURINEUR', 'PERFORAEUR BURINEUR'), ('FRAISEUSE A LAMELLES', 'FRAISEUSE A LAMELLES'), ('FOREUSE A COLONNE', 'FOREUSE A COLONNE'), ('FOREUSE MAGNETIQUE', 'FOREUSE MAGNETIQUE'), ('MARTEAU PERFORATEUR', 'MARTEAU PERFORATEUR'), ('FOREUSE MARTEAU PERFORATEUR', 'FOREUSE MARTEAU PERFORATEUR')], max_length=100, verbose_name='TYPE DE PERCEUSE')),
                ('marque_outillage', models.CharField(choices=[('DEWALT', 'DEWALT'), ('EINHELL', 'EINHELL')], max_length=100, verbose_name='MARQUE')),
                ('puissance_outillage', models.CharField(choices=[('550W', '550W'), ('1100W', '1100W'), ('1150W', '1150W'), ('1400W', '1400W'), ('770W', '770W'), ('650W', '650W'), ('800W', '800W'), ('1705W', '1705W'), ('350W', '350W'), ('600W', '600W'), ('750W', '750W'), ('720W', '720W'), ('1010W', '1010W'), ('1050W', '1050W'), ('900W', '900W'), ('1200W', '1200W')], max_length=100, verbose_name='PUISSANCE')),
                ('transmission', models.CharField(choices=[('1 VITESSE', '1 VITESSE'), ('2 VITESSES', '2 VITESSES'), ('REGLABLE', 'REGLABLE')], max_length=100, verbose_name='TRANSMISSION')),
                ('porte_outils', models.CharField(choices=[('13MM', '13MM'), ('SDS-PLUS', 'SDS-PLUS'), ('SDS-MAX', 'SDS-MAX'), ('1/2 POUCE - 20 UNF', '1/2 POUCE - 20 UNF'), ('MANDRIN', 'MANDRIN'), ('10MM', '10MM')], max_length=100, verbose_name='PORTE OUTILS')),
                ('tension_fonctionnement', models.CharField(choices=[('220V', '220V'), ('230V', '230V')], max_length=100, verbose_name='TENSION')),
                ('alimentation', models.CharField(choices=[('SECTEUR', 'SECTEUR')], max_length=100, verbose_name='ALIMENTATION')),
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
            name='Marteau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('type_marteau', models.CharField(choices=[('MARTEAU DE DEMOLITION', 'MARTEAU DE DEMOLITION'), ('MARTEAU PIQUEUR', 'MARTEAU PIQUEUR'), ('MARTEAU PERFORATEUR', 'MARTEAU PERFORATEUR'), ('MARTEAU ROTATIF', 'MARTEAU ROTATIF'), ('MARTEAU A PERCUSSION', 'MARTEAU A PERCUSSION')], max_length=100, verbose_name='TYPE MARTEAU PIQUEUR')),
                ('marque_outillage', models.CharField(choices=[('EINHELL', 'EINHELL'), ('DEWALT', 'DEWALT')], max_length=100, verbose_name='MARQUE')),
                ('puissance_outillage', models.CharField(choices=[('1500W', '1600W'), ('2000W', '2000W'), ('1250W', '1250W')], max_length=100, verbose_name='PUISSANCE')),
                ('poids', models.CharField(choices=[('10KG', '10KG'), ('11KG', '11KG'), ('30KG', '30KG'), ('NON APPLICABLE', 'NON APPLICABLE')], max_length=100, verbose_name='POIDS(KILOGRAMME)')),
                ('alimentation', models.CharField(choices=[('SECTEUR', 'SECTEUR'), ('BATTERIE', 'BATTERIE')], max_length=100, verbose_name='ALIMENTATION')),
                ('tension_fonctionnement', models.CharField(choices=[('220V', '220V'), ('18V', '18V')], max_length=100, verbose_name='TENSION')),
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
            name='ProtectionDeTravail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('type_protection', models.CharField(choices=[('MASQUE SOUDEUR', 'MASQUE SOUDEUR')], max_length=100, verbose_name='TYPE DE PROTECTION')),
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
            name='TouretAMeulet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_marchine', models.CharField(choices=[('EINHELL', 'EINHELL')], max_length=100, verbose_name='MARQUE')),
                ('puissance_machine', models.CharField(choices=[('400W', '400W'), ('120W', '120W'), ('150W', '150W'), ('240W', '240W')], max_length=100, verbose_name='PUISSANCE')),
                ('diametre_disque', models.CharField(choices=[('175mm', '175mm'), ('200mm', '200mm'), ('75mm', '75mm'), ('150mm', '150mm'), ('240mm', '240mm')], max_length=100, verbose_name='DIAMETRE DE DISQUE')),
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
