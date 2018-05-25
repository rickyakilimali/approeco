# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-18 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0360_auto_20180518_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poubelleuac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('type_poubelle', models.CharField(choices=[('POUBELLE', 'POUBELLE')], max_length=100, verbose_name='TYPE DE POUBELLE')),
                ('matiere', models.CharField(choices=[('PLASTIQUE', 'PLASTIQUE'), ('INOX', 'INOX')], max_length=100, verbose_name='MATIERE')),
                ('volume', models.CharField(choices=[('12L', '12L'), ('30L', '30L'), ('8L', '8L'), ('20L', '20L'), ('6L', '6L')], max_length=100, verbose_name='VOLUME (LITRE)')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
