# La pipeline

La pipeline va traiter chaque commandes de façon harmonique et pouvoir enchainer les résultats.

chaque commandes va appeler la fonction qui lui correspond.

chacune de ces fonctions a les mêmes entrées et la même sortie:
1. le tableau de permutation
2. la colonne de résultats de calcul (s'il y a )
3. l'expression à traiter

On a les éléments 1. et 2. à la sortie de chaque fonction.

pseudo code en python

```
permutation= [[]]
resultat= [[]]

for each cmd:
	func= getFunction(cmd[0])
	permutation, resultat = func(permutation, resultat, cmd[1])
	
```


