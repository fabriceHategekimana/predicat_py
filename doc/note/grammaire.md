# La grammaire

la grammaire doit être capable d'accepter les différentes [entités](values) du langage dans un premier temps.

la grammaire peut faire un pré traitement des données pour simplifier les choses.
Actuellement, le prétraitement choisi se limitera à bien organiser les "not" dans les set, car le langage est très simple.

Il faudra donc juste un type de reconnaissance du langage.

Le parseur retournera un tuple en trois partie:

(la commande, le type, la valeur)

# Ma question:
selon la simplicité du langage, est-ce qu'on pourrait déterminer les types à l'aide du lexer uniquement ? De cette façon, le parseur ne ferrait que de reconnaître les données.

# Labo

Données types:

facts:
- luc ami jean
- marc age 12
- socrate est mortel

rules:
- if A ami B then B ami A
- if A est homme and A parent B then A pere B
- if A aime B and B aime A then A couple B

nodes:
- voiture
- chariot
- julie

link:
- ami
- dans
- client

set:
- A connait B and B connait A get A
- geneve meteo B filter A _contains "0"
- soleil est grand

## après une première observation:
Sauf les règles qui pourraient être compliqués. Le tout pourrait être repéré par des expressions régulières.

Malgré tout il faut quand même s'occuper des "not" dans les sets

# Labo
expression pour les types

fact:
name name name

name= "[_A-Za-z]"

