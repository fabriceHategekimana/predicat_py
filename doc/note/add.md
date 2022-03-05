# Add
Commande qui va ajouter des entités à la [base_de_donnée](base_de_donnée)

## format:
add [entités](entités) [contenu](values)

## algo:

- recevoir la commande (en enlevant le "add")
- faire un [f_typeof](f_typeof)() selon les cas:
	- set:
		- faire un [f_setToSQL](f_setToSQL)() pour obtenir une commande SQL
		- faire un [f_SQLToArray](f_SQLToArray)() pour obtenir un tableau de la base de donnée
		- faire un [f_arrayToFact](f_arrayToFact)() pour obtenir une liste de fait
		- prendre le deuxième set et faire un [f_permute](f_permute)() qui nous retourne une liste de set avec les variables remplacées
		- depuis ce set, faire un [f_setToSubSet](f_setToSubSet)() pour avoir une liste de subSet
		- ajouter chaque élément de ce subSet
	- node:
		- faire un fait: "[name] _is node"
		- faire un [f_insertFact](f_insertFact)()
	- link:
		- faire un fait "_subject [link] _goal"
		- faire un [f_insertFact](f_insertFact)()

