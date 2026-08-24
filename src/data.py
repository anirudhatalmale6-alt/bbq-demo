# -*- coding: utf-8 -*-
"""Page unique « BBQ & matériel de cuisson — Équipements et accessoires ».

BRIEF DU CLIENT (tableur, ligne 2) : « Page consacrée aux équipements de
barbecue et de cuisson : barbecues au gaz, charbon et électriques, grils
professionnels, fumoirs, planchas, fours, équipements de cuisson extérieure,
accessoires, ustensiles, pièces et solutions pour particuliers, restauration
et usage professionnel. Présentation des fabricants, catégories,
spécifications, approvisionnement et distribution. »

CE QUI N'Y EST PAS, ET POURQUOI.

  - AUCUN NOM DE FABRICANT. Le brief demande « présentation des fabricants ».
    Je n'en cite aucun. Citer un fabricant sur une page commerciale sans
    accord de distribution est un probleme juridique, et un catalogue qui
    affiche des marques qu'il ne distribue pas trompe l'acheteur. La page dit
    donc CE QU'UNE FICHE FABRICANT DOIT CONTENIR — pays de fabrication,
    conformite declaree, delai sur les pieces, garantie, politique de
    quantite minimale — sans en remplir une seule.
  - AUCUNE VALEUR CHIFFREE sur un produit. Pas de puissance, pas de surface de
    cuisson, pas de temperature, pas de nombre de bruleurs, pas de poids. Ce
    sont des NOMS DE CHAMPS. Je n'ai mesure aucun appareil.
  - AUCUN PRIX, aucune remise, aucune quantite minimale chiffree, aucun delai.
  - AUCUNE CONFORMITE AFFIRMEE. Le gaz et l'electrique sont des domaines
    reglementes : « conforme » est une declaration que seul le fabricant peut
    faire, avec son dossier. La page ouvre le champ, elle ne le remplit pas.

LE TROISIEME AXE. Comme sur la page foresterie, le filtre par SEGMENT n'est
pas decoratif : un barbecue de jardin et un gril de brasserie ne se vendent
pas au meme client, ne s'installent pas dans les memes conditions et ne sont
pas soumis aux memes obligations. Les melanger dans une liste a plat, c'est
faire perdre son temps aux deux acheteurs.

Tous les compteurs sont DERIVES de ces listes.
"""

MARQUE = 'BBQ & MATÉRIEL DE CUISSON'
TITRE = 'catalogue équipements, accessoires et pièces'

# Palette : sujet chaud, mais catalogue technique. Encre neutre, accent brique.
# Contrastes MESURES par tests.py.
FOND     = '#f6f5f4'
CARTE    = '#ffffff'
LIGNE    = '#e2dedb'
ENCRE    = '#1b1614'
TEXTE    = '#403834'
MUET     = '#665c56'
ACCENT   = '#9c3d17'
ACCENT_D = '#772d10'

# ---------------------------------------------------------------------------
# LES FAMILLES. Reprises du brief, dans son ordre, completees des categories
# qu'il implique sans les nommer (combustibles, entretien).
# ---------------------------------------------------------------------------
FAMILLES = [
    ('barbecues',    'Barbecues'),
    ('grils',        'Grils et plaques professionnels'),
    ('fumoirs',      'Fumoirs et cuisson lente'),
    ('planchas',     'Planchas et plaques de cuisson'),
    ('fours',        'Fours et cuisson à haute température'),
    ('exterieur',    'Cuisine extérieure et aménagement'),
    ('accessoires',  'Accessoires et ustensiles'),
    ('combustibles', 'Combustibles et consommables'),
    ('pieces',       'Pièces détachées'),
    ('entretien',    'Entretien, hygiène et sécurité'),
]

# ---------------------------------------------------------------------------
# L'ENERGIE. C'est le tout premier filtre d'un acheteur : elle decide de
# l'installation, de l'autorisation d'exploiter et du cout d'usage.
# ---------------------------------------------------------------------------
ENERGIES = [
    ('gaz',        'Gaz'),
    ('charbon',    'Charbon de bois'),
    ('electrique', 'Électrique'),
    ('bois',       'Bois et granulés'),
    ('mixte',      'Multi-énergie'),
    ('aucune',     'Sans énergie propre'),
]

# ---------------------------------------------------------------------------
# LE SEGMENT. Deuxieme axe : a qui ca se vend.
# ---------------------------------------------------------------------------
SEGMENTS = [
    ('particulier',  'Particulier'),
    ('restauration', 'Restauration'),
    ('collectivite', 'Collectivité et cuisine centrale'),
    ('traiteur',     'Traiteur et événementiel'),
    ('revente',      'Revente et distribution'),
]

