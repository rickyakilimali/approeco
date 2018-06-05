# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-31 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0418_auto_20180531_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartouche',
            name='couleur_cartouche',
            field=models.CharField(choices=[('COULEUR', 'COULEUR'), ('CYAN', 'CYAN'), ('JAUNE', 'JAUNE'), ('MAGENTA', 'MAGENTA'), ('NOIR', 'NOIR')], max_length=50, verbose_name='COULEUR DE LA CARTOUCHE'),
        ),
        migrations.AlterField(
            model_name='cartouche',
            name='marque_cartouche',
            field=models.CharField(choices=[('BROTHER', 'BROTHER'), ('CANON', 'CANON'), ('EPSON', 'EPSON'), ('HP', 'HP'), ('KATUN', 'KATUN'), ('SAMSUNG', 'SAMSUNG')], max_length=50, verbose_name='MARQUE DE LA CARTOUCHE'),
        ),
        migrations.AlterField(
            model_name='cartouche',
            name='numero_cartouche',
            field=models.CharField(choices=[('05A', '05A'), ('104 S', '104 S'), ('104S', '104S'), ('121', '121'), ('122', '122'), ('123', '123'), ('123A', '123A'), ('126 A', '126 A'), ('126A', '126A'), ('128 A', '128 A'), ('128A', '128A'), ('129', '129'), ('12A', '12A'), ('131 A', '131 A'), ('131A', '131A'), ('136', '136'), ('140', '140'), ('141', '141'), ('15', '15'), ('178', '178'), ('17A', '17A'), ('201 A', '201 A'), ('201A', '201A'), ('21', '21'), ('22', '22'), ('28', '28'), ('29', '29'), ('300', '300'), ('301', '301'), ('304 A', '304 A'), ('305 A', '305 A'), ('305A', '305A'), ('336', '336'), ('35A', '35A'), ('364', '364'), ('36A', '36A'), ('401A', '401A'), ('42 A', '42 A'), ('49', '49'), ('49A', '49A'), ('55 A', '55 A'), ('563', '563'), ('57', '57'), ('60', '60'), ('61', '61'), ('63', '63'), ('63A', '63A'), ('650', '650'), ('716', '716'), ('725', '725'), ('728', '728'), ('73', '73'), ('731', '731'), ('78A', '78A'), ('80 A', '80 A'), ('80A', '80A'), ('83 A', '83 A'), ('83A', '83A'), ('88', '88'), ('920 XL', '920 XL'), ('920', '920'), ('920', '920'), ('932', '932'), ('933 XL', '933 XL'), ('933', '933'), ('94', '94'), ('940', '940'), ('951', '951'), ('CEXV 33', 'CEXV 33'), ('C-EXV14', 'C-EXV14'), ('C-EXV40', 'C-EXV40'), ('CF 350', 'CF 350'), ('CF 351', 'CF 351'), ('GPR08', 'GPR08'), ('GPR18', 'GPR18'), ('GPR22', 'GPR22'), ('IR 2202-CEXV 42', 'IR 2202-CEXV 42'), ('NPG 32', 'NPG 32'), ('TN 1000', 'TN 1000'), ('TN 2025', 'TN 2025'), ('TN 2060', 'TN 2060'), ('TN 2130', 'TN 2130'), ('TN 2260', 'TN 2260'), ('TN 2280', 'TN 2280'), ('TN 240BK', 'TN 240BK'), ('TN 240C', 'TN 240C'), ('TN 240M', 'TN 240M'), ('TN 240Y', 'TN 240Y'), ('TN 261BK', 'TN 261BK'), ('TN 261C', 'TN 261C'), ('TN 261M', 'TN 261M'), ('TN 261Y', 'TN 261Y'), ('TN 3185', 'TN 3185'), ('TN 3250', 'TN 3250'), ('TN 3290', 'TN 3290'), ('TN 3320', 'TN 3320'), ('TN-260', 'TN-260')], max_length=50, verbose_name='NUMERO DE SERIE'),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='marque_desktop',
            field=models.CharField(choices=[('ACER', 'ACER'), ('APPLE', 'APPLE'), ('ASUS', 'ASUS'), ('DELL', 'DELL'), ('FUJITSU', 'FUJITSU'), ('HP', 'HP'), ('LENOVO', 'LENOVO'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='type_processeur',
            field=models.CharField(choices=[('CELERON', 'CELERON'), ('CORE DUO', 'CORE DUO'), ('CORE I3', 'CORE I3'), ('CORE I5', 'CORE I5'), ('CORE I7', 'CORE I7'), ('DUAL CORE', 'DUAL CORE'), ('INTEL CORE', 'INTEL CORE'), ('INTEL XEON', 'INTEL XEON'), ('PENTIUM', 'PENTIUM')], max_length=50, verbose_name='TYPE DE PROCESSEUR'),
        ),
        migrations.AlterField(
            model_name='imprimante',
            name='marque_imprimante',
            field=models.CharField(choices=[('BROTHER', 'BROTHER'), ('CANON', 'CANON'), ('EPSON', 'EPSON'), ('HP', 'HP'), ('SAMSUNG', 'SAMSUNG')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='imprimante',
            name='modele',
            field=models.CharField(choices=[('CANON 4870', 'CANON 4870'), ('COLOR LASERJET PRO M176 N', 'COLOR LASERJET PRO M176 N'), ('COLOR LASERJET PRO M177 FW MFP', 'COLOR LASERJET PRO M177 FW MFP'), ('COLOR LASERJET', 'COLOR LASERJET'), ('DESKJET 125A', 'DESKJET 125A'), ('DESKJET 2130', 'DESKJET 2130'), ('DESKJET 2180', 'DESKJET 2180'), ('DESKJET 3630 W', 'DESKJET 3630 W'), ('DESKJET 3632', 'DESKJET 3632'), ('DESKJET 3635 W', 'DESKJET 3635 W'), ('IMAGE RUNNER 1133', 'IMAGE RUNNER 1133'), ('I-SENSYS MF41', 'I-SENSYS MF41'), ('LASERJET  PRO MFP 177 FW', 'LASERJET  PRO MFP 177 FW'), ('LASERJET  PRO MFP 227 SDN', 'LASERJET  PRO MFP 227 SDN'), ('LASERJET  PRO MFP 277 DW', 'LASERJET  PRO MFP 277 DW'), ('LASERJET  PRO MFP 477 FDN', 'LASERJET  PRO MFP 477 FDN'), ('LASERJET  PRO MFP 477 FDW', 'LASERJET  PRO MFP 477 FDW'), ('LASERJET M 102 A', 'LASERJET M 102 A'), ('LASERJET M 102 W PO', 'LASERJET M 102 W PRO'), ('LASERJET M176N', 'LASERJET M176N'), ('LASERJET M201N', 'LASERJET M201N'), ('LASERJET M252DW', 'LASERJET M252DW'), ('LASERJET P2035', 'LASERJET P2035'), ('LASERJET PRO 400 M4280W', 'LASERJET PRO 400 M4280W'), ('LASERJET PRO 400', 'LASERJET PRO 400'), ('LASERJET PRO CM1415FN', 'LASERJET PRO CM1415FN'), ('LASERJET PRO M102', 'LASERJET PRO M102'), ('LASERJET PRO M107', 'LASERJET PRO M107'), ('LASERJET PRO M12A', 'LASERJET PRO M12A'), ('LASERJET PRO M12W', 'LASERJET PRO M12W'), ('LASERJET PRO M402DN', 'LASERJET PRO M402DN'), ('LASERJET PRO M426', 'LASERJET PRO M426'), ('LASERJET PRO MF M130A', 'LASERJET PRO MF M130A'), ('LASERJET PRO MF M771', 'LASERJET PRO MF M771'), ('LASERJET PRO MFP M 127FW', 'LASERJET PRO MFP M 127FW'), ('LASERJET PRO MFP M 130', 'LASERJET PRO MFP M 130'), ('LASERJET PRO MFP M127 FN', 'LASERJET PRO MFP M127 FN'), ('LASERJET PRO MFP M225', 'LASERJET PRO MFP M225'), ('LASERJET PRO MFP M226', 'LASERJET PRO MFP M226'), ('LASERJET PRO MFP M25', 'LASERJET PRO MFP M25'), ('LASERJET PRO MFP M26', 'LASERJET PRO MFP M26'), ('LASERJET PRO MFP M521DN', 'LASERJET PRO MFP M521DN'), ('LASERJET PRO N20', 'LASERJET PRO N20'), ('LASERJET PRO P 1606 DN', 'LASERJET PRO P 1606 DN'), ('LBP 6030', 'LBP 6030'), ('OFFICE JET 4010', 'OFFICE JET 4010'), ('OFFICE JET 4610', 'OFFICE JET 4610'), ('XPRESS M 2835', 'XPRESS M 2835'), ('XPRESS M2020', 'XPRESS M2020')], max_length=50, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='marque_laptop',
            field=models.CharField(choices=[('ACER', 'ACER'), ('APPLE', 'APPLE'), ('ASUS', 'ASUS'), ('DELL', 'DELL'), ('FUJITSU', 'FUJITSU'), ('HP', 'HP'), ('LENOVO', 'LENOVO'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA')], max_length=50, verbose_name='MARQUE LAPTOP'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='type_processeur',
            field=models.CharField(choices=[('CELERON', 'CELERON'), ('CORE DUO', 'CORE DUO'), ('CORE I3', 'CORE I3'), ('CORE I5', 'CORE I5'), ('CORE I7', 'CORE I7'), ('DUAL CORE', 'DUAL CORE'), ('INTEL CORE', 'INTEL CORE'), ('INTEL XEON', 'INTEL XEON'), ('PENTIUM', 'PENTIUM')], max_length=50, verbose_name='TYPE DE PROCESSEUR'),
        ),
        migrations.AlterField(
            model_name='logiciel',
            name='licence',
            field=models.CharField(choices=[('1 UTILISATEUR', '1 UTILISATEUR'), ('3 UTILISATEURS', '3 UTILISATEURS'), ('10 UTILISATEURS', '10 UTILISATEURS')], max_length=50, verbose_name='LICENCE'),
        ),
        migrations.AlterField(
            model_name='logiciel',
            name='type_logiciel',
            field=models.CharField(choices=[('ANTIVIRUS', 'ANTIVIRUS'), ('INTERNET SECURITY MULTIDEVICE', 'INTERNET SECURITY MULTIDEVICE'), ('ANTIVIRUS+PAREFEU', 'ANTIVIRUS + PAREFEU')], max_length=50, verbose_name='TYPE DE LOGICIEL'),
        ),
        migrations.AlterField(
            model_name='modemwifi',
            name='marque',
            field=models.CharField(choices=[('ACER', 'ACER'), ('APC', 'APC'), ('APPLE', 'APPLE'), ('ASUS', 'ASUS'), ('BROTHER', 'BROTHER'), ('CANON', 'CANON'), ('CISCO', 'CISCO'), ('D LINK', 'D LINK'), ('DELL', 'DELL'), ('EPSON', 'EPSON'), ('FUJITSU', 'FUJITSU'), ('HP', 'HP'), ('HUAWEI', 'HUAWEI'), ('IMOTION', 'IMOTION'), ('IPAD', 'IPAD'), ('ITC', 'ITC'), ('KATUN', 'KATUN'), ('LENOVO', 'LENOVO'), ('LENOVO', 'LENOVO'), ('LINKSYS', 'LINKSYS'), ('MERCURY', 'MERCURY'), ('PREMAX', 'PREMAX'), ('SAMSUNG', 'SAMSUNG'), ('SANDISK', 'SANDISK'), ('SEAGATE', 'SEAGATE'), ('SEAGATE', 'SEAGATE'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA'), ('TP-LINK', 'TP-LINK')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='photocopieuse',
            name='marque_photocopieuse',
            field=models.CharField(choices=[('BROTHER', 'BROTHER'), ('CANON', 'CANON'), ('EPSON', 'EPSON'), ('HP', 'HP'), ('SAMSUNG', 'SAMSUNG')], max_length=50, verbose_name='MARQUE PHOTOCOPIEUSE'),
        ),
        migrations.AlterField(
            model_name='pointacces',
            name='marque',
            field=models.CharField(choices=[('ACER', 'ACER'), ('APC', 'APC'), ('APPLE', 'APPLE'), ('ASUS', 'ASUS'), ('BROTHER', 'BROTHER'), ('CANON', 'CANON'), ('CISCO', 'CISCO'), ('D LINK', 'D LINK'), ('DELL', 'DELL'), ('EPSON', 'EPSON'), ('FUJITSU', 'FUJITSU'), ('HP', 'HP'), ('HUAWEI', 'HUAWEI'), ('IMOTION', 'IMOTION'), ('IPAD', 'IPAD'), ('ITC', 'ITC'), ('KATUN', 'KATUN'), ('LENOVO', 'LENOVO'), ('LENOVO', 'LENOVO'), ('LINKSYS', 'LINKSYS'), ('MERCURY', 'MERCURY'), ('PREMAX', 'PREMAX'), ('SAMSUNG', 'SAMSUNG'), ('SANDISK', 'SANDISK'), ('SEAGATE', 'SEAGATE'), ('SEAGATE', 'SEAGATE'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA'), ('TP-LINK', 'TP-LINK')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='routeur',
            name='marque',
            field=models.CharField(choices=[('CISCO', 'CISCO'), ('D LINK', 'D LINK'), ('LINKSYS', 'LINKSYS'), ('TP-LINK', 'TP-LINK')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='serveur',
            name='marque',
            field=models.CharField(choices=[('ACER', 'ACER'), ('APPLE', 'APPLE'), ('ASUS', 'ASUS'), ('DELL', 'DELL'), ('FUJITSU', 'FUJITSU'), ('HP', 'HP'), ('LENOVO', 'LENOVO'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='serveur',
            name='type_processeur',
            field=models.CharField(choices=[('CELERON', 'CELERON'), ('CORE DUO', 'CORE DUO'), ('CORE I3', 'CORE I3'), ('CORE I5', 'CORE I5'), ('CORE I7', 'CORE I7'), ('DUAL CORE', 'DUAL CORE'), ('INTEL CORE', 'INTEL CORE'), ('INTEL XEON', 'INTEL XEON'), ('PENTIUM', 'PENTIUM')], max_length=50, verbose_name='TYPE DE PROCESSEUR'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='marque',
            field=models.CharField(choices=[('CISCO', 'CISCO'), ('D LINK', 'D LINK'), ('LINKSYS', 'LINKSYS'), ('TP-LINK', 'TP-LINK')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='tablette',
            name='modele_tablette',
            field=models.CharField(choices=[('AIR2', 'AIR 2'), ('PRO 1', 'PRO 1'), ('PRO 2', 'PRO 2'), ('TAB 3 ESSENTIAL', 'TAB 3 ESSENTIAL'), ('TAB A(6)', 'TAB A(6)'), ('TAB E', 'TAB E'), ('TAB S2', 'TAB S2'), ('TAB S3', 'TAB S3')], max_length=100, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='tablette',
            name='systeme_exploitation',
            field=models.CharField(choices=[('ANDROID', 'ANDROID'), ('IOS', 'IOS'), ('WIN7', 'WIN7'), ('WIN8', 'WIN8'), ('WIN10', 'WIN10')], max_length=100, verbose_name="SYSTEME D'EXPLOITATION"),
        ),
        migrations.AlterField(
            model_name='unite_stockage',
            name='marque',
            field=models.CharField(choices=[('HP', 'HP'), ('IMATION', 'IMATION'), ('SANDISK', 'SANDISK'), ('SEAGATE', 'SEAGATE'), ('SEAGATE', 'SEAGATE'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA'), ('WESTERN DIGITAL', 'WESTERN DIGITAL')], max_length=50, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='unite_stockage',
            name='type_stockage',
            field=models.CharField(choices=[('CD-RW', 'CD-RW'), ('DISQUE EXTERNE', 'DISQUE EXTERNE'), ('DISQUE INTERNE DESKTOP', 'DISQUE INTERNE DESKTOP'), ('DISQUE INTERNE LAPTOP', 'DISQUE INTERNE LAPTOP'), ('DVD', 'DVD'), ('FLASHDISK', 'FLASHDISK'), ('MEMOIRE SD', 'MEMOIRE SD')], max_length=50, verbose_name='TYPE DE STOCKAGE'),
        ),
    ]
