# règles sur les groupes
rule check A groupe B and C groupe B filter A notequal C add A voisin C

# règle pour les relations indéfinies
rule check A groupe B and C groupe D filter B notequal D add A inconnu C

# règle d'exclusion des autres membres de groupe
rule check A connected B and A voisin C and B voisin D add C unconnected B and D unconnected A delete C inconnu B and B inconnu C and D inconnu A and A inconnu D

# règles de déduction de groupo
rule check A connected B and B connected C add A connected C 
rule check A unconnected B and B connected C add A unconnected B

# règles de symmétrie
rule check A connected B filter A notequal B add B connected A
rule check A unconnected B filter A notequal B add B unconnected A
rule check A inconnu B filter A notequal B add B inconnu A

# définition de certains groupes
add femmes est groupe
add hotels est groupe
add numeros est groupe

# groupe des femmes
add jocelyne groupe femmes
add lucie groupe femmes
add paule groupe femmes

# groupe des hôtels

add cabotin groupe hotels
add logis groupe hotels
add noctambule groupe hotels

# numeros des chambres
add 305 groupe numeros
add 419 groupe numeros
add 538 groupe numeros
