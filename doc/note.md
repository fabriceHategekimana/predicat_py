# Predicat:

Prédicat est un outil qui s'inspire de la logique du premier ordre.
Cet outil permet de stocker l'information sous la forme de triplet (subject, link, object). On peut donc représenté les informations sous la forme de réseau de connaissance.
Nous pouvons alors utiliser des commandes pour interroger la base, créer de nouvelles informations et simuler un système d'inférence à l'aide de règles.

Commandes:
Pour manipuler les données et la connaissance, on utilise une interface par commande:
Nous avons différentes commandes:

[Documentation](note/note.md)

Création d'alias:
en faisant:
```
alias personnes check A type personne
```
On enregistre "check A type personne" dans l'alias personnes

et en faisant
```
:personnes
```
C'est comme si on faisait: "check A type personne", en effet, cet alias sera remplacé par le terme

