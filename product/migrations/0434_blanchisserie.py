# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-06 08:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0433_auto_20180605_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blanchisserie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/CHAISE', 'USD/CHAISE')], max_length=50, verbose_name='UNITÉ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
    ]
