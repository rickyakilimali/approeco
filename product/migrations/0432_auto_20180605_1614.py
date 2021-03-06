# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-05 16:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0431_auto_20180605_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcasseurNoixDePalme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('puissance', models.CharField(choices=[('15KW', '15KW'), ('20KW', '20KW')], max_length=100, verbose_name='PUISSANCE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='ConstructionDeCharpenteMetallique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Malaxeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('puissance', models.CharField(choices=[('5KW', '5KW'), ('7,5KW', '7,5KW')], max_length=100, verbose_name='PUISSANCE')),
                ('materiaux', models.CharField(choices=[('INOX', 'INOX'), ('ACIER', 'ACIER')], max_length=100, verbose_name='MATERIAUX')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='MenuiserieMetallique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Moulin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('puissance', models.CharField(choices=[('7KW', '7KW'), ('10KW', '10KW')], max_length=100, verbose_name='PUISSANCE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='PateDArachide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('conditionnement_arrachide', models.CharField(choices=[('DOUZAINE DE BOITE DE 250G', 'DOUZAINE DE BOITE DE 250G')], max_length=100, verbose_name='CONDITIONNEMENT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='PimentDeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('forme_piment', models.CharField(choices=[('POUDRE', 'POUDRE')], max_length=100, verbose_name='FORME')),
                ('type_piment', models.CharField(choices=[('AROMATISÉ DEGRAISSEUR', 'AROMATISÉ DEGRAISSEUR'), ('AROMATISÉ STANDARD', 'AROMATISÉ STANDARD'), ('AROMATISÉ STABILISATEUR DE SUCRE (BANKURU)', 'AROMATISÉ STABILISATEUR DE SUCRE (BANKURU)')], max_length=100, verbose_name='TYPE')),
                ('conditionnement_piment', models.CharField(choices=[('CARTON DE 24PIECE DE 50G', 'CARTON DE 24PIECE DE 50G')], max_length=100, verbose_name='CONDITIONNEMENT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='SechageEtEmballageDeLegumes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('poids_avant_sechage', models.CharField(choices=[('10-100KG', '10-100KG'), ('100KG<', '100KG<')], max_length=100, verbose_name='POIDS AVANT SECHAGE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='SechoirElectrique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('volume', models.CharField(choices=[('2M3', '2M3')], max_length=100, verbose_name='VOLUME')),
                ('puissance', models.CharField(choices=[('12KW', '12KW')], max_length=100, verbose_name='PUISSANCE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.RemoveField(
            model_name='carnet',
            name='category',
        ),
        migrations.RemoveField(
            model_name='carnet',
            name='vendeur',
        ),
        migrations.AlterField(
            model_name='accueilaeroport',
            name='units',
            field=models.CharField(choices=[('USD/PERSONNE', 'USD/PERSONNE')], max_length=50, verbose_name='UNITÉ'),
        ),
        migrations.AlterField(
            model_name='affiche',
            name='format_papier',
            field=models.CharField(choices=[('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4')], max_length=50, verbose_name='FORMAT'),
        ),
        migrations.AlterField(
            model_name='assurancevoyage',
            name='tranche_age',
            field=models.CharField(choices=[('0-54 ANS', '0-54 ANS'), ('55-64 ANS', '55-64 ANS'), ('65-69 ANS', '65-69 ANS')], max_length=20, verbose_name="TRANCHE D'AGE"),
        ),
        migrations.AlterField(
            model_name='attache',
            name='contenant',
            field=models.CharField(choices=[('PAQUET', 'PAQUET')], max_length=100, verbose_name='CONTENANT'),
        ),
        migrations.AlterField(
            model_name='attache',
            name='nombre_boite',
            field=models.CharField(choices=[('10 BOITES', '10 BOITES'), ('500GR', '500GR')], max_length=100, verbose_name='NOMBRE DE BOITE'),
        ),
        migrations.AlterField(
            model_name='depliant',
            name='format_papier',
            field=models.CharField(choices=[('A4', 'A4')], max_length=50, verbose_name='FORMAT'),
        ),
        migrations.AlterField(
            model_name='flyer',
            name='format_papier',
            field=models.CharField(choices=[('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6')], max_length=50, verbose_name='FORMAT'),
        ),
        migrations.AlterField(
            model_name='impressiontasse',
            name='quantite',
            field=models.CharField(choices=[('1-100', '1-100'), ('101-200', '101-200'), ('201-500', '201-500'), ('501-1000', '501-1000'), ('1001-10000', '1001-10000'), ('10000<', '10000<')], max_length=100, verbose_name='SUPPORT'),
        ),
        migrations.AlterField(
            model_name='insertionpublicitaire',
            name='dimension',
            field=models.CharField(choices=[('1 PAGE COULEUR', '1 PAGE COULEUR'), ('1 PAGE NB', '1 PAGE NB'), ('1/2 PAGE COULEUR', '1/2 PAGE COULEUR'), ('1/2 PAGE NB', '1/2 PAGE NB'), ('1/4 PAGE NB', '1/4 PAGE NB'), ('LA UNE', 'LA UNE'), ('PUBLI-REPORTAGE', 'PUBLI-REPORTAGE'), ('PUBLICATION', 'PUBLICATION')], max_length=100, verbose_name='DIMENSION INSERTION'),
        ),
        migrations.AlterField(
            model_name='locationdepot',
            name='commune',
            field=models.CharField(choices=[('LIMETE', 'LIMETE')], max_length=100, verbose_name='COMMUNE'),
        ),
        migrations.AlterField(
            model_name='postproduction',
            name='nombre_minute',
            field=models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-40', '20-40'), ('40-80', '40-80')], max_length=20, verbose_name='DUREE DE LA PRODUCTION (PAR MINUTE)'),
        ),
        migrations.AlterField(
            model_name='productiontournage',
            name='nombre_minute',
            field=models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-40', '20-40'), ('40-80', '40-80')], max_length=20, verbose_name='DUREE DU TOURNAGE (PAR MINUTE)'),
        ),
        migrations.AlterField(
            model_name='rollup',
            name='dimension',
            field=models.CharField(choices=[('85X200CM', '85X200CM')], max_length=50, verbose_name='DIMENSION'),
        ),
        migrations.AlterField(
            model_name='tshirtblanc',
            name='quantite',
            field=models.CharField(choices=[('1-100', '1-100'), ('101-200', '101-200'), ('201-500', '201-500'), ('501-1000', '501-1000'), ('1001-10000', '1001-10000'), ('10000<', '10000<')], max_length=50, verbose_name='QUANTITE'),
        ),
        migrations.DeleteModel(
            name='Carnet',
        ),
    ]
