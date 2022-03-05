# PLY:

## Parser:

Syntax directed trnaslation:
des attributs sont attaché à chaque symbol avec une action.
Il faut voir chaque symbol comme un objet.
Chaque symbole a une valeur qui peut être appelé "état"

Yacc utilise un LR-parsing (shift reduce parsing). Bottom up technique.

Utilise un stack pour poser les symbole.
Fait un shift (déposer le token dans le stack) s'il y a rien d'autre à faire
Fait un reduce quand les token présent dans la pile peuvent être réduits à l'aide d'une règle grammatical.

grammar rule:
p: sequence contenant la valeur de chaque symbol de grammaire

yacc.parse()
Fait le parsing et retourne la dernière valeur donnée par le p[0] du start

Créer un empty production
```python
def p_empty(p):
    'empty :'
    pass
```

on peut maintenant appeler empty dans les autres règles grammaticales

S'il y a un shift/reduce conflict, le shift est favorisé

On peut établir des précédences qui vont donner une priorité à certaines règles grammaticales.

1. If the current token has higher precedence than the rule on the stack, it is shifted.
2. If the grammar rule on the stack has higher precedence, the rule is reduced.
3. If the current token and the grammar rule have the same precedence, the rule is reduced for left associativity, whereas the token is shifted for right associativity.
4. If nothing is known about the precedence, shift/reduce conflicts are resolved in favor of shifting (the default).

On peut utiliser la table précédence pour empêcher des opération d'être associatives (par exemple a < b < c)

s'il y a reduce/reduce, la première règle grammatical qui satisfait la transition est prise.

## Debbuging:
parser.out sert de repérage pour le debbuging.
Les différent états (states) du fichier présentents toutes les séquence de token valide accèptés par la grammaire.
Le "." indique la position actuelle du parsing
