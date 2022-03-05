import pandas as pd
from db2 import Data
import csv

db= Data()

def toCSV(name, csvFormat):
    if csvFormat == "gephy":
        tab= db.sqlQuery("select subject,goal,link from facts;")
        tab.insert(0, ["source","target","link"])
    else:
        tab= db.sqlQuery("select * from facts;")
        tab.insert(0, ["subject","link","goal"])
    with open(name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tab)

def fromCSV(name):
    with open(name) as f:
        reader = csv.reader(f)
        tab = list(reader)
    if len(tab[0]) == 3 and tab[0]:
        entete= tab.pop(0)
        if entete == ["subject","target","link"]: # pour gephy
            tab = list(map(lambda x: [x[0], x[2], x[1]], tab))
            db.addFacts(tab)
        elif entete == ["subject","link","goal"]:
            db.addFacts(pd.DataFrame(tab, columns=entete))

def fromCSVTable(name, columnid, entity):#entity is the classe/type of the tuple
    with open(name) as f:
        reader = csv.reader(f)
        tab = list(reader)
    entete= tab.pop(0)
    #print("entete: ", entete)
    if columnid in entete:
        columnNumber= entete.index(columnid)
        for line in tab:
            subject= line[columnNumber]
            do_add(subject+" is "+entity)
            for cNumber,column in enumerate(line):
                link= entete[cNumber]
                goal= line[cNumber]
                if cNumber != columnNumber:
                    do_add(subject+" "+link+" \""+goal+"\"")

def fromPredicatFile(MyPrompt, name):
     f = open(name, "r")
     for line in f.readlines():
         cleanline = line.replace("\n", "")
         if len(cleanline) > 0 and cleanline[0:1] != "#":
             MyPrompt.onecmd(cleanline)