# ---------------------------------------------------------------------------
# LA GRILLE DE CHAMPS. Des NOMS DE CHAMPS, jamais des valeurs.
# ---------------------------------------------------------------------------
CHAMPS = [
    ('surface',    'Surface de cuisson'),
    ('bruleurs',   'Nombre et type de brûleurs'),
    ('puissance',  'Puissance nominale'),
    ('plage',      'Plage de température'),
    ('regulation', 'Mode de régulation'),
    ('allumage',   'Type d’allumage'),
    ('grille',     'Matériau de la grille'),
    ('corps',      'Matériau du corps et de la cuve'),
    ('isolation',  'Isolation et double paroi'),
    ('gaz',        'Type de gaz et détendeur'),
    ('elec',       'Raccordement électrique'),
    ('evacuation', 'Évacuation et extraction'),
    ('couverts',   'Capacité en couverts'),
    ('dimensions', 'Dimensions hors tout'),
    ('poids',      'Poids'),
    ('mobilite',   'Mobilité et mode de pose'),
    ('graisses',   'Récupération des graisses'),
    ('conformite', 'Conformité déclarée par le fabricant'),
    ('garantie',   'Garantie constructeur'),
    ('pieces',     'Disponibilité des pièces détachées'),
    ('montage',    'Montage et mise en service'),
    ('condition',  'Conditionnement et emballage'),
    ('matiere',    'Matière et composition'),
    ('calibre',    'Calibre et granulométrie'),
    ('humidite',   'Taux d’humidité'),
    ('compat',     'Compatibilité appareil'),
]

