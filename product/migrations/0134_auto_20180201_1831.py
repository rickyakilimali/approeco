# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0133_auto_20180201_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compresseurair',
            name='capacite',
        ),
        migrations.RemoveField(
            model_name='compresseurair',
            name='puissance',
        ),
        migrations.AddField(
            model_name='compresseurair',
            name='capacite_compresseur',
            field=models.CharField(choices=[('100L', '100L'), ('150L', '150L'), ('200L', '200L'), ('300L', '300L'), ('1000L', '1000L')], default=1, max_length=100, verbose_name='CAPACITE COMPRESSEUR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compresseurair',
            name='puissance_compresseur',
            field=models.CharField(choices=[('2.0HP', '2.0HP'), ('3.0HP', '3.0HP'), ('4.0HP', '4.0HP'), ('5.5HP', '5.5HP'), ('6.5HP', '6.5HP'), ('7.5HP', '7.5HP'), ('10HP', '10HP')], default=1, max_length=100, verbose_name='PUISSANCE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compresseur',
            name='capacite_compresseur',
            field=models.CharField(choices=[('100L', '100L'), ('150L', '150L'), ('200L', '200L'), ('300L', '300L'), ('1000L', '1000L')], max_length=20, verbose_name='CAPACITE'),
        ),
        migrations.AlterField(
            model_name='compresseur',
            name='puissance_compresseur',
            field=models.CharField(choices=[('2.0HP', '2.0HP'), ('3.0HP', '3.0HP'), ('4.0HP', '4.0HP'), ('5.5HP', '5.5HP'), ('6.5HP', '6.5HP'), ('7.5HP', '7.5HP'), ('10HP', '10HP')], max_length=20, verbose_name='PUISSANCE'),
        ),
        migrations.AlterField(
            model_name='compresseurair',
            name='debit',
            field=models.CharField(choices=[('250L/MIN', '250L/MIN'), ('360L/MIN', '360L/MIN'), ('900L/MIN', '900L/MIN'), ('1000L/MIN', '1000L/MIN'), ('1050L/MIN', '1050L/MIN')], max_length=100, verbose_name='DEBIT(LITRE/MIN)'),
        ),
        migrations.AlterField(
            model_name='compresseurair',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX'),
        ),
        migrations.AlterField(
            model_name='compresseurair',
            name='units',
            field=models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²')], max_length=50, verbose_name='UNITÉS'),
        ),
    ]