# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 09:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0049_auto_20180130_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationVehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('type_vehicule', models.CharField(choices=[('VOITURE', 'VOITURE'), ('JEEP', 'JEEP'), ('MINIBUS', 'MINIBUS')], max_length=20, verbose_name='TYPE DE VEHICULE')),
                ('marque', models.CharField(choices=[('TOYOTA YARIS', 'TOYOTA YARIS'), ('TOYOTA CAMRY ', 'TOYOTA CAMRY '), ('TOYOTA RAV4', 'TOYOTA RAV4'), ('TOYOTA PRADO', 'TOYOTA PRADO'), ('TOYOTA LAND CRUISER', 'TOYOTA LAND CRUISER'), ('TOYOTA HIACE', 'TOYOTA HIACE'), ('TOYOTA HILUX DOUBLE CABINE', 'TOYOTA HILUX DOUBLE CABINE'), ('NISSAN', 'NISSAN'), ('ZX AUTO', 'ZX AUTO'), ('ZOTYE', 'ZOTYE')], max_length=20, verbose_name='MARQUE DU VEHICULE')),
                ('model', models.CharField(choices=[('PATROL V8-SE', 'PATROL V8-SE'), ('PATROL PICK UP SIMPLE CABINE', 'PATROL PICK UP SIMPLE CABINE'), ('PATROL 10 PLACE ', 'PATROL 10 PLACE '), ('NAVARA PICK UP ', 'NAVARA PICK UP '), ('HARDBODY', 'HARDBODY'), ('URVAN', 'URVAN'), ('CIVILIAN', 'CIVILIAN'), ('QUASHKA', 'QUASHKA'), ('JUKE', 'JUKE'), ('PATHFINDER', 'PATHFINDER'), ('SENTRA', 'SENTRA'), ('ALMERA', 'ALMERA'), ('SUNNY', 'SUNNY'), ('X TRAIL 2X4', 'X TRAIL 2X4'), ('X TRAIL 4X4', 'X TRAIL 4X4'), ('GRANDTIGER PICK UP', 'GRANDTIGER PICK UP'), ('TERRALORD LUXURY', 'TERRALORD LUXURY'), ('Z100', 'Z100'), ('GRAND TIGER SUV', 'GRAND TIGER SUV')], max_length=20, verbose_name='MODELE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
