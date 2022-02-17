# Network.py
Générateur de graphe sur le browser (sous la forme d'un fichier html nomé "network.html"). Module qui utilise le Module Networkx de python.

## Fonctions

### getImages():
Génères des images contenu dans le fichier "logo.csv" TODO: plus d'info

### getRandomColor():
Génère une couleur aléatoire quand on l'appelle. Retourne la couleur en héxadécimal.

### getColumn(num, mylist):
Attrape la colonne numéro num de la liste 2D donnée

### unique(mylist):
Retire les triplet redondant de la liste 2D

### addNodes(net, facts):
ajoute la liste de nodes (noeuds) dans le réseau 

### addEdges(net, facts):
ajoute la liste de edge (lien) dans le réseau 

### displayNetwork(tab):
Génère le fichier html et le lance avec notre browser défini par défaut.

