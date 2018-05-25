# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-19 11:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_auto_20180118_1155'),
        ('product', '0376_auto_20180519_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVLed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('taille_ecran', models.CharField(choices=[('19"', '19"'), ('22"', '22"'), ('80"', '80"'), ('32"', '32"'), ('40"', '40"'), ('24"', '24"'), ('43"', '43"'), ('49"', '49"'), ('55"', '55"'), ('65"', '65"')], max_length=100, verbose_name="TAILLE DE L'ECRAN")),
                ('marque', models.CharField(choices=[('SHARP', 'SHARP'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA'), ('WESTPOOL', 'WESTPOOL')], max_length=100, verbose_name='MARQUE DE LA TV')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'USD'), ('$/KM', '$/KM'), ('% DES DROITS ET TAXES', '% DES DROITS ET TAXES'), ('% DE LA VALEUR CIF', '% DE LA VALEUR CIF'), ('USD/SAC', 'USD/SAC'), ('USD/POSTE', 'USD/POSTE')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
