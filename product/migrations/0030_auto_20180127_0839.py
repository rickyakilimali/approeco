# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-27 08:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0029_auto_20180127_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD', 'US$'), ('EUROS', 'EUROS'), ('USD/JOUR', 'USD/JOUR'), ('USD/PAGE', 'USD/PAGE'), ('USD/M2', 'USD/M2'), ('USD/MOIS', 'USD/MOIS'), ('USD/PIECE', 'USD/PIECE'), ('USD', 'USD'), ('USD/KG', 'USD/KG'), ('USD/PERSONNE', 'USD/PERSONNE'), ('USD/GARDIEN/MOIS', 'USD/GARDIEN/MOIS'), ('USD/LITRE', 'USD/LITRE'), ('USD/SPLIT', 'USD/SPLIT'), ('%', '%'), ('% DU SALAIRE', '% DU SALAIRE'), ('% DU 1ER SALAIRE', '% DU 1ER SALAIRE'), ('% DES FONDS TRANSPORTES', '% DES FONDS TRANSPORTES'), ('USD/PERSONNE/JOUR', 'USD/PERSONNE/JOUR'), ('USD/THEME', 'USD/THEME')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.AlterField(
            model_name='ecriturescenario',
            name='nombre_minute',
            field=models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-40', '20-40'), ('40-80', '40-80')], max_length=20, verbose_name='DUREE DU SCENARIO'),
        ),
        migrations.AlterField(
            model_name='postproduction',
            name='nombre_minute',
            field=models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-40', '20-40'), ('40-80', '40-80')], max_length=20, verbose_name='DUREE DE LA PRODUCTION'),
        ),
        migrations.AlterField(
            model_name='productiontournage',
            name='nombre_minute',
            field=models.CharField(choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-40', '20-40'), ('40-80', '40-80')], max_length=20, verbose_name='DUREE DU TOURNAGE'),
        ),
    ]