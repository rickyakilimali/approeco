# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 16:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180118_1155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0352_auto_20180516_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amarante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('BOTTE', 'BOTTE')], max_length=100, verbose_name='CONTENANT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Arachide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('SAC DE 50KG', 'SAC DE 50KG')], max_length=100, verbose_name='CONTENANT')),
                ('caracteristique', models.CharField(choices=[('DECORTIQUE', 'DECORTIQUE')], max_length=100, verbose_name='CONTENANT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Gingembre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('SACHET DE 1,5Kg', 'SACHET DE 1,5Kg')], max_length=100, verbose_name='CONTENANT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Mais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('SAC DE 60KG', 'SAC DE 60KG'), ('SAC DE 100KG', 'SAC DE 100KG')], max_length=100, verbose_name='CONTENANT')),
                ('variete', models.CharField(choices=[('JAUNE', 'JAUNE')], max_length=100, verbose_name='VARIETE DU MAIS')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Manioc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('SAC DE 100KG', 'SAC DE 100KG')], max_length=100, verbose_name='CONTENANT')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Pondu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('SACHET DE 250G', 'SACHET DE 250G'), ('SACHET DE 500G', 'SACHET DE 500G'), ('SACHET DE 1KG', 'SACHET DE 1KG')], max_length=100, verbose_name='CONTENANT')),
                ('type_legume', models.CharField(choices=[('PONDU', 'PONDU')], max_length=100, verbose_name='TYPE DE LEGUME')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.CreateModel(
            name='Semoule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='PRODUIT')),
                ('is_active', models.BooleanField()),
                ('contenant', models.CharField(choices=[('SAC DE 10KG', 'SAC DE 10KG'), ('SAC DE 25KG', 'SAC DE 25KG'), ('SAC DE 1KG', 'SAC DE 1KG')], max_length=100, verbose_name='CONTENANT')),
                ('produit_de_base', models.CharField(choices=[('MAIS', 'MAIS'), ('SOJA', 'SOJA')], max_length=100, verbose_name='PRODUIT DE BASE')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRIX')),
                ('units', models.CharField(choices=[('USD/KG', 'USD/KG')], max_length=50, verbose_name='UNITÉS')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prix'],
            },
        ),
        migrations.RemoveField(
            model_name='farine',
            name='base',
        ),
        migrations.AddField(
            model_name='farine',
            name='contenant',
            field=models.CharField(choices=[('SAC DE 5KG', 'SAC DE 5KG'), ('SAC DE 10KG', 'SAC DE 10KG'), ('SAC DE 20KG', 'SAC DE 20KG')], default=1, max_length=100, verbose_name='CONTENANT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farine',
            name='produit_de_base',
            field=models.CharField(choices=[('MANIOC', 'MANIOC')], default=1, max_length=100, verbose_name='PRODUIT DE BASE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='legume',
            name='type_legume',
            field=models.CharField(choices=[('PONDU', 'PONDU')], max_length=50, verbose_name='TYPE LEGUME'),
        ),
        migrations.AlterField(
            model_name='riz',
            name='variete',
            field=models.CharField(choices=[('JAUNE', 'JAUNE')], max_length=100, verbose_name='VARIETE'),
        ),
        migrations.AlterField(
            model_name='semence',
            name='variete',
            field=models.CharField(blank=True, choices=[('JAUNE', 'JAUNE')], max_length=100, null=True, verbose_name='VARIETE'),
        ),
    ]