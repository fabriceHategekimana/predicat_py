# typeParser.py:

Le parser se charge de vérifier si l'expression entrée est valide. Il se charge ensuite de la parser pour un traitement ultérieur.

La structure de retour est de cette forme:

Pour une expression regroupant une ou plusieurs commandes.

retour= [commande0,...,commandeN]

commande: (nom_de_commande, [contenu0,...,contenuN])
contenu: (type, valeur)

C'est le parser principal de l'outil. Il prend en entrée les commandes du programme et retourne en sortie une structure de donnée plus facile à traiter dans le code.

TODO: graphe de hiérarchie des fonctions

Il y a:
- une partie pour le lexer
- une partie pour le parser
