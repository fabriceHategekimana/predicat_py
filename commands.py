import pandas as pd
import numpy as np
from typeParser import parser
from db2 import Data
from network import displayNetwork
import csv
import re
import datetime
import matplotlib.pyplot as plt

db = Data()
VOIDENTRY = pd.DataFrame()


def toIntIfPossible(val):
    try:
        val = int(val)
    except:
        pass
    return val


def formatColumn_old(x, val, columns):
    if val in columns:   # if it's a variable
        res = toIntIfPossible(x[columns.index(val)])
    else:
        res = toIntIfPossible(val)
    return res


def formatColumn(x, val, columns):
    if val in columns:   # if it's a variable
        res = toIntIfPossible(x[columns.index(val)])
    else:
        res = toIntIfPossible(val)
    return res


def isComparator(element):
    res = False
    if element in ["<", ">", "<=", ">=", "==", "equal", "notequal"]:
        res = True
    return res


def isVariable(element):
    if element in ["equal", "notequal"]:
        res = False
    else:
        val = parser.parse(element)
        if val == None:
            val = ("element", "failed")
        res = False
        if val[0] == "variable":
            res = True
    return res


def isSet(element):
    val = parser.parse(element)
    res = False
    if val[0] == "set":
        res = True
    return res


def setToSQL(set_fact, target="default"):
    triplet = set_fact[1:]
    preSQL = [[], []]
    columns = ["subject", "link", "goal"]
    if target == "default":
        target = db.getDefaultTable()
    # separate variables(=preSQL[0]) and values (=preSQL[1])
    for i in range(len(triplet)):
        if isVariable(triplet[i]):
            preSQL[0].append(columns[i]+" as "+triplet[i])
        else:
            preSQL[1].append(columns[i]+" = '"+triplet[i]+"'")
    # if there are 3 variables
    if len(preSQL[0]) == 3:
        SQLQuery = f"(select {preSQL[0][0]}, {preSQL[0][1]}, {preSQL[0][2]} from facts_{target})"
        # SQLQuery = f"(select * from facts_{target})"
    elif set_fact[0] == 1:   # if there is a 'not'
        SQLQuery = "(select "+",".join(preSQL[0])+f" from facts_{target} except select "+",".join(preSQL[0])+f" from facts_{target} where "+" and ".join(preSQL[1])+")"
    else:
        SQLQuery = "(select "+",".join(preSQL[0])+f" from facts_{target} where "+" and ".join(preSQL[1])+")"
    return SQLQuery


def getVariables(set_fact):
    triplet = set_fact[1:]
    variables = []
    for i in range(len(triplet)):
        if isVariable(triplet[i]):
            variables.append(triplet[i])
    return variables


def flatList(listoflist):
    return [item for elem in listoflist for item in elem]


def getColumn(entry, i):
    return [col[i] for col in entry.copy()]


def unique(flatlist):
    """transform a list on an unique list containing
    all the due informations"""
    newlist = []
    for f in flatlist:
        if f not in newlist:
            newlist.append(f)
    return newlist


def valueOrVariable(entry, set_value):
    if isVariable(set_value):
            res = entry[set_value].values
    else:
        if entry.shape[0] > 0:
            res = np.full(shape=entry.shape[0], fill_value=set_value, dtype=np.object)
        else:
            res = [set_value]
    return res


def createFacts(entry, set_values):
    """set_values: triplet of [subject,link,goal]"""
    df = pd.DataFrame({})
    df["subject"] = pd.Series(valueOrVariable(entry, set_values[0]))
    df["link"] = pd.Series(valueOrVariable(entry, set_values[1]))
    df["goal"] = pd.Series(valueOrVariable(entry, set_values[2]))
    return df


def removeNOTValue(x):
    """get the subject, link, goal without the not value (0, or 1)"""
    return [x[1], x[2], x[3]]


