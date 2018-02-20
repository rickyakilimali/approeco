# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0134_auto_20180201_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('puissance_palan', models.CharField(choices=[('1.6KW', '1.6KW'), ('3KW', '3KW')], max_length=100, verbose_name='PUISSANCE PALAN')),
                ('longueur', models.CharField(choices=[('10M', '10M')], max_length=100, verbose_name='LONGUEUR')),
                ('poids_max', models.CharField(choices=[('3T', '3T')], max_length=100, verbose_name='POIDS MAX(TONNE)')),
                ('type_palan', models.CharField(choices=[('ELECTRIQUE', 'ELECTRIQUE')], max_length=100, verbose_name='TYPE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.AlterField(
            model_name='enseignelumineuse',
            name='longueur',
            field=models.CharField(choices=[('10M', '10M')], max_length=20, verbose_name='LONGUEUR'),
        ),
        migrations.AlterField(
            model_name='rallonge',
            name='longueur',
            field=models.CharField(choices=[('10M', '10M')], max_length=20, verbose_name='RALLONGE'),
        ),
    ]
