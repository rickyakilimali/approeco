# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-23 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0389_baffleportable_batteriecartemere_batteriecmos_cablereseau_camera_casqueavecmicro_casquemusique_casqu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baffleportable',
            name='category',
        ),
        migrations.RemoveField(
            model_name='baffleportable',
            name='vendeur',
        ),
        migrations.DeleteModel(
            name='BafflePortable',
        ),
    ]