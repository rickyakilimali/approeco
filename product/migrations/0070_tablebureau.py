# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0069_auto_20180131_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBureau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('materiau_armoire', models.CharField(choices=[('METAL', 'METAL')], max_length=20, verbose_name='MATERIAU ')),
                ('hauteur', models.CharField(choices=[('157CM', '157CM'), ('198CM', '198CM'), ('200CM', '200CM')], max_length=20, verbose_name='HAUTEUR')),
                ('longueur', models.CharField(choices=[('40CM', '40CM'), ('92CM', '92CM'), ('91CM', '91CM'), ('120CM', '120CM'), ('150CM', '150CM'), ('170CM', '170CM')], max_length=20, verbose_name='LONGUEUR')),
                ('largeur', models.CharField(choices=[('27,5CM', '27,5CM'), ('37,5CM', '37,5CM'), ('30CM', '30CM'), ('78CM', '78CM')], max_length=20, verbose_name='LARGEUR')),
                ('forme', models.CharField(choices=[('RECTANGULAIRE', 'RECTANGULAIRE')], max_length=20, verbose_name='FORME')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME'), ('USD/KG', 'USD/KG'), ('USD/AN', 'USD/AN'), ('USD/HEURE', 'USD/HEURE'), ('USD/MODULE', 'USD/MODULE'), ('USD/KG OU L', 'USD/KG OU L'), ('% DU DEVIS', '% DU DEVIS')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
