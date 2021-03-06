# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 17:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0065_motodeuxroues'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotoTroisRoues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('marque_moto', models.CharField(choices=[('TVS', 'TVS')], max_length=100, verbose_name='MARQUE')),
                ('modele_moto', models.CharField(choices=[('STAR HLX', 'STAR HLX'), ('ZT', 'ZT'), ('APACHE', 'APACHE'), ('KING DELUXE', 'KING DELUXE')], max_length=100, verbose_name='MODELE')),
                ('puissance_moteur', models.CharField(choices=[('100CC', '100CC'), ('125CC', '125CC'), ('160CC', '160CC'), ('180CC', '180CC'), ('200CC', '200CC')], max_length=100, verbose_name='PUISSANCE MOTEUR')),
                ('type_demarrage', models.CharField(choices=[('DEMARRAGE AU KICK', 'DEMARRAGE AU KICK'), ('DEMARRAGE AU KICK ET DEMARRAGE  ELECTRONIQUE', 'DEMARRAGE AU KICK ET DEMARRAGE  ELECTRONIQUE')], max_length=100, verbose_name='TYPE DEMARRAGE')),
                ('etat_moto', models.CharField(choices=[('NEUF', 'NEUF'), ('OCCASION', 'OCCASION')], max_length=100, verbose_name='ETAT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
