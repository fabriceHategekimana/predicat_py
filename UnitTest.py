import unittest
from typeParser import *
from commands import *
from db2 import *
from run import *

class MyTest(unittest.TestCase):
    def testIsElement(self):
        errorMessage= "element unrecognized"
        self.assertEqual(("element", '7'), parser.parse('7'))
        self.assertEqual(("element", '"Hello World!"'), parser.parse('"Hello World!"'))
        self.assertEqual(("element", 'truc'), parser.parse('truc'))

    def testIsVariable(self):
        errorMessage= "variable unrecognized"
        self.assertEqual(("variable", 'A'), parser.parse('A'))
        self.assertEqual(("variable", '_B'), parser.parse('_B'))

    def testIsFact(self):
        errorMessage= "fact unrecognized"
        self.assertEqual(("fact",'a','b','c'), parser.parse('a b c'))
        self.assertEqual(("fact",'"un deux"','3','Quatre'), parser.parse('"un deux" 3 Quatre'))

    def testIsSet(self):
        errorMessage= "set unrecognized"
        self.assertEqual(('set', [(0, 'A', 'b', 'c')]), parser.parse('A b c'))
        self.assertEqual(('set', [(1, 'a', 'b', 'c')]), parser.parse('a b not c'))
        self.assertEqual(('set', [(0, 'a', 'b', 'c'), (0, 'A', 'b', 'C')]), parser.parse('a b c and A b C'))

    def testCommands(self):
        self.assertEqual([('check', ("fact", 'a', 'b', 'c'))], parser.parse('check a b c'))
        self.assertEqual([('add', ("fact", 'a', 'b', 'c'))], parser.parse('add a b c'))
        self.assertEqual([('delete', ("fact", 'a', 'b', 'c'))], parser.parse('delete a b c'))
        self.assertEqual([('check', ('fact', 'a', 'b', 'c')), ('add', ('fact', 'a', 'b', 'c'))], parser.parse('check a b c add a b c'))

    def testFunctions(self):
        self.assertEqual([1,2,3], removeNOTValue([0,1,2,3]))
        self.assertEqual(["fab","fab"], repetitionColumn([["un", "deux", "trois"], ["quatre", "cinq", "six"]], ["A","B","C"], "fab"))
        self.assertEqual(["un","quatre"], substitutionColumn([["un", "deux", "trois"], ["quatre", "cinq", "six"]], ["A","B","C"], "A"))
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], transpose([[1,2,3],[4,5,6],[7,8,9]]))
        self.assertEqual([['un', 'deux', 'trois'], ['un', 'deux', 'trois']], createFacts([["un", "deux", "trois"], ["quatre", "cinq", "six"]], ["A","B","C"], ("un", "deux", "trois")))
        self.assertEqual([['un', 'fab', 'deux'], ['quatre', 'fab', 'cinq']], createFacts([["un", "deux", "trois"], ["quatre", "cinq", "six"]], ["A","B","C"], ("A", "fab", "B")))
        self.assertEqual([['un', 'deux', 'trois'], ['quatre', 'cinq', 'six']], substitute([[["un","deux"],["trois","quatre"]], ["A","B"]], [(0, "un", "deux", "trois"), (1, "quatre","cinq","six")]))

    def testSQLManager(self):
        #db= Data()
        #db.addInHistory("socrate est mortel")
        #self.assertEqual([['1', 'socrate est mortel']], db.getHistory())
        #db.clearHistory()
        #self.assertEqual([], db.getHistory())

        #self.assertEqual(0, db.getStage())
        #db.addStage()
        #self.assertEqual(1, db.getStage())
        #db.clearStage()
        #self.assertEqual(0, db.getStage())
        
        #adding two rules
        #db.addRules(["fred","jami"], ["ami"], [""], "blablabla")
        #db.addRules(["fred","jami"], ["ami"], [""], "blobloblo")
        #deleting the two rules
        #db.deleteRules([0,1])
        #db.clearStage()
        pass

    def testScenario(self):
        db= Data()
        #db.addFacts(["fred ami jami".split(" ")])
        #facts= [["fred","ami","jami"]]
        #print(db.removeRepetitiveFacts(facts))

    def testRun(self):
        self.assertEqual(["un","Bca"], getValueOnly(["un","A", "C", "B", "Bca"]))
        #self.assertEqual(0, getRules(["A ami B"]))
        #self.assertEqual(0, db.getRulesByArgs("","ami",""))
        #runRule("check A ami B and B enemi C add A ennemi B")
        #print(db.getRules())
        #print(propagation())
        self.assertEqual("check A ami B and B ennemi C delete A ami B and B ennemi C", syntaxSugarCommand("delete A ami B and B ennemi C"))
        self.assertEqual("check A ami B add B ami A", syntaxSugarRule("if A ami B then B ami A"))
        #print(parser.parse("A ami B"))
        
unittest.main()
