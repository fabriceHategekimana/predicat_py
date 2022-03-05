# db:
Est une classe qui manipule une base de donnée (sqlite) selon la logique du projet predicat.

PRINCIPE:

la base de donnée est composée de trois tables:

### facts:
Contient la liste des faits composé de différentes sources (écrit à la main, remplit par inférence, importé). Forme la "base de donnée" du programme.

| subject | link | goal |
|---------|------|------|
|         |      |      |

### rules:
Contient un ensemble de règle qui composent le système d'inférence du programme. Les colonnes link, goal et body contiennent les "triggers" qui peuvent lancer la règle par l'exécution du corps présent dans la colonne subject.
| id | subject | link | goal | body |
|----|---------|------|------|------|
|    |         |      |      |      |

### historical
Sert à stopper le processus de propagation et de rétropopagation. Certains ajout de fait vont enclancher des règles qui peuvent ajouter de nouveaux fait et des fait déjà ajouter (ce qui pourrait créer un enclanchement ping pong et donc infini).
Avant d'accomplir une action, le programme va regarder si la commande n'a pas déjà été exécutée durant le stage actuel. Un event est une action simple enregistré dans la base.
Un stage est juste une mesure qui indique à quel rétropopagation ou propagation on se trouve. Un même event peut se trouver dans deux stages différent et ne sera pas compté comme répétitif à ce moment là (l'event sera donc exécuté.)

| stage | event |
|-------|-------|
|       |       |

## Méthodes

### __init__(self):
Fonction d'initialisation.

### createDbIfNotExist(self):
Create a database "data.db" if it doesent exist in the current directory.

### createTablesIfNotExist(self):
Create the tables facts, rules and historical if they don't exist in the database.

### sqlQuery(self, sql):
Take a sql query, send it to the database and return the values as a 2D list

### sqlModify(self, sql):
Take a sql query that modify the data (add, delete, update) and send it to the database

### removeRepetitiveFacts(self, facts):
As it is written. Remove the redundent facts in the 2D list "facts".

### addFacts(self, facts):
Get a 2D list of facts and add them one by one

### deleteFacts(self, facts):
Get a 2D list of facts and delete them one by one

### getStage(self):
Get the actual Stage position

### addStage(self):
Increase the stage position

### clearStage(self):
Set the stage to zero

### getHistory(self, stage):
return the 2D list of previews event (command done) in the actual stage. It is there to avoid cycling to the retro/propagation for ever.

### addInHistory(self, event):
add an event to the History

### clearHistory(self):
clear the History

### getRules(self):
récupère les règles

### getRulesByArgs(self, subject, link, goal):
récupère les règles par leur identifiant

### getActualRuleId(self):
récupère les règles par leur identifiant

### addRules(self, subjects, links, goals, commands):
ajoute une liste de règles

### deleteRules(self, nums):
supprime une liste de règles

### getLinks(self):
récupère la liste de liens distincts présent dans la base de donnée

### getNodes(self):
rècupère la liste de noeuds présent dans la base de donnée

### getCommands(self):
récupère toutes les commandes disponibles 
