# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0022_auto_20180126_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouillie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('composition_bouillie', models.CharField(choices=[('SOYA, BLE, MAIS, RIZ ET HUILE VEGETALE', 'SOYA, BLE, MAIS, RIZ ET HUILE VEGETALE')], max_length=100, verbose_name='COMPOSITION BOUILLIE')),
                ('qualite_bouillie', models.CharField(choices=[('BIO', 'BIO')], max_length=100, verbose_name='QUALITE BOUILLIE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR')], max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
