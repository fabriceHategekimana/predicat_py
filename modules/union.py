from modules.db import *
d= Data()
ENTETE=[]

def isFilter(tab):
    res= False
    if tab[1] in ["<",">","<=",">=","=","-contains"]:
        res= True
    return res

def isComplet(tab):
    res= True
    for t in tab:
        if t.count('A') + t.count('B') + t.count('C') > 0:
           res= False 
    return res

def removeVoidString(liste):
    while("" in liste):
        liste.remove("")
    return liste

def isVariable(element):
    alphabet= ["_A","_B","_C","_D","_E","_F","_G","_H","_I","_J","_K","_L","_M","_N","_O","_P", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    res= False
    if element in alphabet:
        res= True
    return res

def elementOrVariable(entry):
    res="el"
    if isVariable(entry):
        res="var"
    return res

def getPredicateShape(variables, values):
    var= []
    for v in variables:
        inter= v.split(" as ")
        var.append(inter[0])
        var.append(inter[1])
    val= removeVoidString(list(values))
    tab= var+val
    #print("tab:",tab)
    subject= ""
    link= ""
    goal= ""
    i= 0
    while(i < len(tab)):
        if tab[i] == "subject":
            subject= elementOrVariable(tab[i+1])
        elif tab[i] == "link":
            link= elementOrVariable(tab[i+1])
        elif tab[i] == "goal":
            goal= elementOrVariable(tab[i+1])
        i += 2
    shape= subject+","+link+","+goal
    return shape

def getTargetedSet(exp):
    command= completeNot(exp)
    variables, values = variableIndex(command)
    shape= getPredicateShape(variables, values)
    #print("shape:", shape)
    # a b c
    if shape == "el,el,el":
        sql= "select distinct subject, goal, fact from facts"
    # A b c
    elif shape == "var,el,el":
        sql= "select distinct %s from facts" % variables
    # a B c
    elif shape == "el,var,el":
        sql= "select distinct %s from facts" % variables
    # a b C
    elif shape == "el,el,var":
        sql= "select distinct %s from facts" % variables
    # A B c
    elif shape == "var,var,el":
        sql= "select distinct %s, %s from facts" % variables
    # a B C
    elif shape == "el,var,var":
        sql= "select distinct %s, %s from facts" % variables
    # A b C
    elif shape == "var,el,var":
        sql= "select distinct %s, %s from facts" % variables
    # A B C
    elif shape == "var,var,var":
        sql= "select distinct %s, %s, %s from facts" % variables
    else:
        sql= "select * from facts"
    return sql

def getVariables(exp):
    final= []
    for e in exp:
        if isVariable(e) and e not in final:
            final.append(e)
    return final

def match(l1,l2):
    res= False
    for l in l1:
        if l in l2:
            res= True
    return res

def variableIndex(command):
    variables= []
    values= []
    column= ["","subject","","link","","goal"]
    tab= command
    for i in range(len(tab)): # on explore les éléments de la commande
        if tab[i] in ["not",""]: # si on tombe sur un 'not' ou pas on l'ajoute par défaut
            values.append(tab[i])
        elif isVariable(tab[i]): # si on trouve une variable
            variables.append(column[i]+" as "+tab[i]) # on l'ajoute à la table des variables
            values.pop() # on retire le 'not' ou le '' ajouté précédement dans values
        else: # sinon on ajoute le nom de la column et la valeur
            values.append(column[i])
            values.append(tab[i])
    return tuple(variables), tuple(values)

def createUnionQuery(command):
    command= completeNot(command)
    variables, values = variableIndex(command)
    if len(variables) == 2:
        tvariable= "%s,%s" % variables
        tvalue= "%s %s='%s'" % values
        sql= "(select "+tvariable+" from facts where "+tvalue+")"
    elif len(variables) == 1:
        tvariable= "%s" % variables
        tvalue= "%s %s='%s' and %s %s='%s'" % values
        sql= "(select "+tvariable+" from facts where "+tvalue+")"
    else:
        sql= "(select subject as A, link as B, goal as C from facts)"
    return sql

def getGoalNumber(): # get the number in the goal column
    return "(select goal as num from facts where goal like '1%' or goal like '2%' or goal like '3%' or goal like '4%' or goal like '5%' or goal like '6%' or goal like '7%' or goal like '8%' or goal like '9%')"

def convert(exp):
    #split the sentence
    if exp.find("&&") > -1:
        exp= exp.split("&&")
    else:
        exp= exp.split(" ")
    # converting predicat to sql
    sql= "(select count(goal) from facts)" # default sql if an unknow sentence occure
    if isFilter(exp): # if it's an expression with a comparison operation
        if exp[1] == "-contains": # format for "fuzzy" string matching
            exp[1] = "like"
            sql= "(select goal as "+exp[0]+" from facts where goal like '%"+exp[2]+"%')"
        else:
            sql= "(select num as "+exp[0]+" from "+getGoalNumber()+" where num "+exp[1]+" "+exp[2]+")"
    elif exp[0].find("not(") == 0: #if it's a negative predicat
        exp[0]= exp[0][4:]
        #print("exp: ", exp)
        sql1= getTargetedSet(exp.copy())
        sql2= createUnionQuery(exp)[1:-1]
        sql= "("+sql1+" except "+sql2+")"
    elif isComplet(exp):
        exp= completeNot(exp)
        t= tuple(exp)
        sql= "(select * from facts where %s subject='%s' and %s link='%s' and %s goal='%s'" % t+")"
    else:
        sql= createUnionQuery(exp)
    return sql

def hasNot(exp):
    return "not" in exp

def completeNot(exp):
    if hasNot(exp):
        pos= exp.index("not") 
        if pos == 0:
            exp.insert(2, "")
            exp.insert(4, "")
        elif pos == 1:
            exp.insert(0, "")
            exp.insert(4, "")
        elif pos == 2:
            exp.insert(0, "")
            exp.insert(2, "")
    else:
        exp.insert(0, "")
        exp.insert(2, "")
        exp.insert(4, "")
    return exp

def setAND(exp, varList):
    for i in range(len(varList)-1):
        if match(varList[i],varList[i+1]):
            exp= exp.replace("AND","NATURAL JOIN",1)
        else:
            exp= exp.replace("AND","CROSS JOIN",1)
    return exp

def unionPredicat(exp):
    final= []
    tabOR= exp.split(" &or& ")
    for t in tabOR:
        varList= []
        tabAND= t.split(" &and& ")
        subexp= ""
        for i in range(len(tabAND)): # on converti chaque conjonction
            var= getVariables(tabAND[i])
            subexp += convert(tabAND[i])+" AND "
            varList.append(var)
        subexp= subexp[:-5] # on enlève le " AND " en trop
        num= len(t.split(" AND "))
        final.append(setAND(subexp, varList))
    #dernier traitement des parenthèses à côté des or
    for i in range(1,len(final)):
        final[i]= final[i].replace("(","",1).replace(")","",1)
    return " UNION ".join(final)

def unionFilter(exp):
    if exp != "":
        final= []
        tabOR= exp.split(" &or& ")
        for t in tabOR:
            tabAND= t.split(" &and& ")
            semifinal=[]
            for i in range(len(tabAND)): # on converti chaque conjonction
                expression= tabAND[i].split("&&")
                if expression[1] == "-contains":
                    expression[1] = "like"
                    expression[2] = "'%"+expression[2]+"%'"
                semifinal.append(" ".join(expression))
            final.append(" and ".join(semifinal))
        res= " or ".join(final)
    else:
        res= exp
    #print("unionFilter:", res)
    return res

def unionGet(exp):
    exp= exp.replace(" ",",")
    #print("UnionGet:", exp)
    return exp

def union(exp, command="check"):
    #traitement au préalable des predicat, filter, get
    tab= exp.split(" &part& ")
    if len(tab) == 3:
        myPredicat= unionPredicat(tab[0])
        myFilter= unionFilter(tab[1])
        myGet= unionGet(tab[2])
        if command == "check":
            if myFilter != "":
                res= "select "+myGet+" from "+myPredicat+" where "+myFilter+";"
            else:
                res= "select "+myGet+" from "+myPredicat+";"
        elif command == "delete":
            res= "delete from facts "
    else:
        res= unionPredicat(tab[0])
    #print("final query:", res)
    return res
