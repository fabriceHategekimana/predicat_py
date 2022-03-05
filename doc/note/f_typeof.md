# Fonction typeof

évalue le type de la donnée rentrée

Fait appel à l'algorithme de reconnaissance:

----
entree: entité et variable
sortie: type d'entité
----


- on évalue et le parser s'en charge
- types possibles:
	- entités:
		- fact
		- rule
		- node
		- link
		- set
	- variable:
		- on récupère le contenu par une query [nom] _let A
		- on refait un typeof
	- autre:
		- text
		- image
		- vidéo
		- musique
		- lien
		- script
		- unknow
