# Les triplets
Le nom du programme donne un indice: les données sont stockées sous la forme de prédicat. Un prédicat est une affirmation à propos de quelque chose. Dans ce programme un prédicat prend la forme d'un triplet. Les triplets sont l'unité de base en terme de donnée. Chaque triplet est composé de trois parties:

subject link goal

### Le sujet (subject):
C'est souvent l'entité dont don veut parler qui sera le sujet de notre prédicat.

### Le lien (link):
Peut être considéré comme le "verbe" de la phrase. Sert souvent à définir ou a ajouter une information/un attribut au sujet.

### Le but (goal):
Le but peut être considéré comme l'attribut du prédicat. Ici, le but est d'ajouter une information supplémentaire au sujet.

Exemple:
Prenons une affirmation simple: "Socrate est mortel". On peut le traduire sous la forme d'un triplet pars:

Socrate est mortel

"Socrate" est le sujet, "est" est le lien et "mortel" est le but. 

On peut alors représenter quelques information de cette façon:

#### Supression d'article:
Les prédicat ne s'intéressent qu'à une structure grammatical simple. Donc les articles sont enlevés.
"Le temps est pluvieux"
temps est pluvieux

"Marc aime les pommes"
Marc aime pommes

Combinaison de triplet:
On peut combiner les triplet avec l'opérateur de conjonction "et" ("AND" dans le langage pour conserver l'anglais).

"Alice a une voiture et a une moto"
Alice a voiture AND Alice a moto

On peut coller autant de triplet qu'on veut (triplet AND triplets AND ...)


## Les requêtes
Les requêtes s'appuient aussi sur le langage des triplets pour interroger la base de donnée. C'est juste que chaque éléments d'un triplet peut être remplacé par une variable qui est une lettre en majuscule dans le langage.

Socrate est mortel
A est mortel
Socrate A mortel
Socrate est A
A B mortel
A est B
Socrate A B
A B C 

## L'union
À chaque fois que le programme tombera sur une variable, il va tenter de la complèter par les noeuds qui donne bien un triplet existant dans la base de donnée.

Si nous avons ces prédicats dans la base de donnée:
Socrate est homme
Socrate est mortel
Sylvestre est mortel
Sylvestre est chat

Et que nous posons "Socrate est quoi":
Socrate est A

Le programme nous répondra: [homme, mortel] car se sont bien les deux valeurs qui donnent des triplets existant dans la base de données lorsqu'ils remplacent la variable A.

Si on pose "Qui est un homme":
A est homme

Le programme nous répondra: [Socrate]

Bien sûr, si on pose:
A B C
Alors le programme nous retournera tous les triplet contenu dans la base

## Les requêtes composées
On peut aussi faire des requêtes composées à l'aide du connecteur "AND".

Si nous posons "Qui est mortel":
A est mortel
Alors le programme nous répondra [Socrate,Sylvestre]

Mais si nous posons "Qui est un homme et est mortel":
A est homme AND A est mortel

Le programme nous répondra seulement [Socrate] car c'est le seule qui répond aux deux criètres (homme et mortel).


