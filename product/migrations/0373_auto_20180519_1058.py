# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-19 10:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0372_destructeurpapier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Congelateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque', models.CharField(choices=[('ATLAS', 'ATLAS'), ('DEFY', 'DEFY'), ('SAMSUNG', 'SAMSUNG'), ('WHIRLPOOL', 'WHIRLPOOL'), ('XPER', 'XPER')], max_length=100, verbose_name='MARQUE')),
                ('Volume', models.CharField(choices=[('150L', '150L'), ('250L', '250L'), ('350L', '350L'), ('300L', '300L'), ('550L', '550L'), ('260L', '260L'), ('400L', '400L'), ('280L', '280L'), ('320L', '320L'), ('480L', '480L'), ('185L', '185L'), ('324L', '324L'), ('130L', '130L'), ('465L', '465L'), ('500L', '500L'), ('600L', '600L'), ('110L', '110L'), ('120L', '120L'), ('170L', '170L'), ('200L', '200L'), ('450L', '450L')], max_length=100, verbose_name='VOLUME EN LITRE')),
                ('type_congelateur', models.CharField(choices=[('STANDARD', 'STANDARD'), ('DEBOUT', 'DEBOUT'), ('AVEC COOL PACK', 'AVEC COOL PACK'), ('AVEC VITRE', 'AVEC VITRE')], max_length=100, verbose_name='TYPE DE CONGELATEUR')),
                ('alimentation', models.CharField(choices=[('PANNEAUX SOLAIRES', 'PANNEAUX SOLAIRES'), ('PETROL', 'PETROL'), ('SECTEUR', 'SECTEUR')], max_length=100, verbose_name='ALIMENTATION')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.AlterField(
            model_name='bouilloire',
            name='volume',
            field=models.CharField(choices=[('1,7 L', '1,7 L'), ('1,6 L', '1,6 L'), ('2 L', '2 L')], max_length=100, verbose_name='VOLUME'),
        ),
        migrations.AlterField(
            model_name='chauffeeau',
            name='volume',
            field=models.CharField(choices=[('100 L', '100 L'), ('80 L', '80 L'), ('50 L', '50 L'), ('30 L', '30 L')], max_length=100, verbose_name='VOLUME EN LITRE'),
        ),
        migrations.AlterField(
            model_name='destructeurpapier',
            name='Volume_panier_dechet',
            field=models.CharField(choices=[('23L', '23L'), ('16L', '16L'), ('31L', '31L'), ('13L', '13L'), ('3,5L', '3,5L')], max_length=100, verbose_name='VOLUME PANIER DECHIQUETEUSE'),
        ),
        migrations.AlterField(
            model_name='destructeurpapier',
            name='capacite_papier',
            field=models.CharField(choices=[('12 PAPIERS', '12 PAPIERS'), ('17 PAPIERS', '17 PAPIERS'), ('2 PAPIERS', '2 PAPIERS'), ('8 PAPIERS', '8 PAPIERS')], max_length=100, verbose_name='CAPACITE PAPIER'),
        ),
        migrations.AlterField(
            model_name='destructeurpapier',
            name='destruction_carte_credit',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=100, verbose_name='AVEC DESRTUCTEUR CARTE DE CREDIT'),
        ),
        migrations.AlterField(
            model_name='destructeurpapier',
            name='destruction_cd',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=100, verbose_name='AVEC DESRTUCTEUR CD'),
        ),
    ]