# ---------------------------------------------------------------------------
# LES CATEGORIES.
#   (famille, energie, nom, [segments], description, [champs])
# ---------------------------------------------------------------------------
CATEGORIES = [

    # --- Barbecues ----------------------------------------------------------
    ('barbecues', 'gaz', 'Barbecue au gaz sur chariot',
     ['particulier', 'revente', 'traiteur'],
     'Le format dominant du marché grand public. Le nombre de brûleurs et la '
     'possibilité de zones de chaleur séparées décident de ce qu’on peut '
     'réellement cuire dessus.',
     ['surface', 'bruleurs', 'puissance', 'allumage', 'grille', 'corps',
      'gaz', 'mobilite', 'graisses', 'garantie', 'pieces', 'montage']),

    ('barbecues', 'gaz', 'Barbecue au gaz encastrable',
     ['particulier', 'revente'],
     'Bloc de cuisson destiné à être intégré dans un îlot maçonné. La découpe '
     'et les distances de sécurité se valident avant les travaux, pas après.',
     ['surface', 'bruleurs', 'puissance', 'allumage', 'grille', 'corps',
      'gaz', 'dimensions', 'montage', 'conformite', 'garantie']),

    ('barbecues', 'gaz', 'Barbecue au gaz portable',
     ['particulier', 'traiteur', 'revente'],
     'Petit appareil nomade sur cartouche ou petite bouteille. Le poids et le '
     'système de verrouillage du couvercle font la différence à l’usage.',
     ['surface', 'bruleurs', 'puissance', 'allumage', 'grille', 'gaz',
      'poids', 'mobilite', 'condition', 'garantie']),

    ('barbecues', 'charbon', 'Barbecue au charbon à cuve ronde',
     ['particulier', 'revente'],
     'Le classique à couvercle, adapté à la cuisson directe comme indirecte. '
     'La qualité des aérations pilote toute la maîtrise de la température.',
     ['surface', 'grille', 'corps', 'regulation', 'graisses', 'mobilite',
      'poids', 'garantie', 'pieces']),

    ('barbecues', 'charbon', 'Barbecue au charbon rectangulaire',
     ['particulier', 'traiteur', 'restauration'],
     'Foyer allongé, souvent à hauteur de grille réglable. Format préféré dès '
     'qu’il faut cuire beaucoup de pièces en série.',
     ['surface', 'grille', 'corps', 'regulation', 'graisses', 'dimensions',
      'mobilite', 'garantie']),

    ('barbecues', 'charbon', 'Barbecue céramique',
     ['particulier', 'restauration', 'revente'],
     'Cuve épaisse en céramique, très inerte thermiquement : elle tient une '
     'température basse longtemps et monte aussi très haut. Deux usages dans '
     'un seul appareil.',
     ['surface', 'grille', 'corps', 'isolation', 'plage', 'regulation',
      'poids', 'mobilite', 'garantie', 'pieces']),

    ('barbecues', 'electrique', 'Barbecue électrique de table',
     ['particulier', 'revente'],
     'Appareil d’appoint pour balcon et intérieur, là où la flamme est '
     'interdite. Le raccordement et la puissance disponible sur la prise sont '
     'la vraie contrainte.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'grille',
      'graisses', 'poids', 'conformite', 'garantie']),

    ('barbecues', 'electrique', 'Barbecue électrique sur pied',
     ['particulier', 'collectivite', 'revente'],
     'Version sur chariot, souvent retenue en copropriété et en résidence où '
     'le gaz et le charbon sont proscrits par le règlement.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'grille',
      'corps', 'mobilite', 'conformite', 'garantie']),

    ('barbecues', 'bois', 'Barbecue à granulés',
     ['particulier', 'restauration', 'revente'],
     'Alimentation automatique en granulés et régulation électronique. '
     'Combine la fumée du bois et la constance d’un four — mais il faut du '
     'courant.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'grille',
      'isolation', 'graisses', 'pieces', 'garantie', 'montage']),

    ('barbecues', 'mixte', 'Barbecue multi-énergie',
     ['particulier', 'traiteur', 'restauration'],
     'Appareil combinant deux modes de chauffe, gaz et charbon le plus '
     'souvent. Vendu sur la polyvalence : à vérifier que chaque mode est '
     'réellement exploitable, pas juste présent.',
     ['surface', 'bruleurs', 'puissance', 'gaz', 'grille', 'corps',
      'regulation', 'mobilite', 'garantie', 'pieces']),

    # --- Grils professionnels -----------------------------------------------
    ('grils', 'charbon', 'Gril professionnel à charbon',
     ['restauration', 'collectivite'],
     'Appareil de production continue en cuisine ouverte. L’extraction et le '
     'traitement des fumées conditionnent l’autorisation d’exploiter autant '
     'que l’appareil lui-même.',
     ['surface', 'corps', 'grille', 'regulation', 'evacuation', 'couverts',
      'dimensions', 'graisses', 'conformite', 'pieces']),

    ('grils', 'gaz', 'Gril professionnel à gaz',
     ['restauration', 'collectivite'],
     'Gril de ligne de cuisson, à grille nue ou rainurée. Se dimensionne au '
     'nombre de couverts au coup de feu, pas au nombre de couverts du service.',
     ['surface', 'bruleurs', 'puissance', 'gaz', 'grille', 'corps',
      'evacuation', 'couverts', 'graisses', 'conformite', 'pieces']),

    ('grils', 'gaz', 'Gril à pierre de lave',
     ['restauration'],
     'Le rayonnement passe par un lit de pierres, ce qui adoucit la chauffe et '
     'donne un goût caractéristique. Les pierres sont un consommable.',
     ['surface', 'bruleurs', 'puissance', 'gaz', 'grille', 'evacuation',
      'graisses', 'pieces', 'conformite']),

    ('grils', 'mixte', 'Salamandre de finition',
     ['restauration', 'collectivite'],
     'Chauffe par le haut, pour gratiner et finir une assiette. Se juge sur la '
     'rapidité de montée et sur le réglage de la hauteur.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'gaz',
      'dimensions', 'conformite', 'garantie']),

    ('grils', 'electrique', 'Gril de contact et panini',
     ['restauration', 'collectivite', 'revente'],
     'Cuisson entre deux plaques, lisses ou rainurées. Appareil de débit : la '
     'remontée en température entre deux cuissons est le vrai critère.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'grille',
      'graisses', 'poids', 'conformite', 'garantie']),

    ('grils', 'mixte', 'Rôtissoires et tournebroches',
     ['restauration', 'traiteur', 'revente'],
     'Cuisson à la broche, en vitrine ou en arrière-cuisine. Le nombre de '
     'broches et la récupération des jus organisent tout le poste.',
     ['puissance', 'plage', 'regulation', 'elec', 'gaz', 'couverts',
      'dimensions', 'graisses', 'conformite', 'pieces']),

    ('grils', 'charbon', 'Gril à broche verticale',
     ['restauration', 'traiteur'],
     'Broche verticale devant un foyer, pour la cuisson en continu de grandes '
     'pièces. Poste très spécialisé, très rentable quand il tourne.',
     ['puissance', 'regulation', 'gaz', 'elec', 'corps', 'evacuation',
      'graisses', 'dimensions', 'pieces']),

    ('grils', 'charbon', 'Gril compact à charbon de bois',
     ['restauration', 'traiteur'],
     'Petit foyer de comptoir pour brochettes et petites pièces, à hauteur de '
     'client. Très demandé en restauration de rue et en service au comptoir.',
     ['surface', 'corps', 'grille', 'regulation', 'evacuation', 'dimensions',
      'mobilite', 'pieces']),

    # --- Fumoirs ------------------------------------------------------------
    ('fumoirs', 'bois', 'Fumoir décalé à foyer latéral',
     ['particulier', 'restauration', 'traiteur'],
     'Foyer séparé de la chambre de cuisson, pour une fumée indirecte et une '
     'cuisson longue. L’épaisseur de l’acier décide de la stabilité en '
     'température.',
     ['surface', 'corps', 'isolation', 'plage', 'regulation', 'grille',
      'poids', 'dimensions', 'pieces', 'garantie']),

    ('fumoirs', 'charbon', 'Fumoir vertical à bac d’eau',
     ['particulier', 'revente'],
     'Colonne compacte avec réserve d’eau qui stabilise la température. '
     'Format d’entrée de gamme le plus efficace pour la cuisson lente.',
     ['surface', 'corps', 'plage', 'regulation', 'grille', 'graisses',
      'poids', 'garantie', 'pieces']),

    ('fumoirs', 'electrique', 'Fumoir électrique',
     ['particulier', 'restauration', 'collectivite'],
     'Résistance et générateur de fumée pilotés électroniquement. Retenu là '
     'où la flamme nue est interdite ou la surveillance impossible.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'isolation',
      'grille', 'conformite', 'garantie', 'pieces']),

    ('fumoirs', 'bois', 'Fumoir à granulés',
     ['particulier', 'restauration'],
     'Alimentation automatique et régulation fine, pour des cuissons de '
     'plusieurs heures sans surveillance. Consommable dédié.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'isolation',
      'grille', 'pieces', 'garantie']),

    ('fumoirs', 'aucune', 'Fumoir à froid et générateurs de fumée',
     ['particulier', 'restauration', 'traiteur'],
     'Fumage sans cuisson, pour le poisson, le fromage et la charcuterie. '
     'Contrainte principale : maintenir la chambre en dessous du seuil de '
     'cuisson.',
     ['surface', 'corps', 'plage', 'dimensions', 'compat', 'pieces', 'condition']),

    ('fumoirs', 'mixte', 'Armoire de fumage professionnelle',
     ['restauration', 'collectivite'],
     'Enceinte de production avec chariots, sondes et cycles programmables. '
     'Équipement d’atelier, à traiter comme un investissement de process.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'isolation',
      'evacuation', 'couverts', 'conformite', 'pieces', 'montage']),

    ('fumoirs', 'aucune', 'Accessoires de fumage',
     ['particulier', 'restauration', 'revente'],
     'Tubes, labyrinthes, paniers et boîtes à fumée transformant un appareil '
     'existant en fumoir d’appoint. Compatibilité à vérifier appareil par '
     'appareil.',
     ['matiere', 'dimensions', 'compat', 'condition', 'pieces']),

    ('fumoirs', 'bois', 'Barbecue-fumoir combiné',
     ['particulier', 'traiteur'],
     'Appareil unique assurant grillade directe et fumage indirect. Compromis '
     'assumé : il fait les deux, aucun des deux parfaitement.',
     ['surface', 'corps', 'isolation', 'plage', 'regulation', 'grille',
      'graisses', 'mobilite', 'garantie']),

    # --- Planchas -----------------------------------------------------------
    ('planchas', 'gaz', 'Plancha au gaz',
     ['particulier', 'restauration', 'traiteur'],
     'Plaque pleine chauffée par brûleurs, pour une cuisson par conduction. '
     'Le matériau et l’épaisseur de la plaque comptent plus que la puissance.',
     ['surface', 'bruleurs', 'puissance', 'gaz', 'grille', 'plage',
      'regulation', 'graisses', 'mobilite', 'garantie']),

    ('planchas', 'electrique', 'Plancha électrique',
     ['particulier', 'restauration', 'collectivite'],
     'Version raccordée au réseau, souvent en intérieur. La régulation par '
     'zones évite d’avoir à déplacer les pièces en cours de cuisson.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'grille',
      'graisses', 'conformite', 'garantie']),

    ('planchas', 'gaz', 'Plancha encastrable',
     ['particulier', 'restauration'],
     'Plaque intégrée dans un plan de travail ou un îlot. La ventilation sous '
     'le plan et l’évacuation des graisses se prévoient à la conception.',
     ['surface', 'bruleurs', 'puissance', 'gaz', 'dimensions', 'grille',
      'graisses', 'montage', 'conformite']),

    ('planchas', 'electrique', 'Teppanyaki professionnel',
     ['restauration', 'traiteur'],
     'Grande plaque lisse de cuisson devant le client. Le poste est autant un '
     'spectacle qu’un équipement : l’extraction doit être irréprochable.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'grille',
      'evacuation', 'dimensions', 'conformite', 'montage']),

    ('planchas', 'mixte', 'Plaque à snacker rainurée',
     ['restauration', 'collectivite'],
     'Plaque à rainures pour marquer la pièce tout en cuisant par conduction. '
     'Équipement de ligne, choisi pour le rendement.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'gaz',
      'grille', 'graisses', 'conformite']),

    ('planchas', 'aucune', 'Chariots et supports de plancha',
     ['particulier', 'traiteur', 'revente'],
     'Bâti, desserte et rangement associés à la plaque. Vendus séparément, '
     'donc à apparier explicitement avec le modèle de plancha.',
     ['dimensions', 'corps', 'mobilite', 'poids', 'compat', 'montage', 'condition']),

    # --- Fours --------------------------------------------------------------
    ('fours', 'bois', 'Four à pizza au bois',
     ['particulier', 'restauration', 'traiteur'],
     'Sole réfractaire et voûte, chauffés par un feu latéral. La masse '
     'thermique décide du nombre de pizzas enchaînables, pas la taille de la '
     'bouche.',
     ['surface', 'corps', 'isolation', 'plage', 'evacuation', 'poids',
      'dimensions', 'montage', 'pieces']),

    ('fours', 'gaz', 'Four à pizza au gaz',
     ['restauration', 'traiteur'],
     'Même principe, chauffe maîtrisée et montée en température rapide. '
     'Souvent préféré en service continu pour la régularité.',
     ['surface', 'puissance', 'gaz', 'plage', 'regulation', 'isolation',
      'evacuation', 'dimensions', 'conformite', 'pieces']),

    ('fours', 'electrique', 'Four à pizza électrique',
     ['restauration', 'collectivite', 'revente'],
     'Four à sole et voûte séparément régulées. Retenu quand l’évacuation des '
     'fumées est impossible ou trop coûteuse.',
     ['surface', 'puissance', 'plage', 'regulation', 'elec', 'isolation',
      'dimensions', 'conformite', 'garantie']),

    ('fours', 'charbon', 'Four tandoor',
     ['restauration', 'traiteur'],
     'Cuve verticale à cuisson par rayonnement sur les parois. Poste très '
     'spécifique, à traiter avec son extraction dédiée.',
     ['corps', 'isolation', 'plage', 'evacuation', 'dimensions', 'poids',
      'conformite', 'pieces']),

    ('fours', 'bois', 'Four de cuisson extérieure multifonction',
     ['particulier', 'traiteur'],
     'Four extérieur assurant pizza, pain et rôtissage. Vendu avec son abri '
     'et son conduit : l’installation fait partie du produit.',
     ['surface', 'corps', 'isolation', 'plage', 'evacuation', 'poids',
      'dimensions', 'montage', 'garantie']),

    ('fours', 'bois', 'Brasero-plancha à foyer central',
     ['particulier', 'traiteur', 'revente'],
     'Foyer ouvert entouré d’une couronne de cuisson en acier. Objet de '
     'convivialité autant qu’appareil de cuisson.',
     ['surface', 'corps', 'grille', 'plage', 'graisses', 'poids',
      'dimensions', 'montage', 'garantie']),

    ('fours', 'electrique', 'Fours de remise en température',
     ['collectivite', 'traiteur', 'restauration'],
     'Maintien et remise en température des préparations avant service. '
     'Équipement de liaison chaude, encadré côté hygiène.',
     ['puissance', 'plage', 'regulation', 'elec', 'isolation', 'couverts',
      'dimensions', 'conformite', 'garantie']),

    # --- Cuisine exterieure -------------------------------------------------
    ('exterieur', 'aucune', 'Îlots et modules de cuisine extérieure',
     ['particulier', 'revente'],
     'Structures modulaires recevant plaque, gril et rangement. Le plan de '
     'calepinage se valide avant commande : les modules ne se recoupent pas.',
     ['dimensions', 'corps', 'matiere', 'compat', 'montage', 'condition', 'garantie']),

    ('exterieur', 'aucune', 'Éviers et modules techniques extérieurs',
     ['particulier', 'restauration'],
     'Point d’eau, évacuation et rangement humide au plus près du poste de '
     'cuisson. L’alimentation et la vidange se prévoient au gros œuvre.',
     ['dimensions', 'corps', 'matiere', 'montage', 'compat', 'garantie']),

    ('exterieur', 'aucune', 'Plans de travail et dessertes',
     ['particulier', 'traiteur', 'revente'],
     'Surfaces de préparation, chariots et tables d’appoint. La tenue aux UV '
     'et au gel discrimine les matériaux plus que l’aspect.',
     ['dimensions', 'matiere', 'corps', 'mobilite', 'poids', 'montage', 'condition']),

    ('exterieur', 'aucune', 'Abris et auvents de zone de cuisson',
     ['particulier', 'restauration', 'traiteur'],
     'Couverture du poste extérieur. Attention aux distances de sécurité avec '
     'les appareils à flamme : c’est une contrainte, pas une option.',
     ['dimensions', 'matiere', 'montage', 'compat', 'conformite', 'garantie']),

    ('exterieur', 'bois', 'Braseros et foyers d’agrément',
     ['particulier', 'traiteur', 'revente'],
     'Foyers ouverts destinés au chauffage et à l’ambiance, parfois équipés '
     'd’une grille. Réglementation locale à vérifier avant l’installation.',
     ['corps', 'matiere', 'dimensions', 'poids', 'evacuation', 'mobilite', 'condition']),

    ('exterieur', 'aucune', 'Mobilier et assises de zone repas',
     ['particulier', 'restauration', 'revente'],
     'Tables, bancs et tabourets de l’espace cuisson. Nettoyabilité et tenue '
     'à l’extérieur avant l’esthétique.',
     ['dimensions', 'matiere', 'poids', 'mobilite', 'condition', 'garantie']),

    ('exterieur', 'aucune', 'Housses et protections',
     ['particulier', 'revente'],
     'Bâches ajustées, housses respirantes et protections d’hivernage. '
     'Article de rechat régulier, donc de marge — à condition de tenir la '
     'compatibilité à jour.',
     ['dimensions', 'matiere', 'compat', 'condition', 'garantie']),

    # --- Accessoires --------------------------------------------------------
    ('accessoires', 'aucune', 'Ustensiles de cuisson',
     ['particulier', 'restauration', 'revente'],
     'Pinces, spatules, fourchettes et pinceaux. Article d’attachement : '
     'longueur du manche et tenue de la soudure font toute la différence.',
     ['matiere', 'dimensions', 'poids', 'condition', 'garantie']),

    ('accessoires', 'aucune', 'Thermomètres et sondes',
     ['particulier', 'restauration', 'collectivite'],
     'Sondes à cœur, thermomètres de chambre et systèmes sans fil. En '
     'restauration, l’enregistrement des relevés fait partie du dossier '
     'hygiène.',
     ['plage', 'elec', 'compat', 'dimensions', 'conformite', 'garantie']),

    ('accessoires', 'aucune', 'Grilles et surfaces de cuisson d’appoint',
     ['particulier', 'restauration', 'revente'],
     'Grilles de rechange, plaques, pierres et surfaces spéciales. Le premier '
     'critère est la compatibilité exacte avec l’appareil.',
     ['matiere', 'dimensions', 'grille', 'compat', 'poids', 'condition']),

    ('accessoires', 'aucune', 'Paniers, broches et supports',
     ['particulier', 'restauration', 'traiteur'],
     'Accessoires de maintien : paniers à légumes, supports à volaille, '
     'broches et pinces à poisson. Vendus par usage, pas par appareil.',
     ['matiere', 'dimensions', 'compat', 'condition', 'poids']),

    ('accessoires', 'aucune', 'Textile et protection de l’opérateur',
     ['particulier', 'restauration', 'collectivite'],
     'Gants résistants à la chaleur, tabliers et manchettes. En usage '
     'professionnel, cela relève de l’équipement de protection.',
     ['matiere', 'plage', 'dimensions', 'conformite', 'condition']),

    ('accessoires', 'aucune', 'Allumage et démarrage',
     ['particulier', 'traiteur', 'revente'],
     'Cheminées d’allumage, souffleurs et allumeurs. Consommable et matériel '
     'se vendent ensemble ; c’est un panier moyen facile à monter.',
     ['matiere', 'dimensions', 'elec', 'compat', 'condition']),

    ('accessoires', 'aucune', 'Rangement et transport',
     ['particulier', 'traiteur', 'revente'],
     'Mallettes, sacoches et supports d’ustensiles. Article de saison, très '
     'lié à l’offre cadeau.',
     ['matiere', 'dimensions', 'poids', 'condition', 'compat']),

    ('accessoires', 'electrique', 'Petits appareils d’appoint',
     ['particulier', 'restauration', 'revente'],
     'Ventilateurs de foyer, tournebroches motorisés et appareils à couper. '
     'Raccordement et sécurité électrique à déclarer.',
     ['puissance', 'elec', 'compat', 'dimensions', 'conformite', 'garantie']),

    # --- Combustibles -------------------------------------------------------
    ('combustibles', 'charbon', 'Charbon de bois',
     ['particulier', 'restauration', 'revente'],
     'Le combustible de référence du gril. L’essence d’origine et le calibre '
     'décident du temps de chauffe et de la tenue de la braise.',
     ['matiere', 'calibre', 'humidite', 'condition', 'compat']),

    ('combustibles', 'charbon', 'Briquettes',
     ['particulier', 'restauration', 'revente'],
     'Combustible reconstitué à combustion plus longue et plus régulière que '
     'le charbon en morceaux. Choix de production, pas de puriste.',
     ['matiere', 'calibre', 'humidite', 'condition', 'compat']),

    ('combustibles', 'bois', 'Granulés de cuisson',
     ['particulier', 'restauration', 'revente'],
     'Granulés alimentaires dédiés aux appareils à vis sans fin. Ne pas '
     'confondre avec les granulés de chauffage : l’essence et les additifs '
     'diffèrent.',
     ['matiere', 'calibre', 'humidite', 'condition', 'compat']),

    ('combustibles', 'bois', 'Copeaux et bois de fumage',
     ['particulier', 'restauration', 'traiteur'],
     'Copeaux, morceaux et planchettes, par essence. C’est l’essence qui fait '
     'le goût — le référencement se fait donc essence par essence.',
     ['matiere', 'calibre', 'humidite', 'condition', 'compat']),

    ('combustibles', 'aucune', 'Allume-feu et aides à l’allumage',
     ['particulier', 'revente'],
     'Cubes, gels et laine de bois. Produit d’achat d’impulsion, à placer au '
     'plus près du combustible.',
     ['matiere', 'condition', 'conformite', 'compat']),

    ('combustibles', 'aucune', 'Pierres de lave et réfractaires',
     ['restauration', 'revente'],
     'Consommable des grils à pierre et des fours. Se remplace à intervalle '
     'régulier, ce qui en fait un revenu récurrent.',
     ['matiere', 'calibre', 'dimensions', 'compat', 'condition']),

    # --- Pieces detachees ---------------------------------------------------
    ('pieces', 'gaz', 'Brûleurs et rampes gaz',
     ['restauration', 'revente', 'particulier'],
     'Pièce d’usure principale d’un appareil à gaz. La référence exacte du '
     'modèle et l’année de fabrication sont indispensables pour ne pas se '
     'tromper.',
     ['matiere', 'dimensions', 'gaz', 'compat', 'conformite', 'condition']),

    ('pieces', 'aucune', 'Grilles et diffuseurs de rechange',
     ['particulier', 'restauration', 'revente'],
     'Grilles, barres de vaporisation et déflecteurs. Le stock de rechange '
     'conditionne la durée de vie utile de tout le parc installé.',
     ['matiere', 'dimensions', 'grille', 'compat', 'condition']),

    ('pieces', 'electrique', 'Thermostats, sondes et allumages',
     ['restauration', 'revente'],
     'Composants de régulation et d’allumage. La panne la plus fréquente sur '
     'les appareils électroniques, et la plus simple à traiter avec du stock.',
     ['elec', 'plage', 'compat', 'conformite', 'dimensions', 'condition']),

    ('pieces', 'gaz', 'Détendeurs, flexibles et raccords',
     ['particulier', 'restauration', 'revente'],
     'Organes de sécurité soumis à date de péremption. À traiter comme du '
     'matériel réglementé, jamais comme un accessoire.',
     ['gaz', 'dimensions', 'matiere', 'compat', 'conformite', 'condition']),

    ('pieces', 'aucune', 'Bacs à graisse et pièces de cuve',
     ['particulier', 'restauration', 'revente'],
     'Bacs, tiroirs, cendriers et pièces de carrosserie. Peu valorisés, mais '
     'ce sont eux qui décident si l’appareil reste utilisable.',
     ['matiere', 'dimensions', 'graisses', 'compat', 'condition']),

    ('pieces', 'aucune', 'Roues, poignées et quincaillerie',
     ['particulier', 'revente'],
     'Petites pièces mécaniques d’un appareil mobile. Référencement pénible, '
     'mais c’est ce qui fait la différence d’un service après-vente.',
     ['matiere', 'dimensions', 'compat', 'condition']),

    # --- Entretien ----------------------------------------------------------
    ('entretien', 'aucune', 'Produits de nettoyage',
     ['particulier', 'restauration', 'collectivite'],
     'Dégraissants de grille, de cuve et de plaque. En restauration, le '
     'contact alimentaire des produits doit être déclaré.',
     ['matiere', 'condition', 'conformite', 'compat']),

    ('entretien', 'aucune', 'Brosses et outils de nettoyage',
     ['particulier', 'restauration', 'revente'],
     'Brosses, raclettes et grattoirs. Les brosses métalliques posent une '
     'vraie question de sécurité alimentaire — à arbitrer explicitement.',
     ['matiere', 'dimensions', 'compat', 'condition', 'conformite']),

    ('entretien', 'gaz', 'Sécurité gaz et détection',
     ['restauration', 'collectivite', 'particulier'],
     'Détecteurs, coupures d’urgence et contrôle d’étanchéité. Relève de '
     'l’obligation d’exploitation, pas du confort.',
     ['gaz', 'elec', 'dimensions', 'conformite', 'compat', 'garantie']),

    ('entretien', 'aucune', 'Protection incendie du poste',
     ['restauration', 'collectivite'],
     'Couverture anti-feu, extincteur adapté aux graisses et signalétique du '
     'poste de cuisson. Contrôlé lors des visites de conformité.',
     ['matiere', 'dimensions', 'conformite', 'condition', 'garantie']),

    ('entretien', 'aucune', 'Traitement et entretien des surfaces',
     ['particulier', 'restauration', 'revente'],
     'Huiles de culottage, protections antirouille et produits d’hivernage. '
     'Consommable saisonnier à forte rotation.',
     ['matiere', 'condition', 'compat', 'conformite']),
]

