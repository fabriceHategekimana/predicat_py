import pandas as pd
from db2 import Data
import csv

db = Data()


def toCSV(name, csvFormat):
    if csvFormat == "gephy":
        tab = db.sqlQuery("select subject,goal,link from facts;")
        tab.insert(0, ["source","target","link"])
    else:
        tab = db.sqlQuery("select * from facts;")
        tab.insert(0, ["subject","link","goal"])
    with open(name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tab)


def fromCSV(name):
    with open(name) as f:
        reader = csv.reader(f)
        tab = list(reader)
    if len(tab[0]) == 3 and tab[0]:
        entete = tab.pop(0)
        if entete == ["subject", "target", "link"]:  # pour gephy
            tab = list(map(lambda x: [x[0], x[2], x[1]], tab))
            db.addFacts(tab)
        elif entete == ["subject", "link", "goal"]:
            db.addFacts(pd.DataFrame(tab, columns=entete))


def get_csv_as_2D_table(name):
    with open(name) as f:
        reader = csv.reader(f)
        tab = list(reader)
    return tab


def get_columns(tab):
    return tab[0]


def get_lines(tab):
    return tab[1:]


def get_columns_and_lines(tab):
    columns = get_columns(tab)
    lines = get_lines(tab)
    return columns, lines


def get_columns_line_couples(columns, line):
    res = []
    for c, l in zip(columns, line):
        res.append((c, l))
    return res


def get_identifier_and_rest(line, columnid):
    identifier = ""
    rest = []
    i = 0
    while i < len(line):
        if i == columnid:
            identifier = line[i]
        else:
            rest.append(line[i])
        i += 1
    return identifier, rest


def notEmpty(val):
    if val == "" or val == None:
        return "-"
    else:
        return val


def create_triplets(columns, line, columnid):
    couples = get_columns_line_couples(columns, line)
    identifier, rest = get_identifier_and_rest(couples, columnid)
    triplets = []
    # index 0: column name, index 1: value
    for x in rest:
        triplets.append([identifier[1], x[0], notEmpty(x[1])])
    triplets.append([identifier[1], "type", "id"])
    return triplets


def fromCSVTable(name, columnid, entity):  # entity is the classe/type of the tuple
    tab = get_csv_as_2D_table(name)
    columns, lines = get_columns_and_lines(tab)
    columnid = columns.index(columnid)
    triplets = []
    for line in lines:
        triplets += create_triplets(columns, line, columnid)
    for column in columns:
        triplets.append([column, "type", "column"])
    db.addFacts(pd.DataFrame(triplets, columns=["subject", "link", "goal"]))


def fromPredicatFile(MyPrompt, name):
    f = open(name, "r")
    for line in f.readlines():
        cleanline = line.replace("\n", "")
        if len(cleanline) > 0 and cleanline[0:1] != "#":
            MyPrompt.onecmd(cleanline)
