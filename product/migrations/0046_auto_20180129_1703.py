# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-29 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0045_numerisationdonnees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartouche',
            name='marque_cartouche',
            field=models.CharField(choices=[('HP', 'HP'), ('SAMSUNG', 'SAMSUNG'), ('CANON', 'CANON'), ('EPSON', 'EPSON'), ('BROTHER', 'BROTHER'), ('KATUN', 'KATUN')], max_length=50, verbose_name='MARQUE DE CARTOUCHE'),
        ),
        migrations.AlterField(
            model_name='cartouche',
            name='numero_cartouche',
            field=models.CharField(choices=[('61', '61'), ('121', '121'), ('122', '122'), ('17A', '17A'), ('201A', '201A'), ('401A', '401A'), ('563', '563'), ('57', '57'), ('73', '73'), ('21', '21'), ('22', '22'), ('29', '29'), ('49', '49'), ('60', '60'), ('63', '63'), ('920', '920'), ('932', '932'), ('933', '933'), ('951', '951'), ('C-EXV14', 'C-EXV14'), ('C-EXV40', 'C-EXV40'), ('CEXV 33', 'CEXV 33'), ('CF 350', 'CF 350'), ('CF 351', 'CF 351'), ('GPR08', 'GPR08'), ('GPR18', 'GPR18'), ('GPR22', 'GPR22'), ('IR 2202-CEXV 42', 'IR 2202-CEXV 42'), ('NPG 32', 'NPG 32'), ('TN 1000', 'TN 1000'), ('TN 2025', 'TN 2025'), ('TN 2060', 'TN 2060'), ('TN 2130', 'TN 2130'), ('TN 2260', 'TN 2260'), ('TN 2280', 'TN 2280'), ('TN 240BK', 'TN 240BK'), ('TN 240C', 'TN 240C'), ('TN 240M', 'TN 240M'), ('TN 240Y', 'TN 240Y'), ('TN 261BK', 'TN 261BK'), ('TN 261C', 'TN 261C'), ('TN 261M', 'TN 261M'), ('TN 261Y', 'TN 261Y'), ('TN 3185', 'TN 3185'), ('TN 3250', 'TN 3250'), ('TN 3290', 'TN 3290'), ('TN 3320', 'TN 3320'), ('05A', '05A'), ('104 S', '104 S'), ('122', '122'), ('123', '123'), ('123A', '123A'), ('126 A', '126 A'), ('128 A', '128 A'), ('129', '129'), ('12A', '12A'), ('131 A', '131 A'), ('136', '136'), ('140', '140'), ('141', '141'), ('15', '15'), ('178', '178'), ('201 A', '201 A'), ('21', '21'), ('28', '28'), ('300', '300'), ('301', '301'), ('304 A', '304 A'), ('305 A', '305 A'), ('336', '336'), ('35A', '35A'), ('364', '364'), ('36A', '36A'), ('42 A', '42 A'), ('49A', '49A'), ('55 A', '55 A'), ('63A', '63A'), ('650', '650'), ('716', '716'), ('725', '725'), ('728', '728'), ('731', '731'), ('78A', '78A'), ('80 A', '80 A'), ('83 A', '83 A'), ('83A', '83A'), ('88', '88'), ('920 XL', '920 XL'), ('920', '920'), ('933 XL', '933 XL'), ('94', '94'), ('940', '940'), ('TN-260', 'TN-260'), ('104S', '104S'), ('128A', '128A'), ('80A', '80A'), ('126A', '126A'), ('305A', '305A'), ('131A', '131A')], max_length=50, verbose_name='NUMERO DE CARTOUCHE'),
        ),
        migrations.AlterField(
            model_name='logiciel',
            name='licence',
            field=models.CharField(choices=[('1 UTILISATEUR', '1 UTILISATEUR'), ('10 UTILISATEURS', '10 UTILISATEURS'), ('3 UTILISATEURS', '3 UTILISATEURS')], max_length=50, verbose_name='LICENCE'),
        ),
        migrations.AlterField(
            model_name='logiciel',
            name='type_logiciel',
            field=models.CharField(choices=[('ANTIVIRUS', 'ANTIVIRUS'), ('INTERNET SECURITY MULTIDEVICE', 'INTERNET SECURITY MULTIDEVICE'), ('ANTIVIRUS+PAREFEU', 'ANTIVIRUS+PAREFEU')], max_length=50, verbose_name='TYPE DE LOGICIEL'),
        ),
    ]