# ---------------------------------------------------------------------------
# CE QU'UNE FICHE FABRICANT DOIT CONTENIR. Le brief demandait « présentation
# des fabricants ». Aucun n'est nomme. Ce sont les cases a remplir.
# ---------------------------------------------------------------------------
FICHE_FABRICANT = [
    ('Pays de fabrication et pays d’assemblage',
     'Deux informations distinctes, souvent confondues. Elles décident du '
     'régime douanier et de ce qu’on a le droit d’écrire sur l’étiquette.'),
    ('Conformité déclarée et documents disponibles',
     'Le fabricant déclare, sur son dossier. Un distributeur qui affirme la '
     'conformité à sa place engage sa propre responsabilité.'),
    ('Politique de pièces détachées et durée d’engagement',
     'Combien d’années le fabricant s’engage à fournir les pièces. C’est le '
     'critère qui sépare un appareil d’un consommable coûteux.'),
    ('Garantie, périmètre et exclusions',
     'La durée seule ne dit rien. Ce qui compte est ce qui est couvert, et ce '
     'qui saute à la première utilisation professionnelle.'),
    ('Politique de quantité minimale et de conditionnement',
     'Quantité minimale, palettisation et unité de commande. Le champ existe ; '
     'aucune valeur n’est écrite ici.'),
    ('Restrictions territoriales de distribution',
     'Un fabricant accorde rarement un territoire ouvert. À clarifier avant '
     'de construire une gamme autour de lui.'),
]

