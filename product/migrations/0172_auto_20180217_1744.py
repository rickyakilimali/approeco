# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-17 17:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0171_auto_20180217_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baguette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('taille_baguette', models.CharField(choices=[('6MM', '6MM'), ('8MM', '8MM'), ('10MM', '10MM'), ('12MM', '12MM'), ('15MM', '15MM')], max_length=100, verbose_name='TAILLE ANNEAU')),
                ('contenant', models.CharField(choices=[('PAQUET', 'PAQUET'), ('100/PAQUET', '100/PAQUET'), ('CARNET', 'CARNET'), ('BOITE', 'BOITE'), ('JEUX', 'JEUX'), ('RAME', 'RAME')], max_length=100, verbose_name='CONTENANT')),
                ('quantite_par_paquet', models.CharField(choices=[('10 BOITES', '10 BOITES'), ('500GR', '500GR')], max_length=100, verbose_name='NOMBRE DE BOITE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/M', 'USD/M'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS'), ('USD/PERSONNE/MOIS', 'USD/PERSONNE/MOIS'), ('USD/TONNE', 'USD/TONNE'), ('USD/SECONDE', 'USD/SECONDE'), ('USD/M²', 'USD/M²'), ('USD/BOITE', 'USD/BOITE'), ('USD/PAQUET', 'USD/PAQUET'), ('USD/JEU', 'USD/JEU'), ('USD/CONTENANT', 'USD/CONTENANT'), ('USD/CARNET', 'USD/CARNET')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.RenameField(
            model_name='attache',
            old_name='quantite',
            new_name='nombre_boite',
        ),
        migrations.RenameField(
            model_name='boitedarchive',
            old_name='format_boite',
            new_name='dimension_boite',
        ),
        migrations.AddField(
            model_name='attache',
            name='quantite_par_boite',
            field=models.CharField(choices=[('12', '12'), ('24', '24'), ('40', '40'), ('50', '50'), ('60', '60'), ('100', '100'), ('500', '500')], default=1, max_length=100, verbose_name='NOMBRE DE BOITE'),
            preserve_default=False,
        ),
    ]
