# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-04 15:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0274_baredemine'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandeDeSignalisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('longeur', models.CharField(choices=[('500', '500')], max_length=100, verbose_name='LONGUEUR EN METTRE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET'), ('$/M2', '$/M2'), ('$/KM', '$/KM'), ('USD/COMMUNIQUE', 'USD/COMMUNIQUE'), ('USD/PCE', 'USD/PCE'), ('US/JOUR', 'US/JOUR'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