# ---------------------------------------------------------------------------
# APPROVISIONNEMENT ET DISTRIBUTION. Le brief le demande : on decrit les
# etapes, sans aucun delai ni volume.
# ---------------------------------------------------------------------------
CHAINE = [
    ('Sourcing et sélection',
     'Identification des fabricants, vérification de leur capacité à fournir '
     'la documentation, et essai sur échantillon avant tout engagement.'),
    ('Conformité et documentation',
     'Rassemblement des déclarations, notices et marquages exigés sur le '
     'marché visé. Les appareils à gaz et électriques sont réglementés ; '
     'l’absence d’un document bloque la mise en vente, pas la livraison.'),
    ('Import et dédouanement',
     'Classement tarifaire, documents d’origine et contrôles à l’arrivée. '
     'Un classement erroné se paie longtemps après.'),
    ('Stockage et préparation',
     'Réception, contrôle des emballages, constitution des assortiments et '
     'préparation des palettes de revente.'),
    ('Distribution',
     'Vente directe, revente à des détaillants, et fourniture aux cuisines '
     'professionnelles. Trois circuits qui n’ont ni les mêmes marges ni les '
     'mêmes obligations.'),
    ('Service après-vente et pièces',
     'Stock de pièces d’usure, traitement des retours et suivi des garanties. '
     'C’est là que se joue la deuxième vente.'),
]

