import sqlite3
from sqlite3 import Error

CREATE_FACTS= """ CREATE TABLE facts(
                  "subject" TEXT,
                  "link" TEXT,
                  "goal" TEXT
                ); """

CREATE_RULES= """ CREATE TABLE rules(
                  "id" INTEGER NOT NULL PRIMARY KEY,
                  "premises" TEXT,
                  "conclusion" TEXT
                  );"""

CREATE_UNIQUE_INDEX_RULES= """ create unique index facts_subject_link_goal on facts (subject,link,goal); """
CREATE_UNIQUE_INDEX_FACTS= """create unique index rules_premise_conclusion on rules (premises,conclusion);"""
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
            pass
        finally:
            if conn:
                conn.close()

    def createTablesIfNotExist(self):
        try:
           self.c.execute(CREATE_FACTS) 
           self.c.execute(CREATE_RULES) 
           self.c.execute(CREATE_UNIQUE_INDEX_FACTS) 
           self.c.execute(CREATE_UNIQUE_INDEX_RULES) 
        except Error as e:
            pass

    def sqlQuery(self, sql):
        tab= []
        res= self.c.execute(sql)
        for ligne in res:
            tab.append(list(ligne))
        return tab

    def sqlModify(self, sql):
        res= self.c.execute(sql)
        self.conn.commit()
