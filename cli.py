from cmd import Cmd
from modules.compile import *
from modules.network import *
from modules.db import *
from modules.propagation import *
import re
import csv

class MyPrompt(Cmd):
    logo= ""+"|"
    prompt = logo+'normal> '
    intro = "<!>Starting the server<!>"
    use_raw_input= False
    mode = "normal"
    p = re.compile(r'\d+')
    COMPLETIONLIST= []
    d= Data()

    def do_exit(self, inp):
        return True

    def do_mode(self, inp):
        if inp in ["normal","union","sql","grammaire"]:
            self.prompt = self.logo+'%s> ' % inp
            self.mode= inp
        else:
            print("This is note a mode")
            print("Availiable modes: normal, union, sql, grammaire")

    def do_logo(self, inp):
        self.logo= inp+"|"
        self.prompt = self.logo+'%s> ' % self.mode

    def getTable(self, predicatQuery):
        res= self.parserFormat(predicatQuery)
        if res.find("&") != 0: #s'il n'y a pas d'erreur
            sql= union(res)
            res2= self.d.sqlQuery(sql)
        else:
            res2= res[1:]
        return res2

    def do_check(self, inp):
        if self.mode == "normal":
            tab= inp.split(" ")
            title= tab.pop(0)
            if title == "nodes":
                print(self.d.sqlQuery("select distinct subject from facts union select distinct goal from facts;"))
            elif title == "links":
                print(self.d.sqlQuery("select distinct link from facts;"))
            elif title == "rules":
                print(self.d.sqlQuery("select * from rules;"))
            else:
                print(self.getTable("check "+inp))
        elif self.mode == "union":
            res= self.parserFormat("check "+inp)
            if res.find("&") != 0: #s'il n'y a pas d'erreur
                print(union(res))
            else:
                print(res[1:])
        elif self.mode == "grammaire":
            res = self.parserFormat("check "+inp, verbose=True)
            print(res)

    def do_add(self, inp):
        if self.mode == "normal":
            res= self.parserFormat("add "+inp)
            if res.find("&") != 0:
                if res.find("&&rule&&") > -1: # if it's a rule
                    tab= res.split("&&rule&&")
                    self.d.sqlModify("insert or ignore into rules (premises, conclusion) values (\"%s\", \"%s\")" % tuple(tab))
                    retroPropagation(tab)
                else:
                    tab= res.split("&&")
                    self.d.sqlModify("insert or ignore into facts (subject, link, goal) values (\"%s\", \"%s\", \"%s\")" % tuple(tab))
                    if res.find(" ") == -1: # if there isn't any string in the goal
                        propagation(" ".join(tab))
            else:
                print(res[1:])
        elif self.mode == "grammaire":
            res =self.parserFormat("add "+inp, verbose=True)
            print(res)

    def do_rules(self, inp):
        res= self.d.sqlQuery("select * from rules;")
        print(res)

    def do_links(self, inp):
        res= self.d.sqlQuery("select distinct link from facts;")
        print(res)

    def myStr(self, num):
        if num < 10:
            res= "00"+str(num)
        elif num >= 10 and num < 100:
            res= "0"+str(num)
        else:
            res= str(num)
        return res

    def do_listtofact(self, inp):
        tab= inp.split(" ")
        path= tab[0]
        num= int(tab[1])+1
        for i in range(num):
            self.listtofact(path+"/"+self.myStr(i))

    def listtofact(self, inp):
        f = open(inp, "r")
        print(inp)
        lines= f.readlines()
        for i in range(len(lines)-1):
            if lines[i] not in [""," "] and lines[i+1] not in [""," "]:
                fact = (lines[i]+" suit "+lines[i+1]).replace("\n", "")
                print("fact:", fact)
                res =self.parserFormat("add "+fact)
                tab= res.split("&&")
                print("tab:", tab)
                self.d.sqlModify("insert or ignore into facts (subject, link, goal) values (\"%s\", \"%s\", \"%s\")" % tuple(tab))

    def do_apply(self, inp):
        tab= inp.split(" ")
        if len(tab) >= 2:
            if tab[0] == "rules":
                res= self.d.sqlQuery("select * from rules where id in ("+",".join(tab[1:])+");")
            else:
                print("Error bad syntax")
        elif len(tab) == 1:
            if tab[0] == "rules":
                res= self.d.sqlQuery("select * from rules;")
        print("rules selected: ", res)
        for r in res:
            retroPropagation(r[1:])

    def default(self, inp):
        if self.mode == "normal":
            self.normal(inp)
        elif self.mode == "union":
            self.union(inp)
        elif self.mode == "sql":
            self.sql(inp)
        elif self.mode == "grammaire":
            parser.parse(inp,debug=True)
        else:
            print("This mode can't produce anything: try mode normal")

    def do_export(self, inp):
        tab= inp.split(" ")
        if len(tab) == 3 and tab[0] == "to" and tab[1] in ["csv", "gephy"]:
            if inp.find(".csv") == -1:
                inp += ".csv"
            self.toCSV(tab[2],tab[1])
        else:
            print("Bad sytax. \nRight format: 'export to [format] [name]'")
            print("[format]: csv or gephy")

    def do_import(self, inp):
        self.fromCSV(inp) 

    def do_clear(self, inp):
        self.d.sqlModify("delete from facts")
        tab= inp.split(" ")
        if len(tab) == 2 and tab[1] == "all":
            self.d.sqlModify("delete from rules")
        print("database cleared!")

    def do_rename(self, inp):
        #["nodes or links", "old", "new"]
        tab= inp.split(" ")
        if len(tab) == 3:
            if tab[0] == "nodes":
                self.d.sqlModify("update facts set subject='"+tab[2]+"' where subject='"+tab[1]+"'")
                self.d.sqlModify("update facts set goal='"+tab[2]+"' where goal='"+tab[1]+"'")
            elif tab[0] == "links":
                self.d.sqlModify("update facts set link='"+tab[2]+"' where link='"+tab[1]+"'")
            else:
                print("Bad syntax. It should be: 'rename [target] [oldname] [newname]")
                print("[target]= nodes or links")

    def getPredicat(self,exp):
        res= exp
        if exp.find(" filter ") > -1:
            res= exp[:exp.find(" filter ")+1]
        elif exp.find(" get ") > -1:
            res= exp[:exp.find(" get ")+1]
        return res

    def getFacts(self, tab, predicat):
        facts=[]
        for ligne in tab:
            res= self.completePredicat(ligne, predicat)
            tabFacts= self.splitOneDimension(res)
            for fact in tabFacts:
                facts.append(fact.split(" "))
        return facts

    def do_display(self, inp):
        tab= self.getTable("check "+inp)
        predicat= self.getPredicat(inp)
        #getting the result
        facts= self.getFacts(tab,predicat)
        displayNetwork(facts)
        writeCSV(facts, "append.csv")

    def do_append(self, inp):
        tab= self.getTable("check "+inp)
        predicat= self.getPredicat(inp)
        facts= self.getFacts(tab,predicat)
        with open("append.csv") as f:
            reader = csv.reader(f)
            oldFacts = list(reader) # cette table est déjà formatée
        facts += oldFacts
        displayNetwork(facts)
        writeCSV(facts, "append.csv")

    def completePredicat(self, ligne, pred):
        substitution= getVariables(pred.split(" "))
        if len(substitution) > 0:
            for i in range(len(ligne)):
                pred= pred.replace(substitution[i], ligne[i])
        return pred

    def splitOneDimension(self, inp):
        final= []
        tab1= inp.split(" or ")
        for t1 in  tab1:
            tab2= t1.split(" and ")
            for t2 in tab2:
                final.append(t2)
        return final

    def do_delete(self, inp):
        tab= inp.split(" ")
        title= tab.pop(0)
        if title == "rules":
            self.deleteRules(",".join(tab))
        else:
            tab= self.getTable("check "+inp)
            predicat= self.getPredicat(inp)
            #getting the result
            facts= self.getFacts(tab,predicat)
            for fact in facts:
                sql= "delete from facts where subject='%s' and link='%s' and goal='%s'" % tuple(fact)
                self.d.sqlModify(sql)


    def deleteRules(self, numbers):
        print("delete ("+numbers+")")
        self.d.sqlQuery("delete from rules where id in ("+numbers+")")

    def sql(self,inp):
        try:
            print(self.d.sqlQuery(inp))
        except:
            print("Error this is not a sql query")

    def union(self, inp):
        print(union(inp))

    def normal(self,inp):
        print("Bad syntax")

    def parserFormat(self, command, verbose=False):
        parser.parse(command, debug=verbose)
        f= open("res.txt", "r")
        res= f.readlines()[0]
        f.close()
        return res

    def toCSV(self, name, csvFormat):
        if csvFormat == "gephy":
            tab= self.d.sqlQuery("select subject,goal,link from facts;")
            tab.insert(0, ["source","target","link"])
        else:
            tab= self.d.sqlQuery("select * from facts;")
            tab.insert(0, ["subject","link","goal"])
        with open(name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tab)

    def fromCSV(self, name):
        with open(name) as f:
            reader = csv.reader(f)
            tab = list(reader)
        try:
            if len(tab[0]) == 3 and tab[0]:
                entete= tab.pop(0)
                print("entete: ", entete)
                if entete == ["subject","target","link"]: # pour gephy
                    for t in tab:
                        addFact(" ".join([t[0],t[2],t[1]]))
                elif entete == ["subject","link","goal"]:
                    for t in tab:
                        addFact(" ".join(t))
        except:
            print("The csv file has not the good format: ('subject,target,link' or 'subject,goal,link')")

    def completedefault(self,text, line, begidx, endidx):
        nodes= self.d.sqlQuery("select subject from facts where subject like '"+text+"%' union select goal from facts where goal like '"+text+"%' and goal not like '% %';")
        tab= []
        for n in nodes:
            tab.append(n[0])
        return tab

MyPrompt().cmdloop()
