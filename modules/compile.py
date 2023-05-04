import ply.lex as lex
import ply.yacc as yacc
import math as m
import csv

typeTable= {}
VALUES= []

def writeCSV(tab, fname="res.txt"):
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tab)

def write(exp, fname="res.txt"):
    f= open(fname, "w")
    f.write(exp)
    f.close()

def completeAnonymousVariables(exp):
    if exp.find("$VAR$") > -1:
        alphabet= ["_A","_B","_C","_D","_E","_F","_G","_H","_I","_J","_K","_L","_M","_N","_O","_P"]
        if exp.find(" &and& ") > -1:
            tab= exp.split("$VAR$")
            #print("tab:", tab)
            chosenLetters= alphabet[:len(tab)]
            #print("chosenLetters:", chosenLetters)
            exp=""
            for i in range(len(tab)-1):
                exp+= tab[i]+chosenLetters[m.floor(i/2)]
            exp += tab[len(tab)-1]
        else:
            exp= exp.replace("$VAR$", "_A")
    return exp

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   

reserved = { 
        "add" : "ADD",
        "check" : "CHECK",
        "and" : "AND",
        "or" : "OR",
        "if" : "IF",
        "then" : "THEN",
        "not" : "NOT",
        "contains" : "CONTAINS",
        "macro" : "MACRO",
        "filter" : "FILTER",
        "get" : "GET"
        }
                         
tokens = [
    'NUM',
    'VAR',
    'NAME',
    'STRING',
    'SUP',
    'INF',
    'EQUAL',
    'MINUS',
    'PLUS',
    'DOT',
    'EXCL'
        ]+list(reserved.values())

t_INF= r'\<'
t_SUP= r'\>'
t_EQUAL= r'\='
t_MINUS= r'\-'
t_PLUS= r'\+'
t_DOT= r'\.'
t_EXCL= r'\!'

t_ignore = r' '

def t_NUM(t):
    r'\d+'
    t.value = str(t.value)
    return t

def t_NAME(t):
    r'[a-zA-ZéèêàâïùçÀô][a-zA-Z0-9_éèêàâïùçÀô][a-zA-Z0-9_éèêàâïùçÀô]*'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_VAR(t):
    r'_?[A-Z$]'
    t.type = 'VAR'
    return t

def t_STRING(t):
    r'"([^"\n])*"'
    t.type = reserved.get(t.value,'STRING')
    t.value= t.value[1:-1]
    return t

def t_error(t):
    write("&Error: Illegal characters! ", t)
    t.lexer.skip(1)

lexer= lex.lex()

#----------------------------------

#Parser

def p_start(p):
    '''
    start : ADD add
          | CHECK check
    '''
    print("+--------------+")

def p_add(p):
    '''
    add : fact
        | rule
        | macro
    '''
    write(p[1])

def p_fact(p):
    '''
    fact : ent ent ent_string
    '''
    p[0] = "&&".join(p[1:])

def p_fact_not(p):
    '''
    fact : NOT ent ent ent_string
         | ent NOT ent ent_string
         | ent ent NOT ent_string
    '''
    p[0] = "not("+"&&".join(p[1:]).replace("not&&", "").replace("&&not&&", "").replace("&&not", "")

def p_ent(p):
    '''
    ent : NAME
        | NUM
    '''
    p[0] = p[1]

def p_ent_string(p):
    '''
    ent_string : ent
               | STRING
    '''
    p[0] = p[1]

def p_check1(p):
    '''
    check : prop filt get
    '''
    p[1]= completeAnonymousVariables(p[1])
    res= " &part& ".join(p[1:])
    write(res)

def p_check2(p):
    '''
    check : prop filt
    '''
    p[1]= completeAnonymousVariables(p[1])
    res= p[1]+" &part& "+p[2]+" &part& *" #the star is important for the "all" in sql queries
    write(res)

def p_check3(p):
    '''
    check : prop get
    '''
    p[1]= completeAnonymousVariables(p[1])
    res= p[1]+" &part&  &part& "+p[2] #the star is important for the "all" in sql queries
    write(res)

