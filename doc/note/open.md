# open

Ouvre un script qui contient du code écrit en prédicat
une fonction/commande eval n'est jamais recommandée. Elle est surtout là pour stocker des valeurs pour la suite et de pouvoir exécuter des script

## syntaxe
eval contenu

- selon le type de contenu:
	- entité
	- variable (on évalue le reste)
	- si c'est un autre type:
		- text: récupérer les éléments textuels
		- image: ouvrir avec un lecteur d'image
		- vidéo: ouvrir avec un lecteur de vidéo
		- musique: ouvrir avec un lecteur musical
		- lien: ouvrir avec un browser
		- script: faire un [f_evalScript](f_evalScript)()
		- unknow: retourner un message d'erreur