def substitute(entry, set_values):
    """The substitute function is meant to return a list of composed fact
    output: [separated facts]
    separated_fact: ['subject', 'link', 'goal']
        recieve a set and the entry
        output: a list of fact
    """
    if len(set_values[0]) > 3:
        set_values = list(map(removeNOTValue, set_values))
    res = pd.DataFrame({"subject": [], "link": [], "goal": []})
    for s in set_values:
        res = pd.concat([res, createFacts(entry, s)])
    return res


def check(entry, value):
    query = ""
    # check type
    if value == "all":
        query = "select * from facts_default;"
        variables = find_next_letter(entry, 3)
    elif value[0] == "set":
        res = list(map(setToSQL, value[1]))
        query = "select * from "+" natural join ".join(res)+";"
        variables = unique(flatList(list(map(getVariables, value[1]))))
    elif value[0] == "fact":
        target = db.getDefaultTable()
        query = f"select * from facts_{target} where subject = '"+value[1]+"' and link = '"+value[2]+"' and goal = '"+value[3]+"';"
        variables = []
    if query != "":
        return pd.DataFrame(db.sqlQuery(query), columns=variables)
    else:
        return entry


def add(entry, value):
    if value[0] == "fact":
        facts = pd.DataFrame({"subject": [value[1]], "link": [value[2]], "goal": [value[3]]})
    else:
        if entry.shape[0] > 0:
            value = value[1]
            facts = substitute(entry, value).drop_duplicates()
        else:
            facts = pd.DataFrame({"subject": [], "link": [], "goal": []})
    db.addFacts(facts)
    return entry


def delete(entry, value):
    """entry: list of tuple (negative, subject, link, goal)"""
    if entry.shape[0] > 0 and value[0] == "set":
        facts = substitute(entry, value[1])
    else:
        facts = substitute(entry, [value])
    db.deleteFacts(facts)
    return entry


def myFilter(entry, value):
    # val = ('comparators', [('b', 'contains', 'unavailable')])
    if entry.shape[0] > 0:
        for val in value[1]:
            typeConverter = str
            if val[1] == "equal":
                val = (val[0], " == ", val[2])
            elif val[1] == "notequal":
                val = (val[0], " != ", val[2])
            elif val[1] == "contains":
                val = (val[0], " contains ", val[2])
            else:
                typeConverter = int

            # int/string conversion
            if isVariable(val[0]):
                entry[val[0]] = entry[val[0]].map(typeConverter)
            if isVariable(val[2]):
                entry[val[2]] = entry[val[2]].map(typeConverter)

            # special case for the contains query
            if val[1] == " contains ":
                entry = entry[entry[val[0]].str.contains(val[2], case=False)]
            else:
                entry = entry.query("".join(val))
    return entry


def myCsv(entry, value):
    """convert the result of a command to a csv table"""
    entry.to_csv(value[1], index=False)
    return entry


def display(entry, value):
    if value[0] == "fact":
        value = [value]
    else:
        value = value[1]
    if value is not None:
        facts = substitute(entry, value)
        displayNetwork(facts.values)
    return entry


def fromTextToList(entry, sentence):
    tab = sentence.replace('"', '').split(" ")
    df = pd.DataFrame({})
    for i, element in enumerate(tab):
        df[str(i)] = pd.Series(valueOrVariable(entry, element))
    return df.apply(" ".join, axis=1)


def myPrint(entry, value):
    if entry.shape[0] > 0:
        if entry.shape == (1, 1):
            print(entry.iloc[0][0])
        else:
            print(fromTextToList(entry, value))
    return VOIDENTRY


def to_float(text):
    try:
        val = float(text)
    except:
        val = None
    return val


def myMax(entry, value):
    val = entry[value].map(to_float).max()
    return pd.DataFrame([val], columns=["max"])


def myMin(entry, value):
    val = entry[value].map(to_float).min()
    return pd.DataFrame([val], columns=["min"])


def myMean(entry, value):
    val = entry[value].map(float).mean()
    return pd.DataFrame([val], columns=["mean"])