def p_check4(p):
    '''
    check : prop
    '''
    p[1]= completeAnonymousVariables(p[1])
    res= p[1]+" &part&  &part& *" #the star is important for the "all" in sql queries
    write(res)

def p_prop1(p):
    '''
    prop : prop log_op prop
    '''
    p[0] = p[1]+" &"+p[2]+"& "+p[3]

def p_prop2(p):
    '''
    prop : ent_var ent_var ent_var_string
           | ent_var filter_op ent_string
    '''
    p[0] = "&&".join(p[1:])

def p_prop2_not(p):
    '''
    prop : NOT ent_var ent_var ent_var_string
           | ent_var NOT ent_var ent_var_string
           | ent_var ent_var NOT ent_var_string
    '''
    p[0] = "not("+"&&".join(p[1:]).replace("not&&", "").replace("&&not&&", "").replace("&&not", "")

def p_prop_short1(p):
    '''
    prop : ent_var ent_var
    '''
    p[0] = "&&".join(p[1:])+"&&$VAR$" #add an anonimous variable

def p_prop_short2(p):
    '''
    prop : ent_var DOT tail
    '''
    p[0] = p[1]+"&&"+p[3]

def p_prop_short3(p):
    '''
    prop : ent_var ent_var filter_op ent_string 
    '''
    p[0] = p[1]+"&&"+p[2]+"&&$VAR$ &and& $VAR$&&"+p[3]+"&&"+p[4]

def p_prop_tail1(p):
    '''
    tail : ent tail
    '''
    p[0] = p[1]+"&&$VAR$ &and& $VAR$&&"+p[2] #combine with a chain of anonimous variables

def p_prop_tail2(p):
    '''
    tail : ent
    '''
    p[0] = p[1]+"&&$VAR$"

def p_prop_tail3(p):
    '''
    tail : ent VAR
    '''
    p[0] = p[1]+"&&"+p[2]

def p_filt1(p):
    '''
    filt : FILTER filter
    '''
    p[0] = p[2]

def p_filt2(p):
    '''
    filter : filter log_op filter
    '''
    p[0] = p[1]+" &"+p[2]+"& "+p[3]

def p_filt3(p):
    '''
    filter : ent_var filter_op ent_var_string
    '''
    p[0] = "&&".join(p[1:])

def p_get1(p):
    '''
    get : GET getter
    '''
    p[0] = p[2]

def p_get2(p):
    '''
    getter : VAR getter
    '''
    p[0] = p[1]+" "+p[2]

def p_get3(p):
    '''
    getter : VAR
    '''
    p[0] = p[1]

def p_ent_var_string(p):
    '''
    ent_var_string : ent_string
                   | VAR
    '''
    p[0] = p[1]

def p_ent_var(p):
    '''
    ent_var : ent
            | VAR
    '''
    p[0] = p[1]

def p_log_op(p):
    '''
    log_op : AND
           | OR
    '''
    p[0] = p[1]

def p_filter_op(p):
    '''
    filter_op : INF
            | SUP
            | EQUAL
            | EXCL EQUAL
            | INF EQUAL
            | SUP EQUAL
            | MINUS CONTAINS
    '''
    p[0] = "".join(p[1:])

def p_rule(p):
    '''
    rule : IF logalg_rule THEN logalg_rule
    '''
    p[0] = p[2].replace("&&", " ")+"&&rule&&"+p[4].replace("&&", " ")

def p_logalg_rule1(p):
    '''
    logalg_rule : logalg_rule log_op logalg_rule
    '''
    p[0] = p[1]+" &"+p[2]+"& "+p[3]

def p_logalg_rule2(p):
    '''
    logalg_rule : ent_var ent_var ent_var
                | ent_var filter_op ent
    '''
    p[0] = "&&".join(p[1:])

def p_macro(p):
    '''
    macro : MACRO
    '''
    p[0] = p[1]

def p_error(p):
    write("&Error bad syntax")

parser= yacc.yacc()
