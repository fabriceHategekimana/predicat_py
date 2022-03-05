import sqlite3
from sqlite3 import Error

CREATE_FACTS= """ CREATE TABLE facts(
                  "subject" TEXT,
                  "link" TEXT,
                  "goal" TEXT,
                  PRIMARY KEY (subject,link,goal)
                ); """

CREATE_RULES = """ CREATE TABLE rules(
                    "id" INTEGER,
                    "source" TEXT,
                    "type" TEXT, 
                    "listener" TEXT, 
                    "body" TEXT);
                    """

CREATE_HISTORICAL = """ CREATE TABLE historical(
                            "stage" TEXT, 
                            "event" TEXT,
                            PRIMARY KEY (event)); 
                    """

CREATE_STAGE = """
CREATE TABLE stage("stage" TEXT); 
"""

CREATE_CONTEXT = """
CREATE TABLE context("name" TEXT); 
"""

CREATE_UNIQUE_INDEX_RULES = """
CREATE UNIQUE INDEX rules_body on rules (body);
"""

CREATE_UNIQUE_INDEX_FACTS= """create unique index fact_subject_link_goal on rules (subject, link, goal);"""

CREATE_UNIQUE_INDEX_HISTORICAL = """
CREATE UNIQUE INDEX historical_event on historical (event);
"""

INITIALYZE_STAGE = """insert into stage (stage) values (0)"""
INITIALYZE_CONTEXT = """insert into context (name) values ('default')"""

class Data(): 
    nom="data.db"

    def __init__(self):
        #Create database if not exist
        self.createDbIfNotExist()
        #Connect database and create a pointer
        self.conn= sqlite3.connect(self.nom)
        self.c= self.conn.cursor()
        #Create table if not exist
        self.createTablesIfNotExist()

    def createDbIfNotExist(self):
        conn= None
        try:
            conn= sqlite3.connect(self.nom)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def createTablesIfNotExist(self):
        try:
           self.c.execute(CREATE_FACTS) 
           self.c.execute(CREATE_RULES) 
           self.c.execute(CREATE_HISTORICAL) 
           self.c.execute(CREATE_STAGE) 
           self.c.execute(INITIALYZE_STAGE) 
           self.conn.commit()
        except Error as e:
            print(e)

    def sqlQuery(self, sql):
        tab= []
        res= self.c.execute(sql)
        for ligne in res:
            tab.append(list(ligne))
        return tab

    def sqlModify(self, sql):
        res= self.c.execute(sql)
        self.conn.commit()

    def addFacts(self, facts):
        """add a list of facts to the database
            entry: [f1,f2,...]
            fn = [subject, link, goal]
        """
        facts = facts.dropna()
        if facts.shape[1] == 3:
            # self.addStage()
            #adding fact in history
            for index, fact in facts.iterrows():
                self.addInHistory(" ".join(fact))
            if facts.empty == False:
                joinedFacts = "('"+facts["subject"]+"','"+facts["link"]+"','"+facts["goal"]+"')"
                modify= "insert or ignore into facts (subject, link, goal) values "+",".join(joinedFacts)+";"
                self.sqlModify(modify)

    def deleteFacts(self, facts):
        """delete list of facts
            entry: [f1,f2,...]
            fn = [subject, link, goal]
        """
        for index, value in facts.iterrows():
            self.sqlModify("delete from facts where subject='"+str(value["subject"])+"' and link='"+str(value["link"])+"' and goal='"+str(value["goal"])+"';")

    def getStage(self):
        """get the actual stage"""
        return int(self.sqlQuery("select * from stage;")[0][0])

    def addStage(self):
        """increment the actual value in the stage"""
        value = self.getStage()
        self.sqlModify("update stage set stage="+str(value+1))

    def clearStage(self):
        """reset the stage to it's initial value (=0)"""
        self.sqlModify("update stage set stage=0")

    def getHistory(self, stage):
        """get the history of the previous event like:
            'add predicat is fun'"""
        return self.sqlQuery("select * from historical where stage="+str(stage)+";")

    def addInHistory(self, event):
        """add a new event in the history"""
        stage = str(self.getStage())
        self.sqlModify("insert or ignore into historical (stage, event) values ('"+stage+"','"+event+"');")

    def clearHistory(self):
        """clear the History, no more data"""
        self.sqlModify("delete from historical")

    def getRules(self):
        """getting the list of rules"""
        return self.sqlQuery("select * from rules;")

    def getRulesByArgs(self, subject, link, goal):
        """get rules that correspond to a given subject, link, goal"""
        return self.sqlQuery("select body from rules where listener like '%"+subject+"%' or listener like '%"+link+"%' or listener like '%"+goal+"%'") 

    def getActualRuleId(self):
        """getting the number of rules"""
        return len(self.sqlQuery("select id from rules"))

    def addRules(self, Type, subjects, links, goals, commands):
        """add rules"""
        actualId= self.getActualRuleId()
        listener = "'"+",".join(subjects)+";"+",".join(links)+";"+",".join(goals)+"'"
        self.sqlModify("insert into rules (id, source, type, listener, body) values ("+str(actualId)+","+"'default'"+","+Type+","+listener+",'"+commands+"')")

    def deleteRules(self, nums):
        """delete specific rules according to an array of index"""
        for num in nums:
            if num == "all":
                self.sqlModify("delete from rules")
            else:
                self.sqlModify("delete from rules where id="+str(num))

    def getLinks(self):
        """get the avaliables links"""
        return self.sqlQuery("select distinct link from facts")

    def getNodes(self):
        """get the avaliables nodes"""
        return self.sqlQuery("select distinct subject from facts union select goal from facts")

    def getCommands(self):
        """actually need to be stored and dynamicaly modified
           retrieve all avaliable commands"""
        # TODO: add the missing commands
        return ["check","add","delete", "filter", "csv", "display", "print"]


