# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-31 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0422_auto_20180531_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterie',
            name='capacite_batterie',
            field=models.CharField(choices=[('40AH ', '40AH'), ('45AH ', '45AH'), ('60AH ', '60AH'), ('62AH ', '62AH'), ('65AH ', '65AH'), ('66AH ', '66AH'), ('70AH ', '70AH'), ('75AH ', '75AH'), ('80AH ', '80AH'), ('85AH ', '85AH'), ('85AH ', '85AH'), ('88AH ', '88AH'), ('90AH ', '90AH'), ('95AH ', '95AH'), ('100AH', '100AH'), ('105AH', '105AH'), ('120AH', '120AH'), ('150AH', '150AH'), ('180AH', '180AH'), ('200AH', '200AH'), ('220AH', '220AH')], max_length=100, verbose_name='CAPACITE EN AMPERE-HEURE'),
        ),
        migrations.AlterField(
            model_name='batterie',
            name='forme_batterie',
            field=models.CharField(choices=[('DIN', 'DIN'), ('N', 'N'), ('NL', 'NL')], max_length=100, verbose_name='FORME'),
        ),
        migrations.AlterField(
            model_name='batterie',
            name='marque_batterie',
            field=models.CharField(choices=[('AK', 'AK'), ('LARGESTAR', 'LARGESTAR'), ('TUDOR', 'TUDOR')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='bougie',
            name='marque_bougie',
            field=models.CharField(choices=[('BERU', 'BERU'), ('BOSCH', 'BOSCH'), ('NJK', 'NJK'), ('TOYOTA', 'TOYOTA')], max_length=100, verbose_name='MARQUE DE BOUGIE'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='avenue',
            field=models.CharField(choices=[('COLONEL EBEYA', 'COLONEL EBEYA'), ('KASAI', 'KASAI'), ('KASAVUBU', 'KASAVUBU'), ('LUAMBO MAKIADI', 'LUAMBO MAKIADI'), ('SENEGALAIS', 'SENEGALAIS')], max_length=20, verbose_name='AVENUE'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='commune',
            field=models.CharField(choices=[('BANDALUNGWA', 'BANDALUNGWA'), ('GOMBE', 'GOMBE'), ('KASAVUBU', 'KASAVUBU'), ('LIMETE', 'LIMETE')], max_length=20, verbose_name='COMMUNE'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='type_lit',
            field=models.CharField(choices=[('LIT DOUBLE', 'LIT DOUBLE'), ('LIT SIMPLE', 'LIT SIMPLE')], max_length=20, verbose_name='TYPE DE LIT'),
        ),
        migrations.AlterField(
            model_name='constructionbatiment',
            name='nombre_de_pieces',
            field=models.CharField(choices=[('1 -10', '1 -10'), ('11 - 20', '11 - 20'), ('21 - 30', '21 - 30'), ('31 - 40', '31 - 40'), ('41 - 50', '41 - 50'), ('51 - 60', '51 - 60'), ('61 - 70', '61 - 70'), ('71 - 80', '71 - 80'), ('81 - 90', '81 - 90'), ('91 -100', '91 -100')], max_length=50, verbose_name='NOMBRE DE PIECES'),
        ),
        migrations.AlterField(
            model_name='constructionbatiment',
            name='qualite_du_terrain',
            field=models.CharField(choices=[('ALCALINO-TERREUX', 'ALCALINO-TERREUX'), ('ARGILEUX', 'ARGILEUX'), ('MARECAGEUX', 'MARECAGEUX'), ('SABLONEUX', 'SABLONEUX')], max_length=50, verbose_name='QUALITE DU TERRAIN'),
        ),
        migrations.AlterField(
            model_name='constructionbatiment',
            name='usage_du_batiment',
            field=models.CharField(choices=[('COMMERCIAL LUXUEUX', 'COMMERCIAL LUXUEUX'), ('COMMERCIAL ORDINAIRE', 'COMMERCIAL ORDINAIRE'), ('ENTREPOT', 'ENTREPOT'), ('RESIDENTIEL LUXUEUX', 'RESIDENTIEL LUXUEUX'), ('RESIDENTIEL ORDINAIRE', 'RESIDENTIEL ORDINAIRE')], max_length=50, verbose_name='USAGE DU BATIMENT'),
        ),
        migrations.AlterField(
            model_name='constructionroute',
            name='couche_de_beton',
            field=models.CharField(choices=[('NON APPLICABLE', 'NON APPLICABLE'), ('9M³ DE BETON SUR 10M', '9M3 DE BETON SUR 10M')], max_length=50, verbose_name='COUCHE DE BETON'),
        ),
        migrations.AlterField(
            model_name='constructionroute',
            name='couche_de_terre_jaune',
            field=models.CharField(choices=[('NON APPLICABLE', 'NON APPLICABLE'), ('15M³ DE TERRE JAUNE SUR 10M', '15M3 DE TERRE JAUNE SUR 10M')], max_length=50, verbose_name='COUCHE DE TERRE JAUNE'),
        ),
        migrations.AlterField(
            model_name='constructionroute',
            name='couche_de_tout_venant',
            field=models.CharField(choices=[('NON APPLICABLE', 'NON APPLICABLE'), ('15M³ DE 0/31 SUR 10 M', '15M3 DE 0/31 SUR 10 M')], max_length=50, verbose_name='COUCHE DE TOUT VENANT'),
        ),
        migrations.AlterField(
            model_name='constructionroute',
            name='type_de_route',
            field=models.CharField(choices=[('ROUTE ASPHALTEE', 'ROUTE ASPHALTEE'), ('ROUTE DE DESSERTE AGRICOLE', 'ROUTE DE DESSERTE AGRICOLE'), ('ROUTE STABILISEE', 'ROUTE STABILISEE')], max_length=50, verbose_name='TYPE DE ROUTE'),
        ),
        migrations.AlterField(
            model_name='locationdepot',
            name='commune',
            field=models.CharField(choices=[('BANDALUNGWA', 'BANDALUNGWA'), ('GOMBE', 'GOMBE'), ('KASAVUBU', 'KASAVUBU'), ('LIMETE', 'LIMETE')], max_length=100, verbose_name='COMMUNE'),
        ),
        migrations.AlterField(
            model_name='locationvehicule',
            name='marque',
            field=models.CharField(choices=[('IVECO', 'IVECO'), ('MAN', 'MAN'), ('MERCEDES', 'MERCEDES'), ('NISSAN', 'NISSAN'), ('TOYOTA', 'TOYOTA'), ('ZOTYE', 'ZOTYE'), ('ZX AUTO', 'ZX AUTO')], max_length=100, verbose_name='MARQUE DU VEHICULE'),
        ),
        migrations.AlterField(
            model_name='locationvehicule',
            name='modele',
            field=models.CharField(choices=[('26-28', '26-28'), ('26-36', '26-36'), ('33-330', '33-330'), ('ACTROS', 'ACTROS'), ('ALLEX', 'ALLEX'), ('ALMERA', 'ALMERA'), ('CAMRY', 'CAMRY'), ('CIVILIAN', 'CIVILIAN'), ('COROLLA', 'COROLLA'), ('GRAND TIGER SUV', 'GRAND TIGER SUV'), ('GRANDTIGER PICK UP', 'GRANDTIGER PICK UP'), ('HARDBODY', 'HARDBODY'), ('HIACE', 'HIACE'), ('HILUX DOUBLE CABINE', 'HILUX DOUBLE CABINE'), ('JUKE', 'JUKE'), ('LAND CRUISER RUNNER', 'LAND CRUISER RUNNER'), ('LAND CRUISER', 'LAND CRUISER'), ('NAVARA PICK UP ', 'NAVARA PICK UP '), ('NOAH', 'NOAH'), ('PATHFINDER', 'PATHFINDER'), ('PATROL 10 PLACE ', 'PATROL 10 PLACE '), ('PATROL PICK UP SIMPLE CABINE', 'PATROL PICK UP SIMPLE CABINE'), ('PATROL V8-SE', 'PATROL V8-SE'), ('PRADO', 'PRADO'), ('QUASHKA', 'QUASHKA'), ('RAV4', 'RAV4'), ('SENTRA', 'SENTRA'), ('SUNNY', 'SUNNY'), ('TERRALORD LUXURY', 'TERRALORD LUXURY'), ('URVAN', 'URVAN'), ('X TRAIL 2X4', 'X TRAIL 2X4'), ('X TRAIL 4X4', 'X TRAIL 4X4'), ('YARIS', 'YARIS'), ('Z100', 'Z100')], max_length=100, verbose_name='MODELE DU VEHICULE'),
        ),
        migrations.AlterField(
            model_name='moteur',
            name='marque',
            field=models.CharField(choices=[('IVECO', 'IVECO'), ('MAN', 'MAN'), ('MERCEDES', 'MERCEDES'), ('NISSAN', 'NISSAN'), ('TOYOTA', 'TOYOTA'), ('ZOTYE', 'ZOTYE'), ('ZX AUTO', 'ZX AUTO')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='moteur',
            name='modele',
            field=models.CharField(blank=True, choices=[('26-28', '26-28'), ('26-36', '26-36'), ('33-330', '33-330'), ('ACTROS', 'ACTROS'), ('ALLEX', 'ALLEX'), ('ALMERA', 'ALMERA'), ('CAMRY', 'CAMRY'), ('CIVILIAN', 'CIVILIAN'), ('COROLLA', 'COROLLA'), ('GRAND TIGER SUV', 'GRAND TIGER SUV'), ('GRANDTIGER PICK UP', 'GRANDTIGER PICK UP'), ('HARDBODY', 'HARDBODY'), ('HIACE', 'HIACE'), ('HILUX DOUBLE CABINE', 'HILUX DOUBLE CABINE'), ('JUKE', 'JUKE'), ('LAND CRUISER RUNNER', 'LAND CRUISER RUNNER'), ('LAND CRUISER', 'LAND CRUISER'), ('NAVARA PICK UP ', 'NAVARA PICK UP '), ('NOAH', 'NOAH'), ('PATHFINDER', 'PATHFINDER'), ('PATROL 10 PLACE ', 'PATROL 10 PLACE '), ('PATROL PICK UP SIMPLE CABINE', 'PATROL PICK UP SIMPLE CABINE'), ('PATROL V8-SE', 'PATROL V8-SE'), ('PRADO', 'PRADO'), ('QUASHKA', 'QUASHKA'), ('RAV4', 'RAV4'), ('SENTRA', 'SENTRA'), ('SUNNY', 'SUNNY'), ('TERRALORD LUXURY', 'TERRALORD LUXURY'), ('URVAN', 'URVAN'), ('X TRAIL 2X4', 'X TRAIL 2X4'), ('X TRAIL 4X4', 'X TRAIL 4X4'), ('YARIS', 'YARIS'), ('Z100', 'Z100')], max_length=100, null=True, verbose_name='MODEL'),
        ),
        migrations.AlterField(
            model_name='motodeuxroues',
            name='modele_moto',
            field=models.CharField(choices=[('APACHE', 'APACHE'), ('KING DELUXE', 'KING DELUXE'), ('STAR HLX', 'STAR HLX'), ('ZT', 'ZT')], max_length=100, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='mototroisroues',
            name='modele_moto',
            field=models.CharField(choices=[('APACHE', 'APACHE'), ('KING DELUXE', 'KING DELUXE'), ('STAR HLX', 'STAR HLX'), ('ZT', 'ZT')], max_length=100, verbose_name='MODELE'),
        ),
        migrations.AlterField(
            model_name='piecederechangecarrosserie',
            name='type_piece_carosserie',
            field=models.CharField(choices=[('BALAI ESSUIE GLACE AVANT', 'BALAI ESSUIE GLACE AVANT'), ('FEU ARRIERE DROIT', 'FEU ARRIERE DROIT'), ('FEU ARRIERE GAUCHE', 'FEU ARRIERE GAUCHE'), ('PHARE AVANT DROIT', 'PHARE AVANT DROIT'), ('PHARE AVANT GAUCHE', 'PHARE AVANT GAUCHE'), ('RETROVISEUR DROIT', 'RETROVISEUR DROIT'), ('RETROVISEUR GAUCHE', 'RETROVISEUR GAUCHE')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecederechangedirectionsuspension',
            name='type_piece_direction_suspension',
            field=models.CharField(choices=[('AMORTISSEUR ARRIERE DROIT', 'AMORTISSEUR ARRIERE DROIT'), ('AMORTISSEUR ARRIERE GAUCHE', 'AMORTISSEUR ARRIERE GAUCHE'), ('AMORTISSEUR AVANT DROIT', 'AMORTISSEUR AVANT DROIT'), ('AMORTISSEUR AVANT GAUCHE', 'AMORTISSEUR AVANT GAUCHE'), ('AMORTISSEUR DE DIRECTION', 'AMORTISSEUR DE DIRECTION'), ('BIELLETTE STABILISATRICE ARRIERE DROITE', 'BIELLETTE STABILISATRICE ARRIERE DROITE'), ('BIELLETTE STABILISATRICE ARRIERE GAUCHE', 'BIELLETTE STABILISATRICE ARRIERE GAUCHE'), ('BIELLETTE STABILISATRICE AVANT DROITE', 'BIELLETTE STABILISATRICE AVANT DROITE'), ('BIELLETTE STABILISATRICE AVANT GAUCHE + DROITE', 'BIELLETTE STABILISATRICE AVANT GAUCHE + DROITE'), ('BIELLETTE STABILISATRICE AVANT GAUCHE', 'BIELLETTE STABILISATRICE AVANT GAUCHE'), ('BRAS DE SUSPENSION INFERIEURE DROITE', 'BRAS DE SUSPENSION INFERIEURE DROITE'), ('BRAS DE SUSPENSION INFERIEURE GAUCHE', 'BRAS DE SUSPENSION INFERIEURE GAUCHE'), ('BRAS DE SUSPENSION SUPERIEUR DROITE', 'BRAS DE SUSPENSION SUPERIEUR DROITE'), ('BRAS DE SUSPENSION SUPERIEUR GAUCHE', 'BRAS DE SUSPENSION SUPERIEUR GAUCHE'), ('BRAS DE SUSPENSION SUPERIEURE DROITE', 'BRAS DE SUSPENSION SUPERIEURE DROITE'), ('BRAS DE SUSPENSION SUPERIEURE GAUCHE', 'BRAS DE SUSPENSION SUPERIEURE GAUCHE'), ('CREMAILLEUR DE DIRECTION', 'CREMAILLEUR DE DIRECTION'), ('DEMARREUR', 'DEMARREUR'), ('LAME MAITRESSE', 'LAME MAITRESSE'), ('POMPE DE DIRECTION', 'POMPE DE DIRECTION'), ('ROTULE DE DIRECTION EXTERIEURE DROIT', 'ROTULE DE DIRECTION EXTERIEURE DROIT'), ('ROTULE DE DIRECTION EXTERIEURE DROITE', 'ROTULE DE DIRECTION EXTERIEURE DROITE'), ('ROTULE DE DIRECTION EXTERIEURE GAUCHE', 'ROTULE DE DIRECTION EXTERIEURE GAUCHE'), ('ROTULE DE DIRECTION EXTERIEURE GAUCHE', 'ROTULE DE DIRECTION EXTERIEURE GAUCHE'), ('ROTULE DE DIRECTION INFERIEUR DROIT', 'ROTULE DE DIRECTION INFERIEUR DROIT'), ('ROTULE DE DIRECTION INFERIEUR GAUCHE', 'ROTULE DE DIRECTION INFERIEUR GAUCHE'), ('ROTULE DE DIRECTION INFERIEURE DROITE', 'ROTULE DE DIRECTION INFERIEURE DROITE'), ('ROTULE DE DIRECTION INFERIEURE GAUCHE', 'ROTULE DE DIRECTION INFERIEURE GAUCHE'), ('ROTULE DE SUSPENSION INFERIEURE DROITE', 'ROTULE DE SUSPENSION INFERIEURE DROITE'), ('ROTULE DE SUSPENSION INFERIEURE GAUCHE', 'ROTULE DE SUSPENSION INFERIEURE GAUCHE'), ('ROTULE DE SUSPENSION SUPERIEURE DROITE', 'ROTULE DE SUSPENSION SUPERIEURE DROITE'), ('ROTULE DE SUSPENSION SUPERIEURE GAUCHE', 'ROTULE DE SUSPENSION SUPERIEURE GAUCHE'), ('SILEMBLOC BARRE STABILISATRICE ARRIERE', 'SILEMBLOC BARRE STABILISATRICE ARRIERE'), ('SILEMBLOC BARRE STABILISATRICE AV 48632-60020', 'SILEMBLOC BARRE STABILISATRICE AV 48632-60020'), ('SILEMBLOC BARRE STABILISATRICE AV 48815-60180', 'SILEMBLOC BARRE STABILISATRICE AV 48815-60180'), ('SILEMBLOC BARRE STABILISATRICE AV', 'SILEMBLOC BARRE STABILISATRICE AV'), ('SILEMBLOC BARRE STABILISATRICE AVANT', 'SILEMBLOC BARRE STABILISATRICE AVANT'), ('SILEMBLOC BRAS DE STABILISATION AV', 'SILEMBLOC BRAS DE STABILISATION AV'), ('SILEMBLOC BRAS DE SUSPENSION INFERIEUR 1', 'SILEMBLOC BRAS DE SUSPENSION INFERIEUR 1'), ('SILEMBLOC BRAS DE SUSPENSION SUPERIEUR', 'SILEMBLOC BRAS DE SUSPENSION SUPERIEUR'), ('SILEMBLOC BRAS DE SUSPENSION SUPERIEURE', 'SILEMBLOC BRAS DE SUSPENSION SUPERIEURE'), ('SILEMBLOC LAME INFERIEURE', 'SILEMBLOC LAME INFERIEURE'), ('SILEMBLOC LAME SUPERIEURE', 'SILEMBLOC LAME SUPERIEURE'), ('SOUFFLET DE DIRECTION', 'SOUFFLET DE DIRECTION')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecederechangeelectrique',
            name='type_piece_electrique',
            field=models.CharField(choices=[('ALTERNATEUR', 'ALTERNATEUR'), ('CONTACTEUR DE PRESSION D’HUILE', 'CONTACTEUR DE PRESSION D’HUILE'), ('CONTACTEUR PRESSION HUILE', 'CONTACTEUR PRESSION HUILE'), ('DEMARREUR', 'DEMARREUR'), ('INTERRUPTEUR DE TEMPERATURE', 'INTERRUPTEUR DE TEMPERATURE'), ('POMPE A VIDE ALTERNATEUR', 'POMPE A VIDE ALTERNATEUR'), ('RELAI DE DEMARRAGE', 'RELAI DE DEMARRAGE')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecederechangeembrayage',
            name='type_piece_embrayage',
            field=models.CharField(choices=[('BUTEE EMBRAYAGE', 'BUTEE EMBRAYAGE'), ('CYLINDRE EMETTEUR', 'CYLINDRE EMETTEUR'), ('CYLINDRE RECEPTEUR', 'CYLINDRE RECEPTEUR'), ('DISQUE EMBRAYAGE', 'DISQUE EMBRAYAGE'), ('KIT DE REPARATION CYLINDRE EMETTEUR', 'KIT DE REPARATION CYLINDRE EMETTEUR'), ('KIT DE REPARATION CYLINDRE RECEPTEUR', 'KIT DE REPARATION CYLINDRE RECEPTEUR'), ('PLATEAU EMBRAYAGE', 'PLATEAU EMBRAYAGE')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecederechangefreinage',
            name='pieces_rechange_freinage',
            field=models.CharField(choices=[('CYLINDRE DE ROUE ARRIERE DROITE', 'CYLINDRE DE ROUE ARRIERE DROITE'), ('CYLINDRE DE ROUE ARRIERE GAUCHE', 'CYLINDRE DE ROUE ARRIERE GAUCHE'), ('DISQUE DE FREIN AVANT', 'DISQUE DE FREIN AVANT'), ('DISQUE/TAMBOUR DE FREIN ARRIERE', 'DISQUE/TAMBOUR DE FREIN ARRIERE'), ('MAITRE CYLINDRE DE FREIN', 'MAITRE CYLINDRE DE FREIN'), ('PLAQUETTE DE FREIN AVANT', 'PLAQUETTE DE FREIN AVANT'), ('PLAQUETTE/MACHOIRE DE FREIN ARRIERE', 'PLAQUETTE/MACHOIRE DE FREIN ARRIERE')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecederechangerefroidissement',
            name='type_piece_refroidissement',
            field=models.CharField(choices=[('ACCOUPLEMENT HYDRAULIQUE', 'ACCOUPLEMENT HYDRAULIQUE'), ('BOUCHON RADIATEUR', 'BOUCHON RADIATEUR'), ('COURROIE ALTERNATEUR', 'COURROIE ALTERNATEUR'), ('POMPE A EAU', 'POMPE A EAU'), ('RADIATEUR', 'RADIATEUR'), ('THERMOSTAT', 'THERMOSTAT'), ('VENTILATEUR', 'VENTILATEUR')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecederechangetransmission',
            name='type_piece_transmission',
            field=models.CharField(choices=[('CROISILLON 1', 'CROISILLON 1'), ('CROISILLON', 'CROISILLON'), ('ECROU DE ROUE ARRIERE', 'ECROU DE ROUE ARRIERE'), ('ECROU DE ROUE AVANT', 'ECROU DE ROUE AVANT'), ('GOUJON DE ROUE ARRIERE', 'GOUJON DE ROUE ARRIERE'), ('GOUJON DE ROUE AVANT', 'GOUJON DE ROUE AVANT'), ('KIT DE ROULEMENT ROUE ARRIERE', 'KIT DE ROULEMENT ROUE ARRIERE'), ('KIT DE ROULEMENT ROUE AVANT DROITE', 'KIT DE ROULEMENT ROUE AVANT DROITE'), ('KIT DE ROULEMENT ROUE AVANT GAUCHE', 'KIT DE ROULEMENT ROUE AVANT GAUCHE'), ('KIT ROULEMENT DE ROUE AVANT DROIT', 'KIT ROULEMENT DE ROUE AVANT DROIT'), ('KIT ROULEMENT DE ROUE AVANT GAUCHE', 'KIT ROULEMENT DE ROUE AVANT GAUCHE'), ('MOYEU AVANT GAUCHE', 'MOYEU AVANT GAUCHE'), ('PALIER DE TRANSMISSION', 'PALIER DE TRANSMISSION'), ('SOUFFLET DE TRANSMISSION', 'SOUFFLET DE TRANSMISSION')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecerechangemoteur',
            name='pieces_rechange_moteur',
            field=models.CharField(choices=[('COURROIE COMPRESSEUR', 'COURROIE COMPRESSEUR'), ('COURROIE DE DISTRIBUTION', 'COURROIE DE DISTRIBUTION'), ('COURROIE DIRECTION', 'COURROIE DIRECTION'), ('COURROIE DISTRIBUTION', 'COURROIE DISTRIBUTION'), ('FILTRE A AIR', 'FILTRE A AIR'), ('FILTRE A CARBURANT  16405-01T0A', 'FILTRE A CARBURANT  16405-01T0A'), ('FILTRE A CARBURANT  16405-02N0A', 'FILTRE A CARBURANT  16405-02N0A'), ('FILTRE A CARBURANT', 'FILTRE A CARBURANT'), ('FILTRE A HUILE', 'FILTRE A HUILE'), ('FILTRE HABITACLE', 'FILTRE HABITACLE'), ('INJECTEUR COMPLET', 'INJECTEUR COMPLET'), ('INJECTEUR', 'INJECTEUR'), ('NEZ INJECTEUR', 'NEZ INJECTEUR'), ('POMPE A CARBURANT', 'POMPE A CARBURANT'), ('POMPE A HUILE', 'POMPE A HUILE'), ('SUPPORT MOTEUR', 'SUPPORT MOTEUR'), ('TENDEUR ALTERNATEUR', 'TENDEUR ALTERNATEUR'), ('TENDEUR DISTRIBUTION', 'TENDEUR DISTRIBUTION'), ('TURBO COMPRESSEUR', 'TURBO COMPRESSEUR')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='piecerevisionmoteur',
            name='pieces_revision_moteur',
            field=models.CharField(choices=[('BIELLE MOTEUR', 'BIELLE MOTEUR'), ('BOURRAGE MOTEUR ', 'BOURRAGE MOTEUR '), ('BOURRAGE MOTEUR BOUR04403', 'BOURRAGE MOTEUR BOUR04403'), ('BOURRAGE MOTEUR', 'BOURRAGE MOTEUR'), ('CHEMISE (JEU DE 4 PIECES)', 'CHEMISE (JEU DE 4 PIECES)'), ('CHEMISE(JEU DE 4 PCES)', 'CHEMISE(JEU DE 4 PCES)'), ('COUSSINET BIELLE', 'COUSSINET BIELLE'), ('COUSSINET LATERAL', 'COUSSINET LATERAL'), ('COUSSINET PALIER', 'COUSSINET PALIER'), ('CROISILLON 1', 'CROISILLON 1'), ('CROISILLON 2', 'CROISILLON 2'), ('GOUJON DE ROUE ARRIERE', 'GOUJON DE ROUE ARRIERE'), ('JOINT DE CULASSE', 'JOINT DE CULASSE'), ('PISTON (SANS SEGMENT)', 'PISTON (SANS SEGMENT)'), ('PISTON(SANS SEGMENT)', 'PISTON(SANS SEGMENT)'), ('POCHETTE DE JOINT', 'POCHETTE DE JOINT'), ('RETIENT HUILE', 'RETIENT HUILE'), ('ROULEMENT MOYEU ARRIERE', 'ROULEMENT MOYEU ARRIERE'), ('SEGMENTS', 'SEGMENTS')], max_length=50, verbose_name='TYPE DE PIECE'),
        ),
        migrations.AlterField(
            model_name='pneu',
            name='dimension_pneu',
            field=models.CharField(choices=[('1100R20', '1100R20'), ('1100R22.5', '1100R22.5'), ('1200R20', '1200R20'), ('1200R22.5', '1200R22.5'), ('1400R20', '1400R20'), ('1400R22.5', '1400R22.5'), ('145R12', '145R12'), ('155/70R13', '155/70R13'), ('165/65R14', '165/65R14'), ('165/70R13', '165/70R13'), ('175/70R13', '175/70R13'), ('175/70R14', '175/70R14'), ('175/70R15', '175/70R15'), ('185/65R14', '185/65R14'), ('185/65R15', '185/65R15'), ('185/70R13', '185/70R13'), ('185/70R14', '185/70R14'), ('185R14C', '185R14C'), ('195/65R15', '195/65R15'), ('195/70R14', '195/70R14'), ('195/70R15', '195/70R15'), ('195/75R15C', '195/75R15C'), ('195R14C', '195R14C'), ('195R15C', '195R15C'), ('205/55R16', '205/55R16'), ('205/65R15', '205/65R15'), ('205/70R15C', '205/70R15C'), ('205/80R16', '205/80R16'), ('205R14C', '205R14C'), ('205R15', '205R15'), ('205R16', '205R16'), ('215/65R16', '215/65R16'), ('215/70R16', '215/70R16'), ('215/80R15', '215/80R15'), ('215R14C', '215R14C'), ('215R15', '215R15'), ('225/60R17', '225/60R17'), ('225/65R17', '225/65R17'), ('225/70R14', '225/70R14'), ('225/70R15', '225/70R15'), ('225/70R15', '225/70R15'), ('225/70R16', '225/70R16'), ('225/70R17', '225/70R17'), ('225/75R16', '225/75R16'), ('235/60R16', '235/60R16'), ('235/65R17', '235/65R17'), ('235/70R15', '235/70R15'), ('235/70R16', '235/70R16'), ('235/70R17', '235/70R17'), ('235/70R18', '235/70R18'), ('235/75R15', '235/75R15'), ('245/65R17', '245/65R17'), ('245/70R16', '245/70R16'), ('245/70R17', '245/70R17'), ('245/70R18', '245/70R18'), ('245/75R16', '245/75R16'), ('255/55R17', '255/55R17'), ('255/55R18', '255/55R18'), ('255/70R16', '255/70R16'), ('265/60R18', '265/60R18'), ('265/70R15', '265/70R15'), ('265/70R16', '265/70R16'), ('265/70R17', '265/70R17'), ('275/60R17', '275/60R17'), ('275/65R17', '275/65R17'), ('275/75R16', '275/75R16'), ('295/80R22.5', '295/80R22.5'), ('315/80R20', '315/80R20'), ('315R20', '315R20'), ('650R16', '650R16'), ('750R16 LT', '750R16 LT'), ('825R16', '825R16'), ('900R20', '900R20'), ('900R22.5', '900R22.5')], max_length=100, verbose_name='DIMENSION'),
        ),
        migrations.AlterField(
            model_name='triplex',
            name='epaisseur',
            field=models.CharField(choices=[('5MM', '5MM'), ('8MM', '8MM'), ('10MM', '10MM')], max_length=100, verbose_name='EPAISSEUR'),
        ),
        migrations.AlterField(
            model_name='voiturejeepbus',
            name='marque_voiture',
            field=models.CharField(choices=[('IVECO', 'IVECO'), ('MAN', 'MAN'), ('MERCEDES', 'MERCEDES'), ('NISSAN', 'NISSAN'), ('TOYOTA', 'TOYOTA'), ('ZOTYE', 'ZOTYE'), ('ZX AUTO', 'ZX AUTO')], max_length=100, verbose_name='MARQUE'),
        ),
        migrations.AlterField(
            model_name='voiturejeepbus',
            name='modele_voiture',
            field=models.CharField(choices=[('ALMERA', 'ALMERA'), ('CIVILIAN', 'CIVILIAN'), ('GRAND TIGER SUV', 'GRAND TIGER SUV'), ('GRANDTIGER  PICK UP', 'GRANDTIGER  PICK UP'), ('HARDBODY', 'HARDBODY'), ('JUKE', 'JUKE'), ('NAVARA PICK UP', 'NAVARA PICK UP'), ('PATHFINDER', 'PATHFINDER'), ('PATROL 10 PLACE', 'PATROL 10 PLACE'), ('PATROL PICK UP SIMPLE CABINE', 'PATROL PICK UP SIMPLE CABINE'), ('PATROL V8-SE', 'PATROL V8-SE'), ('QUASHKAI', 'QUASHKAI'), ('SENTRA', 'SENTRA'), ('SPRINTER 209', 'SPRINTER 209'), ('SPRINTER 313 CDI ', 'SPRINTER 313 CDI '), ('SUNNY', 'SUNNY'), ('TERRALORD LUXURY', 'TERRALORD LUXURY'), ('URVAN', 'URVAN'), ('X TRAIL 2X4', 'X TRAIL 2X4'), ('X TRAIL 4X4', 'X TRAIL 4X4'), ('Z100', 'Z100')], max_length=100, verbose_name='MODELE'),
        ),
    ]
