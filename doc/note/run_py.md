# Run.py
Est le module prinicipal qui "exécute" les commandes. 
TODO: graphe de hiérarchie des fonctions

## svPrint(tab)
Fait comme le print, mais affiche les données en format csv:

## run(inp)
La fonction principale du module a comportement dépenant de l'entrée.
Si l'entrée est une règle, alors on le traite comme tel et on l'enregistre.
Si l'entreée est autre, alors elle passe par le parseur.

## runRule(rest)
La fonction en charge de formater et de ranger la règle qui lui est donnée.

## removeCommands(exp)
prend une expression et remplace chaque commande par un ','

## getValueOnly(tab)
Les sets sont composé de constantes et de variables. Cette fonction enlève les variables pour garder seulement les constantes (c'est pour l'entête des règles stockées)

## filterVariables(exp)
Prend une expression, sépart chaque partie et enlève les variables.

## runCommand(inp)
Comme son nom l'indique, lance la commande donnée. La commande sera reformatée si besoin et sera parsée avant de faire appel à la fonction execute.

## execute(entry, c)
Execute prend la commande (mise sous la forme de structure de données), prend la built-in fonction correspondante pour exécuter la commande. Si ça n'existe pas, renvoi une erreur.

## getFirstWord(exp)
Comme son nom l'indique, prend une commande et prend le premier mot (ici, le nom de la commande).

## getRules(hist)
Cette fonction transforme l'historique en un groupe de règles correspondantes.

## propagation() 
On obtient l'historique des dernières actions faites et on en retire un ensemble de règles qui leur correspondent. On finit par appliquer ses règles dans un "subRun"

Algo:
prendre l'historique des commandes mises: add et delete
appeller les règles enregistrées -> expressions
exécuter les règles
fin

## subRun(inp)
Fait comme run mais n'efface pas l'historique

## syntaxSugarCommand(command)
Va "parser" des commandes raccourcies pour donner leur équivalent dans la vrai syntaxe du programme

## syntaxSugarRule(rule)
Va "parser" des règles raccourcies pour donner leur équivalent dans la vrai syntaxe du programme


# Graphe:
Fait:
investiguer sur:
- [X] runRule 
- [X] runCommand
- [X] execute

Modifier le tableau en dataframe:
- [X] VOIDENTRY
- [ ] commands.py
