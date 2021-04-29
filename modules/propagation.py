from modules.union import *
#from db import *

def complete(exp, varList, value):
    for i in range(len(varList)):
        exp= exp.replace(varList[i], value[i])
    return exp

def retroPropagation(rule):
    sql= union(rule[0])
    facts= d.sqlQuery("select * from "+sql+";")
    varList= getVariables(rule[0].split(" "))
    for fact in facts:
        res= complete(rule[1], varList, fact)
        if res not in(ENTETE):
            addFact(res)

def addFact(fact):
    d.sqlModify("insert or ignore into facts (subject,link,goal) values (\"%s\",\"%s\",\"%s\")" % tuple(fact.split(" ")))
    ENTETE.append(fact)
    if fact.find(" ") == -1: # Si c'est pas une chaine de caractère (s'il y a des espaces)
        propagation(fact)

def propagation(fact):
    fact= fact.split(" ")
    print("fact", fact)
    for i in range(3):
        fact[i]= "%"+fact[i]+"%"
    rules= d.sqlQuery("select * from rules where premises like '%s' or premises like '%s' or premises like '%s'" % tuple(fact))
    for rule in rules:
        retroPropagation(rule[1:])

