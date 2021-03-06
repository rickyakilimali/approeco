# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-18 14:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0187_entretienetreparationdevehicule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionBatiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('qualite_du_terrain', models.CharField(choices=[('SABLONEUX', 'SABLONEUX'), ('ARGILEUX', 'ARGILEUX'), ('MARECAGEUX', 'MARECAGEUX'), ('ALCALINO-TERREUX', 'ALCALINO-TERREUX')], max_length=20, verbose_name='QUALITE DU TERRAIN')),
                ('usage_du_batiment', models.CharField(choices=[('ENTREPOT', 'ENTREPOT'), ('COMMERCIAL ORDINAIRE', 'COMMERCIAL ORDINAIRE'), ('COMMERCIAL LUXUEUX', 'COMMERCIAL LUXUEUX'), ('RESIDENTIEL ORDINAIRE', 'RESIDENTIEL ORDINAIRE'), ('RESIDENTIEL LUXUEUX', 'RESIDENTIEL LUXUEUX')], max_length=20, verbose_name='USAGE DU BATIMENT')),
                ('nombre_d_etages', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=20, verbose_name="NOMBRE D'ETAGE")),
                ('nombre_de_pieces', models.CharField(choices=[('1 -10', '1 -10'), ('11 - 20', '11 - 20'), ('21 - 30', '21 - 30'), ('31 - 40', '31 - 40'), ('41 - 50', '41 - 50'), ('51 - 60', '51 - 60'), ('61 - 70', '61 - 70'), ('71 - 80', '71 - 80'), ('81 - 90', '81 - 90'), ('91 -100', '91 -100'), ('1 -10', '1 -10')], max_length=20, verbose_name='NOMBRE DE PIECES')),
                ('type_de_terrain', models.CharField(choices=[('TERRAIN PLAT', 'TERRAIN PLAT'), ('TERRAIN INCLINÉ', 'TERRAIN INCLINÉ')], max_length=20, verbose_name='TYPE DE TERRAIN')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.AlterField(
            model_name='assainissement',
            name='type_assainissement',
            field=models.CharField(choices=[('DESINSECTISATION', 'DESINSECTISATION'), ('DERATISATION', 'DERATISATION'), ('NETTOYAGE', 'NETTOYAGE'), ('NETTOYAGE APRES CHANTIER', 'NETTOYAGE APRES CHANTIER'), ('DESINFECTION', 'DESINFECTION')], max_length=100, verbose_name="TYPE D'ASSAINISSEMENT"),
        ),
    ]
