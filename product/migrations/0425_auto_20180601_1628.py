# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-01 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0424_auto_20180601_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amarante',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='arachide',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='armoire',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='armoire',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='boeuf',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='boeuf',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='bouillie',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='bouturemanioc',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='brique',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='bureau',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='caissondebureau',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='carreau',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='chaisebureau',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='chaisesalleattente',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='chevre',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='chevre',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='constructionbatiment',
            name='units',
            field=models.CharField(choices=[('USD/M2', 'USD/M2')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='constructionroute',
            name='units',
            field=models.CharField(choices=[('USD/KM', 'USD/KM')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='consultancedecoration',
            name='units',
            field=models.CharField(choices=[('USD/HEURE', 'USD/HEURE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='cossettemanioc',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='cossettemanioc',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='decorationamenagement',
            name='units',
            field=models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='decorationsurface',
            name='units',
            field=models.CharField(choices=[('USD/M2', 'USD/M2')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='entretienetreparationdevehicule',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='entretienetreparationdevehicule',
            name='units',
            field=models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='etagere',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='farine',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='gingembre',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='huile',
            name='units',
            field=models.CharField(choices=[('USD/LITRE', 'USD/LITRE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='installationelectrique',
            name='units',
            field=models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='legume',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='legume',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='legumeseche',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='locationcamion',
            name='units',
            field=models.CharField(choices=[('USD/JOUR', 'USD/JOUR')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='locationdepot',
            name='units',
            field=models.CharField(choices=[('USD/MOIS', 'USD/MOIS')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='locationremorquematadi',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='locationstand',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='mais',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='manioc',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='mielpur',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='mielpur',
            name='units',
            field=models.CharField(choices=[('USD/LITRE', 'USD/LITRE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='missioncontrolechantier',
            name='units',
            field=models.CharField(choices=[('USD/MOIS', 'USD/MOIS')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='moellon',
            name='units',
            field=models.CharField(choices=[('USD/TONNE', 'USD/TONNE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='peinture',
            name='units',
            field=models.CharField(choices=[('USD/KG OU LITRE', 'USD/KG OU LITRE'), ('USD/KG OU L', 'USD/KG OU L')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='peinturespeciale',
            name='units',
            field=models.CharField(choices=[('USD/KG OU LITRE', 'USD/KG OU LITRE'), ('USD/KG OU L', 'USD/KG OU L')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangecarrosserie',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangecarrosserie',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangedirectionsuspension',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangedirectionsuspension',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangeelectrique',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangeelectrique',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangeembrayage',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangeembrayage',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangefreinage',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangefreinage',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangerefroidissement',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangerefroidissement',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecederechangetransmission',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecederechangetransmission',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecerechangemoteur',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecerechangemoteur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='piecerevisionmoteur',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='piecerevisionmoteur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='poisson',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='poisson',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='porc',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='porc',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='poubelleuac',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='poulet',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='poulet',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='reboisement',
            name='units',
            field=models.CharField(choices=[('USD/M2', 'USD/M2')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='riz',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='riz',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='semence',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='semoule',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='tableau',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='tableordinateur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='tablereunion',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='tourteau',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='travauxpeinture',
            name='units',
            field=models.CharField(choices=[('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='triplex',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='vase',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITE'),
        ),
    ]