# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-17 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0181_auto_20180417_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piecederechangeembrayage',
            old_name='pieces_rechange_embrayage',
            new_name='type_piece_embrayage',
        ),
    ]
