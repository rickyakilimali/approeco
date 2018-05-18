# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-15 10:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0337_auto_20180515_1053'),
    ]

    operations = [

        migrations.AlterField(
            model_name='demenagement',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='depliant',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='desagrafeuse',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='detecteurincendie',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='detecteurintrusion',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='diable',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='diamantcoupecarreaux',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='diffusionspotpublicitaire',
            name='units',
            field=models.CharField(choices=[('USD/SECONDE', 'USD/SECONDE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='disjoncteur',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='disjoncteurcompact',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='disjoncteurcontacteur',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='disjoncteurmoteur',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='disquedescie',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='ecritoire',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='ecriturescenario',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='elastiques',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='enregistreurcamerasurveillance',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='enseignelumineuse',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='entreposage',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='entretienetreparationdevehicule',
            name='units',
            field=models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50),
        ),
        migrations.AlterField(
            model_name='enveloppe',
            name='units',
            field=models.CharField(choices=[('USD/PAQUET', 'USD/PAQUET')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='envoicolisinternational',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='envoicolisinternationalplus70kg',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='envoicolisnational0a20kgs',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='envoicolisnational100kgsetplus',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='envoicolisnational20kgsa99kgs',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='envoicourrierinternational',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='equerre',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecederechangeelectrique',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecederechangeembrayage',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecederechangefreinage',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecederechangerefroidissement',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecederechangetransmission',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecerechangemoteur',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='piecerevisionmoteur',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pile',
            name='units',
            field=models.CharField(choices=[('USD/PAQUET', 'USD/PAQUET')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='pinceau',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='pins',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='placement',
            name='units',
            field=models.CharField(choices=[('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='plafonnierled',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='plantoir',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='pneu',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='pointacces',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='poisson',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pompeeau',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pompeforage',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pompehydrophore',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pompeimmergee',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='porc',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50),
        ),
        migrations.AlterField(
            model_name='portecle',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='porteclef',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='postit',
            name='units',
            field=models.CharField(choices=[('USD/CARNET', 'USD/CARNET')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='postproduction',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='xstand',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50),
        ),
    ]
