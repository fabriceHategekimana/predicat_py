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
        rest = runRule(rest)
        subRun(rest)
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
        rest = runRule(rest)
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
    rest = syntaxSugarRule(rest)
    first, rest = getFirstWord(rest)
    res = "check void void void"
    if first == "delete":
        ruleIds = rest.split(" ")
        db.deleteRules(ruleIds)
    elif first == "":
        for rule in db.getRules():
            print(rule)
    else:  #if we add an expression
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
    triplet = ["", "", ""]
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
    exp = removeCommandsAndConnectors(exp)
    tab = exp.split(" , ")
    triplets = list(filter(lambda z: not z == None, map(lambda x: x.split(" ") if x.count(" ") == 2 else None, tab)))
    # Do not remove (make the reduce fuction in the lin 57 work properly)
    triplets.append(["A", "A", "A"])
    tripletsValue = list(map(lambda x: getValueOnly(x), triplets))
    return cleanTripletsValue(np.array(tripletsValue).T)


def is_element(command):
    if command[0] == "element":
        return True
    else:
        return False


def format_command(command):
    if is_element(command):
        command = db.getMacro(command[1])[0][0]
    return command


def runCommand(inp):
    # check A grade lt append (check $1 engagement B) (A) (B) append (check $1 $2 C) (A,B) (C)
    # check A species B select A append [calc ($1+1)] [A] [C]
    inp = syntaxSugarCommand(inp)
    commands = parser.parse(inp)
    entry = VOIDENTRY
    for c in commands:
        '''On traite en premier lieu les expresion de degré superieur
        exec et append'''
        if c[0] == "exec":
            command = c[1][0]
            parameters = c[1][1]
            command = format_command(command)
            if parameters == "":
                entry = runCommand(command)
            else:
                entry = runParametrizedCommand(entry, parameters, command)
        elif c[0] == "append":
            command = c[1][0]
            parameters = c[1][1]
            columns = c[1][2]
            command = format_command(command)
            if parameters == "":
                entry = runCommand(command)[parameters.split(",")+columns.split(",")]
            else:
                entry = runParametrizedCommand(entry, parameters, command)[parameters.split(",")+columns.split(",")]
        else:
            entry = execute(entry, c)
    return entry


def get_dataframe_from_line(line):
    return line[1]


def replace_parameter_by_value2(command, values, parameters):
    i = 0
    for p in parameters:
        val = values[p]
        command = command.replace(f"${i+1}", f"{val}")
        i += 1
    return command


def run_command_with_parameters(command, serie, parameters):
    command = replace_parameter_by_value2(command, serie, parameters)
    # command = replace_parameter_by_value(command, serie)
    entry = runCommand(command)
    return entry


# TODO à déselectionner la ligne 160
def runParametrizedCommand(entry, parameters, command):
    parameters = parameters.split(",")
    # selected_entry = entry[parameters]
    selected_entry = entry
    data = []
    for line in selected_entry.iterrows():
        line = get_dataframe_from_line(line)
        df = run_command_with_parameters(command, line, parameters)
        for p, l in zip(parameters, line):
            df[p] = l
        data.append(df)
    final = pd.concat(data, ignore_index=True)
    return final


def execute(entry, c):
    funct = FUNCTIONCOMMANDS.get(c[0], "null")
    if funct != "null":
        entry = funct(entry, c[1])
    else:
        entry = VOIDENTRY
    return entry


def getFirstWord(exp):
    tab = exp.split(" ")
    return tab[0], " ".join(tab[1:])


def getRules(hist):
    """This function transform the history in a list of corresponding rules"""
    triplets = list(map(lambda x: x.split(" "), hist))
    rulesUnformated = list(map(lambda x: db.getRulesByArgs(x[0], x[1], x[2]), triplets))
    if rulesUnformated != []:
        rules = list(reduce(lambda x, y: x+y, rulesUnformated))
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
            command = "check "+rest+" "+command+" "+"delete "+rest+" "+command
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
            rule = "check "+rest.replace(" then ", " add ")
    return rule
