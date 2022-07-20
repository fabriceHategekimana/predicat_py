import pandas as pd
import numpy as np
from typeParser import parser
from db2 import Data
from network import displayNetwork
import csv
import re

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
    # check type
    if value[0] == "set":
        res = list(map(setToSQL, value[1]))
        query = "select * from "+" natural join ".join(res)+";"
        variables = unique(flatList(list(map(getVariables, value[1]))))
    elif value[0] == "fact":
        target = db.getDefaultTable()
        query = f"select * from facts_{target} where subject = '"+value[1]+"' and link = '"+value[2]+"' and goal = '"+value[3]+"';"
        variables = []
    return pd.DataFrame(db.sqlQuery(query), columns=variables)


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
    if entry.shape[0] > 0:
        if value[0] == "set":
            facts = substitute(entry, value[1])
        else:
            facts = substitute(entry, [value])
        db.deleteFacts(facts)
    return entry


def myFilter(entry, value):
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
        print(fromTextToList(entry, value))
    return VOIDENTRY


def to_float(text):
    try:
        val = float(text)
    except:
        val = 0.0
    return val


def myMax(entry, value):
    val = entry[value].map(to_float).max()
    return pd.DataFrame([val], columns=["max"])


def myMin(entry, value):
    val = entry[value].map(to_float).min()
    return pd.DataFrame([val], columns=["min"])


def myMean(entry, value):
    val = entry[value].map(to_float).mean()
    return pd.DataFrame([val], columns=["mean"])


def myResume(entry, value):
    max_val = entry[value].map(to_float).max()
    min_val = entry[value].map(to_float).min()
    mean_val = entry[value].map(to_float).mean()
    return pd.DataFrame([[min_val, max_val, mean_val]], columns=["min", "max", "mean"])


def count(entry, value):
    line_nb = entry.shape[0]
    return pd.DataFrame([line_nb], columns=["count"])


# deprecated
def countis(entry, sentence):
    print(str(entry.shape[0])+sentence[0]+sentence[1])
    if eval(str(entry.shape[0])+sentence[0]+sentence[1]):
        return entry
    else:
        return VOIDENTRY


def check_from(entry, value):
    # ("check_from", name, type)
    db.setDefaultTab(value[1])
    return check(entry, value[2])


def select(entry, value):
    """will extract the given variables from the dataFrame"""
    """value: [Var, Var, ...]"""
    return entry[value].drop_duplicates()


def reference(entry, value):
    """look for a node that contain the value"""
    """value = ('element', Val)"""
    term = re.sub('"', '', value[1])
    table = db.getDefaultTable()
    res = db.sqlQuery(f"select subject as A from facts_{table} where subject like '%{term}%' union select goal as A from facts_{table} where goal like '%{term}%';")
    print(res)
    return entry


def rename(entry, value):
    """rename [node/link] name newname"""
    """value = [[node|link],arg1, ..., argn]"""
    table = db.getDefaultTable()
    if value[0] == "node":
        db.sqlModify(f"UPDATE facts_{table} SET subject='{value[2]}' WHERE subject='{value[1]}'") 
        db.sqlModify(f"UPDATE facts_{table} SET goal='{value[2]}' WHERE goal='{value[1]}'") 
    elif value[0] == "link":
        db.sqlModify(f"UPDATE facts_{table} SET link='{value[2]}' WHERE link='{value[1]}'")
    else:
        print("error, the target is note even a node or a link")
    return entry


def myCalc(entry, value):
    val = eval(value.replace('"',''))
    return pd.DataFrame([val], columns=["calc"])


FUNCTIONCOMMANDS = {
        "check": check,
        "add": add,
        "delete": delete,
        "filter": myFilter,
        "csv": myCsv,
        "display": display,
        "print": myPrint,
        "countis": countis,
        "count": count,
        "check_from": check_from,
        "select": select,
        "reference": reference,
        "rename": rename,
        "max": myMax,
        "min": myMin,
        "mean": myMean,
        "resume": myResume,
        "calc": myCalc
        }

entr = pd.DataFrame({"A": ["pierre"], "B": ["ami"], "C": ["anne"]})
delete(entr, ('fact', 'pierre', 'ami', 'anne'))


