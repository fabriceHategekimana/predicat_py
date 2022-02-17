from cmd import Cmd
from db2 import *
from run import *
from import_module import *

# version 2
class MyPrompt(Cmd):
    #defining variables for i in  the display
    logo = ""+"|"
    prompt = logo+'normal> '
    intro = "<!>Starting the NEW server<!>"
    use_raw_input = False
    mode = "normal"
    COMPLETIONLIST = []

    def default(self, inp):
        if self.mode == "union":
            commands = parser.parse(inp, debug=False)
            print(commands)
        elif self.mode == "sql":
            if inp[0:7] == "select":
                print(db.sqlQuery(inp))
            else:
                db.sqlModify(inp)
        else:
            run(inp)

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

    def do_export(self, inp):
        """to do an 'export to csv/gephy' """
        tab= inp.split(" ")
        if len(tab) == 3 and tab[0] == "to" and tab[1] in ["csv", "gephy"]:
            if inp.find(".csv") == -1:
                inp += ".csv"
            toCSV(tab[2],tab[1])
        else:
            print("Bad sytax. \nRight format: 'export to [format] [name]'")
            print("[format]: csv or gephy")

    def do_import(self, inp):
        tab= inp.split(" ")
        if tab[0] == "csv":
            fromCSV(tab[1]) 
        elif tab[0] == "predicat":
            fromPredicatFile(self, tab[1])
        elif tab[0] == "csvtable":
            if len(tab) == 4 and tab[2] == "id":
                csvfile= tab[1]
                entity= csvfile.replace(".csv","")
                columnid= tab[3]
                fromCSVTable(csvfile, columnid, entity)

    def do_test(self, inp):
        commands = db.sqlQuery("select body from rules where body like '%print%'")
        for command in commands:
            run(command[0])

    def do_reset(self, inp):
        db.sqlModify("DELETE FROM facts")
        db.sqlModify("DELETE FROM rules")
        db.sqlModify("DELETE FROM historical")
        db.sqlModify("DELETE FROM stage")
        db.sqlModify("INSERT INTO stage (stage) values (0)")

    def do_context(self, inp):
        if inp == "":
            print(db.getContext())
        else:
            tab = inp.split(" ")
            if tab[0] == "select":
                if len(tab) > 1:
                    db.setDefaultTable(tab[1])
                else:
                    print("error: you must specify an context table name")
            elif tab[0] == "selected":
                print(db.getDefaultTable())
            elif tab[0] == "create":
                if len(tab) > 1:
                    db.createContext(tab[1])
                else:
                    print("error: you must specify an context table name")

    def completedefault(self, text, line, begidx, endidx):
        table = db.getDefaultTable()
        query = f"select subject from facts_{table} where subject like '{text}%' union select goal from facts_{table} where goal like '{text}%' and goal not like '% %' union select link from facts_{table} where link like '{text}%';"
        nodes = db.sqlQuery(query)
        tab = []
        for n in nodes:
            tab.append(n[0])
        return tab


MyPrompt().cmdloop()
