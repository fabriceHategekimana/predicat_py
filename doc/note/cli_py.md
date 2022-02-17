# cli.py
Est le module Commande line interface. C'est un interactive prompt qui permet de modifier en direct la base de donnée et de l'interroger.

## Commandes

### exit
Quitte tout simplement l'invite de commande.

### logo [symbole]
Permet d'ajouter un symbole comme logo dans le prompt.

### export to [format] [name]
Export la base de données au format csv ou gephy.

### import  csvtable [name] id [columnid] | csv [name]
import les données au format csv ou csvtable

### Mode [mode]
Il existe 3 modes:
- normal
- sql
- union
	
#### Le mode normal
Fait ce qu'on attend du programme: appelle la fonction run du module run.

#### Le mode sql
Prend des commandes sql et les exécute directement sur la base de donnée

#### Mode union
Affiche les requêtes que nous faisons sous la forme de structure de données.  

## Autres fonctions
#### completedefault
S'occupe de faire la completion
