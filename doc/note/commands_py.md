# Module Commandes:

Deux type de fonctions:
- commandes
- utilitaires
- mathematiques
- test

## Commandes:
Chaque commande prend en entrée une "entry" qui est juste un tuple composé d'une entête et d'un tableau. Cette "entry" est en faite une structure qui retient en mémoire le résultat des précédentes commandes et qui est mis à jour à chaque nouvelle commande (voir la [pipeline](pipeline)). En plus de l'entrée

[check](check)(entry, value):
[add](add)(entry, value):
[delete](delete)(entry, value):
[myCsv](csv)(entry, value):
[display](display)(entry, value):
[excel](excel)(entry, value):
[myFilter](filter)(entry, value):

## utilitaires
toIntIfPossible(val):
formatColumn(x, val, columns):
setToSQL(set_fact):
getVariables(set_fact):
flatList(listoflist):
getColumn(entry, i):
createFacts(tab, columns, set_value):
removeNOTValue(x):
substitute(entry, set_values):
substitutionColumn(tab, columns, variable):
repetitionColumn(tab, columns, value):

## mathématiques
transpose(tab):
unique(flatlist):

## test
isVariable(element):
isSet(element):
