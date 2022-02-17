# Check
Commande qui va permettre de faire des requête à la base de donnée pour obtenir des faits

query## format:
check [values](values)

- recevoir la commande (en enlevant le "check")
- faire un [f_typeof](f_typeof)() selon les cas:
	- set:
		- faire un [f_setToSQL](f_setToSQL)() pour obtenir une commande SQL
		- faire un [f_SQLToArray](f_SQLToArray)() pour obtenir un tableau de la base de donnée
		- faire un [f_arrayToFact](f_arrayToFact)() pour obtenir une liste de fait
		- printer la liste de fait
	- node:
		- sélectionner tout les noeud (subject et goal) avec une union
		- printer la table
	- link:
		- sélectionner tout les liens 
		- printer la table