def myResume(entry, value):
    max_val = entry[value].map(to_float).max()
    min_val = entry[value].map(to_float).min()
    mean_val = entry[value].map(to_float).mean()
    count_val = entry[value].shape[0]
    return pd.DataFrame([[min_val, max_val, mean_val, count_val]], columns=["min", "max", "mean", "count"])


def count(entry, value):
    line_nb = entry.shape[0]
    return pd.DataFrame([line_nb], columns=["count"])


def mySum(entry, value):
    sum_val = entry[value].map(to_float).sum()
    return pd.DataFrame([sum_val], columns=["sum"])


def parse_indices(index, entry):
    if index.isnumeric():
        return pd.DataFrame(entry.iloc[int(index)])
    else:
        return entry[index.split(",")]


def select(entry, value):
    if isinstance(value, tuple):
        if value[0] == "distinct":
            return parse_indices(value[1], entry).drop_duplicates()
    else:
        return parse_indices(value, entry)


def reference(entry, value):
    """look for a node that contain the value"""
    """value = ('element', Val)"""
    term = re.sub('"', '', value[1])
    table = db.getDefaultTable()
    res = db.sqlQuery(f"select subject as A from facts_{table} where subject like '%{term}%' union select goal as A from facts_{table} where goal like '%{term}%';")
    print(res)
    return entry


def rename(entry, value):
    table = db.getDefaultTable()
    if value[0] == "node":
        db.sqlModify(f"UPDATE facts_{table} SET subject='{value[2]}' WHERE subject='{value[1]}'") 
        db.sqlModify(f"UPDATE facts_{table} SET goal='{value[2]}' WHERE goal='{value[1]}'") 
    elif value[0] == "link":
        db.sqlModify(f"UPDATE facts_{table} SET link='{value[2]}' WHERE link='{value[1]}'")
    elif value[0] == "column":
        olds = value[1].split(",")
        news = value[2].split(",")
        d = {}
        for old, new in zip(olds, news):
            d[old] = new
        entry = entry.rename(columns=d)
    else:
        # TODO lister les type d'erreur
        if "," in value[0]:
            old = "("+value[0]+")"
            new = "("+value[1]+")"
        else:
            old = value[0]
            new = value[1]
        print("------------")
        print("Bad target, you must specify a an existing target with the right spelling:")
        print(f"Syntax: rename [target] {old} {new}")
        print("Target can be: column,node,link")
        print("------------")
    return entry


def replace_parameter_by_value(command, values):
    for i in range(len(values)):
        val = values[i]
        command = command.replace(f"${i+1}", f"{val}")
    return command


def format_expression(expression, entry):
    nb_row = 1 if entry.empty else entry.shape[0]
    elements = expression.split(" ")
    symbol_list = []
    for element in elements:
        if element in entry.columns:
            symbol_list.append(list(entry[element]))
        else:
            symbol_list.append([element]*nb_row)
    return pd.DataFrame(symbol_list).sum()


def myCalc(entry, value):
    print(value)
    expression = value[0]
    columns = value[1].split(",")
    computed_column = []
    if columns == [""]:
        expressions = format_expression(expression, entry)
        values = expressions.map(eval)
        return pd.DataFrame(values, columns=["calc"])
    else:
        for line in entry[columns].iterrows():
            new_expression = replace_parameter_by_value(expression, line[1])
            computed_column.append(eval(new_expression))
    return pd.DataFrame(computed_column, columns=["calc"])


def mySort(entry, value):
    columns = value.split(",")
    return entry.sort_values(columns)


def myShuffle(entry, value):
    return entry.sample(frac=1)


def get_date(day):
    today = datetime.date.today()
    if day == "today":
        return today
    elif day == "tomorrow":
        return datetime.date(today.year, today.month, today.day+1)
    elif day == "yesterday":
        return datetime.date(today.year, today.month, today.day-1)


