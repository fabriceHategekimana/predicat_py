# Predicat
C'est un outil pour représenter l'information sous la forme de fait et de graphe avec un peu de logique.

# Qu'est ce qu'on peut faire?

1. Créer des faits
2. Poser des questions
3. Créer des règles

----

# Syntaxe du LS faits

## prédicats à deux expressions
	[sujet] [lien] [verbe]

## exemple
Pour dire "Socrate est un homme":  
```bash
|normal> Socrate est homme
```

----

# Syntaxe du LS requête(1)

## principe
Même structure que les faits mais avec l'utilisation de variables

## variables réservées
A, B, C
Pas plus de `deux` variables par fait.

----

# Syntaxe du LS requête(2)

## Cas 1
check **A** est homme = "**Qui** est un homme?"

## Cas 2
check Socrate **A** homme = "**Quel relation** Socrate a avec 'homme'?"

## Cas 3
check Socrate est **A** = "**Qu'est-ce qu**'est Socrate?"

----

# Autres questions: 2 variables
## Cas 4
check **A B** homme = "**Qu'est-ce qui est relier à **'homme'?"

## Cas 5
check Socrate **A B** = "**Qu'est ce qu'on dit sur** Socrate?"

## Cas 6
check **A** est **B** = "**Qu'est-ce qui** 'est' **quoi?**"

----

# Syntaxe LS règles

## Syntax
add `if` [conditions] `then` [conclusions]

## exemple
Pour donner la règle "Tout les hommes sont mortels":  
```bash
	|normal> add if A est homme then A est mortel
```

# Getting started
This is actually a python project. You just have to run:
```bash
python cli.py
```

## Commands
### add
1) Vous pouvez ajouter des faits simples comme:  
```bash
add Jean ami Pierre 
```
Qui veut dire "Jean est ami avec Pierre".  

2)Vous pouvez ajouter simplement des règles comme:
```bash
add if A ami B then B ami A
```
Qui veut dire "Si A est un ami de B, alors B est ami avec A" (pour créer une relation bidirectionnelle à toute amitié).

### check 
1) Le check permet d'interrogé la base de fait et de règles préalablement établis. On peut enfait combiner plusieurs fait contenant des variables avec des "and" pour demander des choses plus précises.  
Vous pouvez poser des question pour savoir des choses:
```bash
check A parent Louis and A frere Lisa
```
Qui veut dire, "Regarde si quelqu'un qui est le parent de Loui et le frère de Lisa."

2) Le check permet aussi de visualisé toutes les règles créées avec:
```bash
check rules
```

3) Le check permet des requêtes plus avancés divisé en trois parties:
check [relation] filter [filter] get [get]
- relation: Les requêtes sur les relations: C'est des fait avec variables composés avec des "and"
- filter (optionnel): Les filtrages sur les variables 
- get (optionnel):  Les variables qui vont être affichées

Exemple:
Pour chercher les amis de Sylvie qui ont plus de 20 ans:
```bash
check A ami Sylvie and A age B filter B > 20 get A
```

### Delete 
Suit la même forme que check, sauf qu'il supprime les données s'il les trouve.
Le delete permet aussi de supprimer les règles grâce à leur identifiant numérique:
```bash
delete rules 1 3 4
```
Pour dire "supprime les règles 1, 3 et 4" 

### Display 
Suit la même forme que check, sauf qu'il affiche les données sous la forme d'un graphe sur votre navigateur.  

### Clear
Permet de supprimer tout les faits présents dans la base de donnée pour reprendre sur une nouvelle base.  
```bash
delete rules 1 3 4
```
Attention, pas de retour en arrière. Malheureusement, il faudra supprimer les règle manuellement (mais normalement il n'y en a pas beaucoup).  

### export
Permet d'exporter nos faits dans un fichier csv de notre choix
```bash
export to csv personnages.csv
```
Va exporter tout les faits qu'on a actuellement dans la base sous la forme de csv

### import
Permet d'importer nos faits depuis un fichier csv de notre choix
```bash
import sauvegarde/personnages.csv
```
Va importer le ficher "personnages.csv" présent dans le dossier "sauvegarde".
Pour l'instant le fichier csv doit être en 3 colonnes et doit avoir "subject,link,goal" en entête.

