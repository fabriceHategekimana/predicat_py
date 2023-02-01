Predicat:

Predicat is a tool that is a RDF compatible database

# Modules:
- [network](network)

[log](log)

paramètres passés dans les fonctions

Dans chaque fonctions nous avons toujours en paramètre:
- le DataFrame d'entrée
- les valeurs d'entrée

Dans la syntaxe nous pouvons entrer les valeurs dans les fonctions dans les parenthèses:
tableaux de valeurs: (val1,val2,...)
chaque valeur peut être de différent type:
- colonne (l'entrée peut être vide ou non)
- valeur:
	- nombre
	- chaine de caractère

Par là nous avons différent cas de figure

| entrée | paramètres | action          |
|--------|------------|-----------------|
| vide   | colonne    | erreur          |
| vide   | scalaire   | 1               |
| n      | colonne    | entree(colonne) |
| n      | scalaire   | liste = n       |

Ce que je veux: éviter les tuple élément


dt (asfdkjl)


| syntaxe             | value            |   |   |
|---------------------|------------------|---|---|
| CMD                 | ""               |   |   |
| CMD VAR             | string           |   |   |
| CMD contour         | string           |   |   |
| CMD NAME contour    | (string, string) |   |   |
| CMD contour contour | (string, string) |   |   |


pour check, add et delete, la valeur peut aussi être un `fait` ou un `set`
pour filter, on a le type `comparator`
pour display on a les truc de check, add et delete mais on peut aussi utiliser une variable (typé "variable") ou un élément (typé "element")
Un contour peut prendre une nouvelle expression
TODO: remplacer `element` par `NAME`
