`[lun 18 jui 2022 15:18:33 CEST]`
Utilisation de predicat pour gérer du csv
Importation du programme d'engagement de l'armée
- j'envisage un traceur de courbe
`[lun 18 jui 2022 19:20:14 CEST]`
Utilisation pour un csv sur le pinguin
après ce sera sur un csv des mes dépenses
`[lun 18 jui 2022 20:21:55 CEST]`
Idée de création de macro:
macro name "check $1 truc ..."
`[mer 20 jui 2022 01:30:21 CEST]`
Finalement fini l'implémentation du exec
C'est mieux d'utiliser les parenthèse qui donnent un certain style pour la définition d'expression

-----

exec "1 + 5"

TODO: ici on parse manuellement
`macro` incr calc "$1+1"

check A age B exec incr "B" // renvoie seulement le nouveau tableau
check A age B append "C" incr "B" // ajoute les colonnes désirées dans le tableau précédent
check A age B append "C" "hello"

----

macro get_lieux "check A lieu B select B"

exec get_lieux 

--------

append "C" "hello"
append "C;D;E" "hello;hello;hello"
append "C" nb_repos "A"

--------

macro nb_repos "check $1 engagement B filter B contains repos count"

check A type id exec nb_repos "A"

Dans la commande:
on va faire une boucle pour obtenir les résultats de chaque instances.
Si on tombe sur plusieur résultats pour un élément on duplique l'élément:
exemple
element : Fabrice; résultats: un,deux,trois on a donc:

| A       | B     |
|---------|-------|
| Fabrice | un    |
| Fabrice | deux  |
| Fabrice | trois |

Il nous reste plus qu'à concatener tout les tableau et retourner le resultat
