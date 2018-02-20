# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0156_telephonebureau'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImprimanteABadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('marque_imprimante_badge', models.CharField(choices=[('EVOLIS', 'EVOLIS')], max_length=100, verbose_name='MARQUE IMPRIMANTE')),
                ('technologe_impression_badge', models.CharField(choices=[('TRANSFERT THERMIQUE', 'TRANSFERT THERMIQUE'), ('RETRANSFERT', 'RETRANSFERT')], max_length=100, verbose_name='TECHNOLOGIE IMPRESSION')),
                ('faces_imprimes', models.CharField(choices=[('SIMPLE FACE', 'SIMPLE FACE'), ('DOUBLE FACE', 'DOUBLE FACE')], max_length=100, verbose_name='FACES IMPRIMES')),
                ('vitesse_impression', models.CharField(choices=[('144 CARTES/HEURE', '144 CARTES/HEURE'), ('325 CARTES/HEURE', '325 CARTES/HEURE'), ('500 CARTES/HEURE', '500 CARTES/HEURE'), ('850 CARTES/HEURE', '850 CARTES/HEURE')], max_length=100, verbose_name="VITESSE D'IMPRESSION")),
                ('option_encodage', models.CharField(choices=[('NON', 'NON'), ('MAGNETIQUE+CARTE A PUCE AVEC CONTACT+CARTE A PUCE SANS CONTACT', 'MAGNETIQUE+CARTE A PUCE AVEC CONTACT+CARTE A PUCE SANS CONTACT')], max_length=100, verbose_name="OPTION D'ENCODAGE")),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.AlterField(
            model_name='boitederivation',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=20, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='coffretelectrique',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=20, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='contacteur',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='controleaccesetpointage',
            name='marque_equipement',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='detecteurintrusion',
            name='marque_detecteur',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=100, verbose_name='MARQUE DETECTEUR'),
        ),
        migrations.AlterField(
            model_name='disjoncteur',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurdifferentiel',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='disjoncteurmoteur',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='fusible',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='interrupteurdifferentiel',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='interrupteursectionneur',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='minuteurcontacteur',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='sirene',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=100, verbose_name='PUISSANCE TONDEUSE'),
        ),
        migrations.AlterField(
            model_name='telephonebureau',
            name='marque',
            field=models.CharField(choices=[('ABB', 'ABB'), ('GENERAL ELECTRIC', 'GENERAL ELECTRIC'), ('SCHNEIDER', 'SCHNEIDER'), ('SUPREMA', 'SUPREMA'), ('PROLINE', 'PROLINE'), ('TELEMECA', 'TELEMECA'), ('NEC', 'NEC')], max_length=100, verbose_name='MARQUE TELEPHONE'),
        ),
    ]