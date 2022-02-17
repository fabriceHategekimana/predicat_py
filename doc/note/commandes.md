# Commandes
Nous avons différents type de commandes.

- check
- add
- delete
- myCsv
- display
- excel
- myFilter

Chaque commande a le même protocole d'évaluation. La commande prend en entrée un tableau et une structure de donnée représentant une valeur d'entrée puis sort à son tour un tableau.

cmd(tab,val) -> tab

Cela permet de pouvoir combiner les commandes sous la forme d'un [pipeline](pipeline). Toute les commandes écrite par un utilisateur prennent des arguments qui seront convertis en valeur. La première commande dans une combinaison de commandes prendra par défaut un tabelau vide.

cmd args 
va donner
cmd([],val) -> tab

et
cmd1 args1 cmd2 args2 ... cmdN argsN
va donner l'enchainement
cmd1([],val1) -> tab1
cmd2(tab1, val2) -> tab2
...
cmdN(tabN-1, valN) -> tabN

S'il n'y a plus de commandes qui suit alors le programme retourne le dernier tableau obtenu.

