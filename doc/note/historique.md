# historique
TODO: vérifier que la rétropropagation se fait bel et bien
L'historique existe pour permettre une propagation et une rétropropagation efficace.

## La propagation
Cela arrive lorsqu'un triplet est envoyé dans la base de donnée. Le triplet va enclancher un certain nombre de règles qui vont engendrer de nouveaux triplets à ajouter dans la base de donnée.

## La rétropropagation
Cela arrive lorsqu'une règle d'inférence est envoyée dans la base de donnée. La règle va prendre les données présentes dans la base de donnée qui correspondent à son entête et vont générer de nouveau triplets.

Comme on le voit, la propagation et la rétropropagation son des algorithme d'activation en chaîne. La résultante de chacune des deux donne un ensemble de nouveau triplets qui vont à leur tour activer ces algorithmes. On aurai un schéma du genre:
... triplets -> algorithmes -> triplets -> algorithmes -> ...

Et cette activation en chaîne peut très facilement tourner à l'infinit si les règles ajoutent des triplets redondant. 

Par soucis de propreté, d'unicité et d'efficacité, la base de données ne conserve pas deux fois un même triplet. C'est pourquoi elle ignor tout triplet déjà présent dans la base. Cependant chaque triplet va nécessairement appeller un ensemble de règles d'inférence avant d'être ajouté/ignoré par la base.

Imaginons que dans ce processus nous ayons deux règle de ce genre (dans un format simplifié):

si A alors B
si B alors A

On pourrait même mettre des règles intéremédiaire qui font une suite de génération, le but étant de faire une boucle dans leurs définition. Reprenons le cas décrit plus haut. Si l'utilisateur entre A alors le programme va inéfrer/Générer B é la première propagation. Quand le B généré est ajouté dans la base, alors la deuxième règle va générer A. Alors ce A va aussi activer la deuxièmre règle et ainsi de suite.

C'est pour éviter ce genre de problème que l'historique a été créée. Voila comment elle s'implémente dans le modèle de propagation et de rétropropagation.

1. Lorsqu'il fait sa commande, cette commande est "runnée" normalement en vérifiant d'avoir au préalable effacé l'historique.
2. S'il y a des triplets, alors ceux-ci son mis dans la base de données et activent les règles d'inférences correspondantes: c'est la propagation. Alors un numéro indiquant la propagation actuelle est donné et des nouveau triplets sont générés.
3. répéter le point deux jusqu'à ce qu'une propagation ne génère plus de triplets ajoutables.

Ce processus va réduire progressivement la quantité de triplet ajoutables dans la base de données. En effet, si un triplet a déjà été produit dans une propagation précédente, alors celui si sera rejeté avant même d'activer des règles d'inférence. Cela bloque la possibilité de tomber sur une boucle infinie.

Comme dit précédemment, l'historique sera effacé à la prochaine commande entrée par l'utilisateur.
