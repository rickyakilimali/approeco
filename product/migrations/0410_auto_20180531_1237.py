# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-31 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0409_auto_20180531_1206'),
    ]

    operations = [


        migrations.AlterField(
            model_name='pompeforage',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='pompeforage',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='pompehydrophore',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='pompehydrophore',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='pompeimmergee',
            name='debit_pompe',
            field=models.CharField(choices=[('300 L/H', '300 L/H'), ('600 L/H', '600 L/H'), ('1200 L/H', '1200 L/H'), ('1500 L/H', '1500 L/H'), ('1800 L/H', '1800 L/H'), ('3000 L/H', '3000 L/H'), ('3600 L/H', '3600 L/H'), ('3800 L/H', '3800 L/H'), ('4020 L/H', '4020 L/H'), ('4600 L/H', '4600 L/H'), ('6800 L/H', '6800 L/H'), ('10020 L/H', '10020 L/H'), ('10500 L/H', '10500 L/H'), ('15700 L/H', '15700 L/H'), ('17500 L/H', '17500 L/H'), ('18000 L/H', '18000 L/H'), ('23000 L/H', '23000 L/H'), ('66000 L/H', '66000 L/H')], max_length=100, verbose_name='DEBIT POMPE EN LITRE/HEURE)'),
        ),
        migrations.AlterField(
            model_name='pompeimmergee',
            name='puissance_pompe',
            field=models.CharField(choices=[('5,5 HP', '5,5 HP'), ('6,5 HP', '6,5 HP'), ('4,0 HP', '4,0 HP'), ('2 HP', '2 HP'), ('3 HP', '3 HP'), ('4 HP', '4 HP'), ('10HP', '10HP'), ('7,5 HP', '7,5H P'), ('0,5 HP', '0,5 HP'), ('0.75 HP', '0.75 HP'), ('1 HP', '1 HP'), ('1,5 HP', '1,5 HP'), ('15 HP', '15 HP'), ('20 HP', '20 HP'), ('25 HP', '25 HP'), ('30 HP', '30 HP'), ('40 HP', '40 HP')], max_length=100, verbose_name='PUISSANCE POMPE EN CHEVAUX'),
        ),
        migrations.AlterField(
            model_name='prisewifi',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='processeur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='protectionsurtensions',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='raboteuse',
            name='type_raboteuse',
            field=models.CharField(choices=[('RABOTEUSE ELECTRIQUE', 'RABOTEUSE ELECTRIQUE'), ('RABOT AVEC TABLE', 'RABOT AVEC TABLE'), ('RABOT DEGAUCHISSEUSE', 'RABOT DEGAUCHISSEUSE'), ('RABOT', 'RABOT')], max_length=100, verbose_name='TYPE'),
        ),
        migrations.AlterField(
            model_name='rack',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='reductionpvc',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='reductionpvc',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='repartiteuradsl',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='repartiteurhdmi',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='retransmissiondirect',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rivet',
            name='dimension',
            field=models.CharField(choices=[('4x40 MM', '4x40 MM'), ('4x25 MM', '4x25 MM')], max_length=100, verbose_name='DIMENSION'),
        ),
        migrations.AlterField(
            model_name='rivet',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='riz',
            name='type_riz',
            field=models.CharField(blank=True, choices=[('DECORTIQUE', 'DECORTIQUE'), ('NON DECORTIQUE', 'NON DECORTIQUE')], max_length=100, null=True, verbose_name='TYPE DE RIZ'),
        ),
        migrations.AlterField(
            model_name='rollup',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='rollup',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='roseareliure',
            name='units',
            field=models.CharField(choices=[('USD/PAQUET', 'USD/PAQUET')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rouleaubandeaponcer',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rouleaucablecoaxial',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rouleauflexuble',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='routeur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rubanimpression',
            name='longueur',
            field=models.CharField(choices=[('LQ350', 'LQ350'), ('LX350', 'LX350')], max_length=100, verbose_name='LONGUEUR'),
        ),
        migrations.AlterField(
            model_name='rubanimpression',
            name='modele',
            field=models.CharField(choices=[('P-TOUCH', 'P-TOUCH')], max_length=100, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='rubanimpression',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rubanpapier',
            name='marque',
            field=models.CharField(choices=[('BROTHER', 'BROTHER')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='rubanpapier',
            name='modele',
            field=models.CharField(choices=[('P-TOUCH', 'P-TOUCH')], max_length=100, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='rubanpapier',
            name='numero',
            field=models.CharField(choices=[('DK-11202', 'DK-11202'), ('DK-11207', 'DK-11207'), ('DK-22205', 'DK-22205'), ('DK-22210', 'DK-22210')], max_length=100, verbose_name='LONGUEUR'),
        ),
        migrations.AlterField(
            model_name='rubanpapier',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='rubanpouretiqueteuse',
            name='marque',
            field=models.CharField(choices=[('BROTHER', 'BROTHER')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='rubanpouretiqueteuse',
            name='modele',
            field=models.CharField(choices=[('P-TOUCH TZE-FX621', 'P-TOUCH TZE-FX621'), ('P-TOUCH TZE-FX631', 'P-TOUCH TZE-FX631')], max_length=100, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='rubanpouretiqueteuse',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sac',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sacados',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sachet',
            name='quantite',
            field=models.CharField(choices=[('1-100', '1-100'), ('101-500', '101-500'), ('501-1000', '501-1000'), ('1001-2000', '1001-2000'), ('2001-5000', '2001-5000'), ('5001-10000', '5001-10000'), ('10001<', '10001<')], max_length=50, verbose_name='QUANTITE'),
        ),
        migrations.AlterField(
            model_name='sciecirculaire',
            name='diametre_lame',
            field=models.CharField(choices=[('235mm', '235mm'), ('350mm', '350mm'), ('165mm', '165mm'), ('160mm', '160mm'), ('190mm', '190mm'), ('210mm', '210mm'), ('250mm', '250mm'), ('300mm', '300mm')], max_length=100, verbose_name='DIAMETRE DE LAME'),
        ),
        migrations.AlterField(
            model_name='sciecirculaire',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sciecloche',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sciesauteuse',
            name='puissance',
            field=models.CharField(choices=[('1750W', '1750W'), ('2200W', '2200W'), ('1200W', '1200W'), ('1230W', '1230W'), ('1400W', '1400W'), ('1500W', '1500W'), ('2000W', '2000W'), ('1800W', '1800W'), ('2800W', '2800W'), ('1600W', '1600W')], max_length=100, verbose_name='PUISSANCE'),
        ),
        migrations.AlterField(
            model_name='sciesauteuse',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='scotch',
            name='longueur',
            field=models.CharField(choices=[('30CM', '30CM'), ('50CM', '50CM'), ('3M', '3M'), ('23M', '23M'), ('100M', '100M'), ('250M', '250M')], max_length=100, verbose_name='LONGUEUR EN METRE'),
        ),
        migrations.AlterField(
            model_name='scotch',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sechemain',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='sechemain',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='selfpourprojecteur',
            name='puissance',
            field=models.CharField(choices=[('400W', '400W')], max_length=100, verbose_name='PUISSANCE'),
        ),
        migrations.AlterField(
            model_name='selfpourprojecteur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='semence',
            name='units',
            field=models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='serveur',
            name='capacite_ram_max',
            field=models.CharField(choices=[('1GB', '1GB'), ('2GB', '2GB'), ('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB'), ('12GB', '12GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB')], max_length=50, verbose_name='MEMOIRE RAM MAXIMUM'),
        ),
        migrations.AlterField(
            model_name='serveur',
            name='modele_serveur',
            field=models.CharField(choices=[('POWEREDGE', 'POWEREDGE'), ('PROLIANT', 'PROLIANT')], max_length=50, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='serveur',
            name='type_serveur',
            field=models.CharField(choices=[('TOUR', 'TOUR'), ('RACKABLE', 'RACKABLE')], max_length=50, verbose_name='TYPE DE SERVEUR'),
        ),
        migrations.AlterField(
            model_name='serveur',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='signataire',
            name='nombre_compartiments',
            field=models.CharField(choices=[('10', '10'), ('15', '15'), ('20', '20'), ('25', '25'), ('30', '30')], max_length=100, verbose_name='NOMBRE DE COMPARTIMENTS'),
        ),
        migrations.AlterField(
            model_name='signataire',
            name='units',
            field=models.CharField(choices=[('USD/PIECE', 'USD/PIECE'), ('USD/PCE', 'USD/PCE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='silicone',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='siphon',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='siphon',
            name='type_sanitaire',
            field=models.CharField(choices=[('BAIGNOIRE', 'BAIGNOIRE'), ('EVIER', 'EVIER'), ('LAVABO', 'LAVABO'), ('SOL', 'SOL')], max_length=20, verbose_name="TYPE D'INSTALLATION SANITAIRE"),
        ),
        migrations.AlterField(
            model_name='siphon',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=20, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='sirene',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),
        migrations.AlterField(
            model_name='socket',
            name='units',
            field=models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITE'),
        ),

    ]
