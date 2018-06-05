# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0425_auto_20180601_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaisebureau',
            name='type_chaise',
            field=models.CharField(choices=[('CHAISE DE BUREAU', 'CHAISE DE BUREAU'), ('CHAISE DE DIRECTION', 'CHAISE DE DIRECTION'), ('CHAISE VISITEUR', 'CHAISE VISITEUR')], max_length=20, verbose_name='TYPE DE CHAISE'),
        ),
        migrations.AlterField(
            model_name='coffretjeubarre',
            name='intensite',
            field=models.CharField(choices=[('63A', '63A'), ('250A', '250A'), ('400A', '400A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='contacteur',
            name='intensite',
            field=models.CharField(choices=[('9A', '9A'), ('12A', '12A'), ('18A', '18A'), ('25A', '25A'), ('100A', '100A'), ('115A', '115A'), ('150A', '150A'), ('185A', '185A'), ('225A', '225A'), ('1000A', '1000A')], max_length=100, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='depliant',
            name='quantite',
            field=models.CharField(choices=[('20001<', '20001<'), ('10001-20000', '10001-20000'), ('5001-10000', '5001-10000'), ('4001-5000', '4001-5000'), ('3001-4000', '3001-4000'), ('2001-3000', '2001-3000'), ('1001-2000', '1001-2000'), ('501-1000', '501-1000'), ('1-500', '1-500')], max_length=50, verbose_name='QUANTITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteur',
            name='intensite',
            field=models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('6A', '6A'), ('10A', '10A'), ('16A', '16A'), ('20A', '20A'), ('25A', '25A'), ('32A', '32A'), ('40A', '40A'), ('50A', '50A'), ('63A', '63A')], max_length=50, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurcompact',
            name='intensite',
            field=models.CharField(choices=[('64A', '64A'), ('100A', '100A'), ('125A', '125A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurcontacteur',
            name='intensite',
            field=models.CharField(choices=[('18A', '18A'), ('25A', '25A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A')], max_length=100, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='enregistreurcamerasurveillance',
            name='nombre_canaux',
            field=models.CharField(choices=[('16', '16')], max_length=20, verbose_name='NOMBRE DE CANAUX'),
        ),
        migrations.AlterField(
            model_name='escortefonds',
            name='units',
            field=models.CharField(choices=[('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES')], max_length=50, verbose_name='UNITÉ'),
        ),
        migrations.AlterField(
            model_name='fusible',
            name='intensite',
            field=models.CharField(choices=[('16A', '16A'), ('63A', '63A'), ('80A', '80A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A'), ('250A', '250A')], max_length=50, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='interrupteurdifferentiel',
            name='intensite',
            field=models.CharField(choices=[('25A', '25A'), ('40A', '40A'), ('63A', '63A'), ('80A', '80A')], max_length=50, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='interrupteurdifferentiel',
            name='nombre_phase',
            field=models.CharField(choices=[('2', '2'), ('4', '4')], max_length=50, verbose_name='NOMBRE DE PHASE'),
        ),
        migrations.AlterField(
            model_name='interrupteursectionneur',
            name='intensite',
            field=models.CharField(choices=[('40A', '40A'), ('63A', '63A'), ('125A', '125A')], max_length=100, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='inverseurcoffret',
            name='intensite',
            field=models.CharField(choices=[('63A', '63A'), ('100A', '100A'), ('125A', '125A'), ('160A', '160A'), ('200A', '200A')], max_length=20, verbose_name='INTENSITE'),
        ),
        migrations.AlterField(
            model_name='poisson',
            name='type_de_poisson',
            field=models.CharField(choices=[('MUNGUSU', 'MUNGUSU'), ('MOJOMBO', 'MOJOMBO'), ('MINZANDA', 'MINZANDA'), ('MGOMGO', 'MGOMGO'), ('CAPITAINE', 'CAPITAINE'), ('MBOTO', 'MBOTO'), ('MINZANDA', 'MINZANDA'), ('NGOLO', 'NGOLO'), ('SOLE MOYENNE', 'SOLE MOYENNE'), ('GRANDE SOLE', 'GRANDE SOLE'), ('CAPITAINE MOYEN', 'CAPITAINE MOYEN'), ('GRAND CAPITAINE', 'GRAND CAPITAINE'), ('FILET DE CAPITAINE', 'FILET DE CAPITAINE'), ('PERCHE', 'PERCHE'), ('FILET DE PERCHE', 'FILET DE PERCHE'), ('MEROU', 'MEROU'), ('RAIE (MAZIBA)', 'RAIE (MAZIBA)'), ('AILE DE RAIE', 'AILE DE RAIE'), ('ROUGET', 'ROUGET'), ('SAINT PIERRE', 'SAINT PIERRE'), ('BARRACUDA', 'BARRACUDA'), ('COSSA MOYEN MOANDA', 'COSSA MOYEN MOANDA'), ('COSSA MOYEN POINTE NOIRE', 'COSSA MOYEN POINTE NOIRE'), ('COSSA ROYALE POINTE NOIRE', 'COSSA ROYALE POINTE NOIRE'), ('PETITE LANGOUSTE MOANDA', 'PETITE LANGOUSTE MOANDA'), ('LANGOUSTE MOYENNE POINTE NOIRE', 'LANGOUSTE MOYENNE POINTE NOIRE'), ('GRANDE LANGOUSTE POINTE NOIRE', 'GRANDE LANGOUSTE POINTE NOIRE'), ('PIEUVRE POINTE NOIR', 'PIEUVRE POINTE NOIR'), ('CRABE', 'CRABE'), ('CALAMARD', 'CALAMARD'), ('SECHE', 'SECHE'), ('COSSA DECORTIQUE', 'COSSA DECORTIQUE'), ('MORUE', 'MORUE')], max_length=50, verbose_name='TYPE DE POISSON'),
        ),
        migrations.AlterField(
            model_name='semence',
            name='poids',
            field=models.CharField(choices=[('1KG', '1KG'), ('5KG', '5KG'), ('10KG', '10KG'), ('25KG', '25KG')], max_length=100, verbose_name='CONTENANT'),
        ),
    ]
