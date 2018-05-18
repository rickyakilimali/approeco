# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-10 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0289_auto_20180510_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonnementjournal',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='accessoireshydrophore',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=20),
        ),
        migrations.AlterField(
            model_name='accueilaeroport',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='adresseippublique',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='affichagelogosurecran',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='affiche',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50),
        ),
        migrations.AlterField(
            model_name='agrafe',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='agrafeuse',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='aiguilleavibrerlebeton',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='albumcartedevisite',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='ampoule',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='ampouleelectrique',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ampoulesolaire',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='anneauplastique',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='appareildemesure',
            name='unite_prix',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=20),
        ),
        migrations.AlterField(
            model_name='appareildemesure',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50),
        ),
        migrations.AlterField(
            model_name='appareilmesure',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='armoire',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50),
        ),
        migrations.AlterField(
            model_name='arracheclou',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='aspirateur',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='assainissement',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='assistancecomptable',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='assistancefiscale',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='assurancevoyage',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='attache',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),
        migrations.AlterField(
            model_name='attachecableaclouer',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC')], max_length=50, verbose_name='UNITÉS'),
        ),



    ]