# BBQ & matériel de cuisson — équipements et accessoires

Maquette de démonstration, page unique. Barbecues au gaz, au charbon et
électriques, grils professionnels, fumoirs, planchas, fours, cuisine
extérieure, accessoires, combustibles et pièces détachées.

En ligne : https://anirudhatalmale6-alt.github.io/bbq-demo/

## Trois axes

Famille × **énergie** × **segment**.

L'énergie parce que c'est le premier filtre réel d'un acheteur : elle décide
de l'installation, de l'autorisation d'exploiter et du coût d'usage. Le
segment parce qu'un barbecue de jardin et un gril de brasserie ne se vendent
pas au même client, ne s'installent pas dans les mêmes conditions et ne sont
pas soumis aux mêmes obligations. Les mélanger dans une liste à plat fait
perdre son temps aux deux acheteurs.

## Ce que la page n'affiche pas, volontairement

**Aucun nom de fabricant.** Le brief demandait une « présentation des
fabricants ». Citer une marque sans accord de distribution est un problème
juridique, et afficher des marques qu'on ne distribue pas trompe l'acheteur.
La page dit donc ce qu'une fiche fabricant doit contenir — pays de
fabrication, conformité déclarée, engagement sur les pièces, garantie et ses
exclusions, politique de quantité minimale, restrictions territoriales — sans
en remplir une seule.

**Aucune valeur chiffrée** : ni puissance, ni surface de cuisson, ni
température, ni nombre de brûleurs, ni poids, ni prix, ni quantité minimale,
ni délai. Ce sont des noms de champs.

**Aucune conformité affirmée.** Le gaz et l'électrique sont réglementés :
« conforme » est une déclaration que seul le fabricant peut faire, avec son
dossier. Un distributeur qui l'affirme à sa place engage sa propre
responsabilité.

## Regénérer

```
cd src
python3 build.py ../index.html   # refuse de construire si une donnée est incohérente
python3 tests.py                 # 69 contrôles dans un vrai navigateur
```

### Contrôle négatif

```
python3 tests.py /chemin/page-truquee.html
```

Le mode contrôle sort en erreur si la page truquée **passe**, et n'écrit
aucune capture — pour qu'un contrôle ne puisse jamais écraser une image
livrable. Les onze règles (marque, puissance, température, dimension, poids,
brûleurs, prix, quantité minimale, délai, garantie, conformité affirmée) ont
toutes été déclenchées de cette façon.
