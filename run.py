from commands import *
from functools import reduce


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


def macro_error_message(command):
    print(f"Bad name: there is no macro that has the name '{command}'.")
    print("------------")
    print("Try look for thoses existing ones or create your own with this name:")
    functions = pd.DataFrame(db.getMacroList(), columns=["name", "command"])
    for name in functions["name"]:
        print("    - "+name)
    print("------------")


def format_command(command, parameters):
    if "$" not in command:
        if " " in command and parameters != [""]:
            print("Bad assignation: you give a parameter(s) to an expression that doesn't accept parmeter")
        else:
            function = db.getMacro(command)
            if function == []:
                macro_error_message(command)
            else:
                command = function[0][0]
    return command


def isValue(param):
    if to_float(param) != None:
        return True
    elif "'" in param or '"' in param:
        return True
    else:
        return False


def convertValue(param):
    if param.isnumeric():
        return int(param)
    elif "." in param and param.replace(".", "").isnumeric():
        return to_float(param)
    elif "'" in param or '"' in param:
        return param[1:-1]
    else:
        return param


def format_parameters(parameters_string, entry):
    params = parameters_string.split(",")
    parameters = []
    for param in params:
        if param in entry.columns or isValue(param):
            parameters.append(convertValue(param))
    return parameters


def create_link_command(columns):
    columns = columns.split(",")
    letters = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    new_command = []
    old_name = []
    new_name = []
    for column in columns:
        new_command.append(f"A {column} {letters[i]}")
        old_name.append(f"{letters[i]}")
        new_name.append(f"{column}")
        i += 1
    new_command = "check "+" and ".join(new_command)+" "
    part2 = "rename column ("+",".join(old_name)+") ("+",".join(new_name)+")"
    return new_command+part2


def runCommand(inp):
    inp = syntaxSugarCommand(inp)
    commands = parser.parse(inp)
    entry = VOIDENTRY
    if commands is not None:
        for c in commands:
            # Expression de degrés supérieur (qui execute d'autre expressions du même langage)
            if c[0] == "exec":
                command = c[1][0]
                parameters = format_parameters(c[1][1], entry)
                command = format_command(command, parameters)
                entry = runParametrizedCommand(entry, parameters, command)
            elif c[0] == "links":
                new_command = create_link_command(c[1])
                entry = runCommand(new_command)
            else:
                entry = execute(entry, c)
    else:
        print(f"syntax: there is a problem with the syntax of your sentence:\n '{inp}'")
        print("-----------------")
    return entry


def get_dataframe_from_line(line):
    return line[1]


def replace_parameter_by_value(command, values, parameters):
    if parameters != [""]:
        i = 0
        for p in parameters:
            if p in values.index:
                val = values[p]
            else:
                val = p
            command = command.replace(f"${i+1}", f"{val}")
            i += 1
    return command


def replace_parameter_by_value2(command, values):
    i = 0
    for val in values:
        command = command.replace(f"${i+1}", f"{val}")
        i += 1
    return command


def run_command_with_parameters(command, serie, parameters):
    if isinstance(serie, list):
        command = replace_parameter_by_value2(command, serie)
    else:
        command = replace_parameter_by_value(command, serie, parameters)
    entry = runCommand(command)
    return entry


def parameters_exist(command):
    if command.find("$") > -1:
        return True
    else:
        return False


def nb_parameters(command):
    return command.count("$")


def pcount(params):
    if params == [""]:
        return 0
    else:
        return len(params)


def runParametrizedCommand(entry, parameters, command):
    selected_entry = entry.copy()
    if (selected_entry.empty or parameters == [""]) and not parameters_exist(command):
        return runCommand(command)
    else:
        if nb_parameters(command) == pcount(parameters):
            if not selected_entry.empty:
                data = []
                for line in selected_entry.iterrows():
                    line = get_dataframe_from_line(line)
                    df = run_command_with_parameters(command, line, parameters)
                    for c, l in zip(entry.columns, line):
                        df[c] = l
                    data.append(df)
                return pd.concat(data, ignore_index=True)
            else:
                df = run_command_with_parameters(command, parameters, parameters)
                return df
        else:
            awaited = nb_parameters(command)
            founded = pcount(parameters)
            print(f"parameter mismatch: {awaited} awaited but {founded} found")
            return VOIDENTRY


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
    return command


def syntaxSugarRule(rule):
    first, rest = getFirstWord(rule)
    if first == "if":
        if " then " in rest:
            rule = "check "+rest.replace(" then ", " add ")
    return rule