def format_date_column(column, entry):
    nb_row = 1 if entry.empty else entry.shape[0]
    if column in entry.columns:
        return pd.to_datetime(entry[column])
    elif column in ["today", "tomorrow", "yesterday"]:
        date_list = [get_date(column)]*nb_row
        df = pd.DataFrame(date_list, columns=[column])
        return pd.to_datetime(df[column])
    elif column.count("-") == 2:
        date_list = [value]*nb_row
        column = "date"
        df = pd.DataFrame(date_list, columns=[column])
        return  pd.to_datetime(df[column])


def myDate(entry, value):
    return entry
    if isinstance(value, tuple):
        if value[0] == "diff":
            columns = value[1].split(",")
            tab = []
            left_dates = format_date_column(columns[0], entry)
            right_dates = format_date_column(columns[1], entry)
            for x, y in zip(left_dates, right_dates):
                tab.append((x-y).days)
            entry["diff"] = tab
    else:
        if value in ["today", "tomorrow", "yesterday"]:
            date_value = get_date(value)
            entry = pd.DataFrame([date_value], columns=[value])
            entry[value] = pd.to_datetime(entry[value])
        elif value.count("-") == 2:
            entry = pd.DataFrame([value], columns=["date"])
            entry["date"] = pd.to_datetime(entry["date"])
        else:
            columns = value.split(",")
            for c in columns:
                entry[c] = pd.to_datetime(entry[c])
    return entry


def myFloat(entry, value):
    entry[value] = entry[value].map(to_float)
    return entry


def myString(entry, value):
    entry[value] = entry[value].map(str)
    return entry


def find_next_letter(entry, number):
    i = 0
    variables = []
    alphabetic_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while len(variables) < number and i < len(alphabetic_list):
        letter = "_"+alphabetic_list[i:i+1]
        if letter not in entry.columns:
            variables.append(letter)
        i += 1
    return variables


def myMap(entry, value):
    try:
        if len(value) == 2:
            entry[value[1]] = entry[value[1]].map(eval(value[0]))
        elif len(value) == 3:
            letter = find_next_letter(entry, 1)[0]
            entry["map"] = entry[value[2]].map(eval(value[1]))
    except:
        print(f"Bad entry: '{value[0]}' isn't an existing function")
    return entry


def slicer(start, end):
    return lambda x: x[start:end]


def mySlice(entry, value):
    interval = value[0].split(",")
    entry[value[1]] = entry[value[1]].map(slicer(int(interval[0]), int(interval[1])))
    return entry


def myList(entry, value):
    return entry
    if isinstance(value, tuple):
        values = value[1].split(",")
        name = value[0]
    else:
        values = value.split(",")
        name = "list"
    if len(values) == entry.shape[0]:
        entry[name] = values
    else:
        rows = entry.shape[0]
        lenlist = len(values)
        print(f"length mismatch: the table has {rows} rows but the given list has {lenlist} rows")
    return entry


def myClear(entry, value):
    return VOIDENTRY


def myLimit(entry, value):
    return entry.iloc[:int(value)]


def myPlot(entry, value):
    columns = value.split(",")
    plt.plot(entry[columns[0]], entry[columns[1]])
    plt.show(block=False)
    return entry


def parameter_manager(entry, values):
    pass


FUNCTIONCOMMANDS = {
        "check": check,
        "add": add,
        "delete": delete,
        "filter": myFilter,
        "csv": myCsv,
        "display": display,
        "print": myPrint,
        "count": count,
        "select": select,
        "reference": reference,
        "rename": rename,
        "max": myMax,
        "min": myMin,
        "mean": myMean,
        "resume": myResume,
        "calc": myCalc,
        "sort": mySort,
        "shuffle": myShuffle,
        "dt": myDate,
        "float": myFloat,
        "str": myString,
        "map": myMap,
        "slice": mySlice,
        "list": myList,
        "clear": myClear,
        "sum": mySum,
        "limit": myLimit,
        "plot": myPlot,
        }

entr = pd.DataFrame({"A": ["pierre"], "B": ["ami"], "C": ["anne"]})
delete(entr, ('fact', 'pierre', 'ami', 'anne'))

