# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0131_auto_20180201_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betonniere',
            name='capacite',
        ),
        migrations.RemoveField(
            model_name='betonniere',
            name='type',
        ),
        migrations.AddField(
            model_name='betonniere',
            name='capacite_betonniere',
            field=models.CharField(choices=[('180L', '180L'), ('260L', '260L'), ('350L', '350L'), ('360L', '360L'), ('500L', '500L')], default=1, max_length=100, verbose_name='CAPACITE(LITRE)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='betonniere',
            name='type_betonniere',
            field=models.CharField(choices=[('ELECTRIQUE', 'ELECTRIQUE'), ('DIESEL', 'DIESEL')], default=1, max_length=100, verbose_name='TYPE BETONNIERE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='betonniere',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='betonniere',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²')], max_length=50, verbose_name='UNITÉS'),
        ),
    ]