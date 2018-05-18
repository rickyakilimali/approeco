# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-16 14:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0177_auto_20180416_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitPharmaceutique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('classe_therapeutique', models.CharField(choices=[('ANTIHELMINTHIQUES', 'ANTIHELMINTHIQUES'), ('INFECTIOLOGIE', 'INFECTIOLOGIE'), ('ANTI-INFLAMMATOIRE ET ANTALGIQUES', 'ANTI-INFLAMMATOIRE ET ANTALGIQUES'), ('ANTISPASMODIQUE ET ANTIFLATULENCE', 'ANTISPASMODIQUE ET ANTIFLATULENCE'), ('GASTRO-ENTEROLOGIE', 'GASTRO-ENTEROLOGIE'), ('DERMATOLOGIE', 'DERMATOLOGIE'), ('BRONCHOPNEUMONIE', 'BRONCHOPNEUMONIE')], max_length=50, verbose_name='CLASSE THERAPEUTIQUE')),
                ('presentation', models.CharField(choices=[('COMPRIME', 'COMPRIME'), ('CREME ANTI-INFLAMMATOIRE', 'CREME ANTI-INFLAMMATOIRE'), ('SUSPENSION LIQUIDE', 'SUSPENSION LIQUIDE'), ('GOUTTES', 'GOUTTES'), ('AMPOULE', 'AMPOULE'), ('GELULES', 'GELULES'), ('CREME DERMIQUE', 'CREME DERMIQUE'), ('SIROP', 'SIROP')], max_length=50, verbose_name='PRESENTATON')),
                ('dosage', models.CharField(choices=[('250MG', '250MG'), ('500MG', '500MG'), ('10MG', '10MG'), ('50G', '50G'), ('100MG', '100MG'), ('60ML', '60ML'), ('10ML', '10ML'), ('10G', '10G'), ('5MG/2MG/8MG', '5MG/2MG/8MG'), ('100ML', '100ML'), ('400MG', '400MG')], max_length=50, verbose_name='DOSAGE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
