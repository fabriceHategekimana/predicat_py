# Delete
Commande qui va supprimer des entités de la [base_de_donnée](base_de_donnée)
## format:
delete [entités](values) [contenu](contenu)

## algo
- recevoir la commande (en enlevant le "delete")
- faire un [f_typeof](f_typeof)() selon les cas:
	- set:
		- faire un [f_setToSQL](f_setToSQL)() pour obtenir une commande SQL
		- faire un [f_SQLToArray](f_SQLToArray)() pour obtenir un tableau de la base de donnée
		- faire un [f_arrayToFact](f_arrayToFact)() pour obtenir une liste de fait
		- pour chaque fait, faire un [f_deleteFact](f_deleteFact)()
	- node:
		- faire un query [nom] A B et A B [nom]
		- pour chaque élément faire un [f_deleteFact](f_deleteFact)()
	- link:
		- faire un query A [nom] B
		- pour chaque fait faire un [f_deleteFact](f_deleteFact)()
