# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Papeterie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=50, verbose_name='NOM DE LA CATEGORIE')),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.CharField(max_length=50, verbose_name='SLUG')),
            ],
        ),
    ]
