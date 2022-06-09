from commands import *
from functools import reduce

def dataPrint(dataFrame):
    concatenation = lambda x: print(",".join(x))
    dataFrame.apply(concatenation, axis=1)

def run(inp):
    """run a command. Two cases:
        1) this is a rule command and we perform delete, display or save
        2) this is a normal command and we start parsing it"""
    db.clearStage()
    db.clearHistory()
    first, rest = getFirstWord(inp)
    if first == "rule":
        rest= runRule(rest)
        subRun(rest)
    elif first == "node":
        print(db.getNodes())
    elif first == "link":
        print(db.getLinks())
    else:
        val = runCommand(inp)
        print(val)
        propagation()

def runFromExternal(inp):
    """like run but print the results differently for a cli purpose"""
    db.clearStage()
    db.clearHistory()
    first, rest = getFirstWord(inp)
    if first == "rule":
        rest= runRule(rest)
        subRun(rest)
    elif first == "node":
        dataPrint(db.getNodes())
    elif first == "link":
        dataPrint(db.getLinks())
    else:
        val = runCommand(inp)
        dataPrint(val)
        propagation()

def runRule(rest):
    rest= syntaxSugarRule(rest)
    first, rest = getFirstWord(rest)
    res= "check void void void"
    if first == "delete":
        ruleIds= rest.split(" ")
        db.deleteRules(ruleIds)
    elif first == "":
        for rule in db.getRules():
            print(rule)
    else: #if we add an expression
        exp = first+" "+rest
        values = filterVariables(rest)
        db.addRules("'inference'", values[0], values[1], values[2], exp)
        res = exp
    return res

def removeCommandsAndConnectors(exp):
    """get an expression and replace each commande by a ','"""
    tab = exp.split(" ")
    commands = db.getCommands()
    connectors = ["and"]
    commandsAndConnectors = commands+connectors
    return " ".join(list(map(lambda x: "," if x in commandsAndConnectors else x, tab)))

def getValueOnly(tab):
    """delete all the variables in a given list"""
    triplet= ["", "", ""]
    for i in range(3):
        if not isVariable(tab[i]) and not isComparator(tab[i]):
            triplet[i] += tab[i]
    return triplet

def cleanTripletsValue(tripletsValue):
    res = []
    for line in tripletsValue:
        res.append([x for x in line if x != ""])
    return res

def filterVariables(exp):
    """get an expression, separate each part and remove variables"""
    exp= removeCommandsAndConnectors(exp)
    tab= exp.split(" , ")
    triplets= list(filter(lambda z: not z == None, map(lambda x: x.split(" ") if x.count(" ") == 2 else None, tab)))
    # Do not remove (make the reduce fuction in the lin 57 work properly)
    triplets.append(["A", "A", "A"])
    tripletsValue = list(map(lambda x: getValueOnly(x), triplets))
    return cleanTripletsValue(np.array(tripletsValue).T)

def runCommand(inp):
    inp = syntaxSugarCommand(inp)
    commands= parser.parse(inp)
    entry= VOIDENTRY
    for c in commands:
        entry= execute(entry,c)
    return entry # TODO modify the returned entry (perhaps a matrix or still a df)

def execute(entry, c):
    funct= FUNCTIONCOMMANDS.get(c[0], "null")
    if funct != "null":
        entry= funct(entry, c[1])
    else:
        entry= VOIDENTRY
    return entry

def getFirstWord(exp):
     tab= exp.split(" ")
     return tab[0], " ".join(tab[1:])

def getRules(hist):
    """This function transform the history in a list of corresponding rules"""
    triplets = list(map(lambda x: x.split(" "), hist))
    rulesUnformated = list(map(lambda x: db.getRulesByArgs(x[0], x[1], x[2]), triplets))
    if rulesUnformated != []:
        rules = list(reduce(lambda x,y: x+y, rulesUnformated))
    else:
        rules = rulesUnformated
    return rules

def noneIfNotTriplet(hist):
    res = hist
    if hist.count(" ") != 2:
        res = None
    return res

def propagation():
    """launch rules according to the history of event (add)"""
    historyUnformated = db.getHistory(db.getStage())
    history = list(filter(lambda x: x != None, map(lambda x: noneIfNotTriplet(x[1]), historyUnformated)))
    rules = np.unique(getRules(history))
    db.addStage()
    for rule in rules:
        subRun(rule)

def subRun(inp):
    """run a command link run but dont clear history. Two cases:
        1) this is a rule command and we perform delete, display or save
        2) this is a normal command and we start parsing it"""
    first, rest = getFirstWord(inp)
    if first == "rule":
        runRule(rest)
    else:
        runCommand(first+" "+rest)
    propagation()

def syntaxSugarCommand(command):
    first, rest = getFirstWord(command)
    if first == "delete":
        if isSet(rest):
            command= "check "+rest+" "+command+" "+"delete "+rest+" "+command
    elif first == "display":
        if rest == "all":
            command = "check A B C display A B C"
        elif isSet(rest):
            command = "check "+rest+" "+command
    elif first == "check":
        if rest == "all":
            command = "check A B C"
    return command

def syntaxSugarRule(rule):
    first, rest = getFirstWord(rule)
    if first == "if":
        if " then " in rest:
            rule= "check "+rest.replace(" then ", " add ")
    return rule
