# Règles:
Pour qu'un paradigme logique puisse être mis en forme, il faut des propositions ainsi que des règles d'inférence.

C'est pourquoi le programme dispose aussi de la possibilité de pouvoir avoir des règles qui vont s'appliquées automatiquement à chaque commandes entrées par l'utilisateur, ce qui va provoquer une chaine d'activation (voir la propagation dans [historique](historique)). On peut dire ici que les règles d'inférences sont des commandes qui se lance automatiquement à des moments spécifiques sans avoir besoin de l'intervention de l'utilisateur.

Une règle d'inférence est simple dans sa définition car elle est composée en deux parties:
- les conditions
- les conséquence

Les conditions sont seulement des élément composés de commandes check et filter alors que le reste est composé de commandes qui peuvent modifier la base de donnée (add, delete, etc.) ou d'autres fonctions.

L'astuce dans le programme est qu'une règle d'inférence est juste une composition de commande de type "get and set" préfixé par la commande rule. Cela nous permet de tester l'application d'une commande et voir si on est intéressé à la transformer en règle d'inférence.

Par exemple, si on veut dire que tout les chiens de la base de données sont des mammifères:

check A est chien add A est mammifere

Si on veut le transformer en règle, il suffit juste de prefixer le tout par la commande rule:

rule check A est chien add A est mammifere

La plus part des règle d'inférence sont le plus souvent là pour créer de nouvelles informations on peut donc ajouter du sucre syntaxique avec la notation "if then":

rule if A est chien then A est mammifere

Cette notation est plus intuitive pour nous et sera transformé dans la forme précédente par le programme.

Étant donné que les règles sont issues de commandes, on peut faire faire des règles complexes par des commandes complexes.

TODO: processus de transformation et d'ingestion d'une règle dans la base de données.