NOTE = (
    'Chaque carte est une CATÉGORIE d’équipement, pas une référence en stock. '
    'Elle indique ce que la catégorie regroupe, l’énergie qu’elle utilise, les '
    'segments auxquels elle s’adresse, et la grille de champs sur laquelle '
    'deux appareils de cette catégorie se comparent. Le segment est un axe à '
    'part entière : un barbecue de jardin et un gril de brasserie ne se '
    'vendent pas au même client, ne s’installent pas dans les mêmes '
    'conditions et ne sont pas soumis aux mêmes obligations. Les mélanger '
    'dans une liste à plat fait perdre son temps aux deux acheteurs.'
)

AVERTISSEMENT = (
    'Le brief demandait une présentation des fabricants. Aucun fabricant '
    'n’est nommé sur cette page. Citer une marque sans accord de distribution '
    'est un problème juridique, et afficher des marques qu’on ne distribue pas '
    'trompe l’acheteur ; la page dit donc ce qu’une fiche fabricant doit '
    'contenir, sans en remplir une seule. Aucune valeur chiffrée non plus : '
    'pas de puissance, pas de surface de cuisson, pas de température, pas de '
    'nombre de brûleurs, pas de poids, pas de prix, pas de quantité minimale, '
    'pas de délai. Ce sont des noms de champs. Et aucune conformité n’est '
    'affirmée : le gaz et l’électrique sont réglementés, « conforme » est une '
    'déclaration que seul le fabricant peut faire, avec son dossier.'
)
