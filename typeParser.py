import ply.lex as lex
import ply.yacc as yacc

reserved = {
        "not": "NOT",
        "and": "AND",
        "check": "CHECK",
        "add": "ADD",
        "delete": "DELETE",
        "filter": "FILTER",
        "equal": "STRINGEQUAL",
        "notequal": "STRINGNOTEQUAL",
        "pred": "PREDEXT",
        "csv": "CSV",
        "display": "DISPLAY",
        "print": "PRINT",
        "countis": "COUNTIS",
        "count": "COUNT",
        "checkfrom": "CHECKFROM",
        "select": "SELECT",
        "reference": "REFERENCE",
        "contains": "STRINGCONTAINS",
        "rename": "RENAME",
        "max": "MAX",
        "min": "MIN",
        "mean": "MEAN",
        "resume": "RESUME",
        "calc": "CALC",
        "exec": "EXEC",
        "append": "APPEND"
        }

# List of token names.   This is always required
tokens = [
   'NUMBER',
   'NAME',
   'STRING',
   'PARENTHESE',
   'PARAMETER',
   'VAR',
   'EQUAL',
   'INF',
   'SUP',
   'PRED',
   'DOT'
]+list(reserved.values())

# A regular expression rule with some action code


def t_STRING(t):
    r'"([^"\n])*"'
    return t


def t_NUMBER(t):
    r'\d+'
    return t


def t_NAME(t):
    r'([a-zA-Zà]\w+ | [a-zà])'
    t.type = reserved.get(t.value, 'NAME')
    return t


def t_VAR(t):
    r'(_)?[A-Z]'
    return t


def t_PARENTHESE(t):
    r'\(([^)\n])*\)'
    return t


def t_PARAMETER(t):
    r'\$\d'
    return t

# A string containing ignored characters (spaces and tabs)


t_EQUAL = r'='
t_INF = r'<'
t_SUP = r'>'
t_DOT = r'\.'
t_ignore = ' \t'


def t_error(t):
    # Error handling rule
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# start
def p_exp(p):
    '''exp : cmds
           | type
           | comparators
           | csvfile
           | pred
           '''
    p[0] = p[1]


def p_cmds(p):
    '''cmds : cmd mcmd'''
    if p[2] == None:
        res = []
    else:
        res = p[2] 
    p[0]= [p[1]]+res


def p_mcmd0(p):
    '''mcmd : '''
    pass


def p_mcmd1(p):
    '''mcmd : cmd mcmd'''
    if p[2] == None:
        res= []
    else:
        res= p[2] 
    p[0]= [p[1]]+res


def p_cmd(p):
    '''cmd : CHECK type
           | CHECKFROM name_type
           | ADD type
           | DELETE type
           | FILTER comparators
           | CSV csvfile
           | DISPLAY content
           | PRINT STRING
           | COUNTIS compnextelement
           | COUNT
           | MEAN VAR
           | MAX VAR
           | MIN VAR
           | RESUME VAR
           | CALC STRING
           | EXEC PARENTHESE
           | EXEC PARENTHESE PARENTHESE
           | APPEND PARENTHESE PARENTHESE
           | APPEND PARENTHESE PARENTHESE PARENTHESE
           | SELECT variables
           | REFERENCE element
           | RENAME args
           '''
    if p[1] == "exec":
        if len(p[1:]) == 2:
            p[0] = ("exec", (p[2][1:-1], ""))
        else:
            p[0] = ("exec", (p[2][1:-1], p[3][1:-1]))
    if p[1] == "append":
        if len(p[1:]) == 3:  # (expression, variables, columns)
            p[0] = ("append", (p[2][1:-1], "", p[3][1:-1]))
        else:
            p[0] = ("append", (p[2][1:-1], p[3][1:-1], p[4][1:-1]))
    elif len(p[1:]) < 2:
        p[0] = (p[1], "void")
    else:
        p[0] = (p[1], p[2])


def p_content1(p):
    '''content : type'''
    p[0] = p[1]


def p_content2(p):
    '''content :'''
    pass


def p_is_comparators(p):
    '''comparators : comparator conjcomparator'''
    if p[2] == None:
        res = []
    else:
        res = p[2]
    p[0] = ("comparators", [p[1]] + res)


def p_is_comparator(p):
    '''comparator : variable compnext
                  | element compnext'''
    p[0] = (p[1][1], p[2][0], p[2][1])


def p_is_comparator2(p):
    '''compnext : symbol variable
                | symbol element'''
    p[0] = [p[1], p[2][1]]


def p_is_comparator3(p):
    '''compnextelement : symbol element'''
    p[0]= [p[1], p[2][1]]


def p_conjcomparator2(p):
    '''conjcomparator : AND comparator conjcomparator
    '''
    if p[3] == None:
        res= []
    else:
        res= p[3]
    p[0]= [p[2]] + res


def p_conjcomparator(p):
    '''conjcomparator : '''
    pass


def p_symbol(p):
    '''symbol : EQUAL EQUAL
              | INF EQUAL
              | SUP EQUAL
              | INF
              | SUP
              | STRINGEQUAL
              | STRINGNOTEQUAL
              | STRINGCONTAINS
              '''
    p[0]= "".join(p[1:])


def p_is_type(p):
    '''type : element
             | variable
             | fact
             | set'''
    p[0] = p[1]


def p_is_variable(p):
    '''variable : VAR'''
    p[0] = ("variable", p[1])


def p_is_element(p):
    '''element : NUMBER
               | NAME
               | STRING'''
    p[0] = ("element", p[1])


def p_is_fact(p):
    '''fact : element element element'''
    p[0] = ("fact", p[1][1], p[2][1], p[3][1])


def p_is_set0(p):
    '''set : set_fact conjset'''
    if p[2] == None:
        res= []
    else:
        res= p[2]
    p[0] = ("set", [p[1]] + res)


def p_is_set1(p):
    '''set_fact : set_fact_classic
                | set_fact_with_not
    '''
    p[0]= p[1]


def p_is_set1_0(p):
    '''set_fact : fact
                  '''
    p[0]= (0,) + p[1][1:]


#the element element VAR is to fill a hole during the parsing LR(1)
def p_is_set2(p):
    '''set_fact_classic : set_element set_element set_element
                        | element element VAR
                  '''
    if type(p[1]) == tuple:
        p[1]= p[1][1]
        p[2]= p[2][1]
    p[0]= (0, p[1], p[2], p[3])


#the element element VAR NOT is to fill a hole during the parsing LR(1), the next line too
def p_is_set3(p):
    '''set_fact_with_not : NOT set_element set_element set_element
                     | set_element NOT set_element set_element
                     | set_element set_element NOT set_element
                     | set_element set_element set_element NOT
                     '''
    if p[1] == "not":
        res = (p[2], p[3], p[4])
    elif p[2] == "not":
        res = (p[1], p[3], p[4])
    elif p[3] == "not":
        res = (p[1], p[2], p[4])
    elif p[4] == "not":
        res = (p[1], p[2], p[3])
    p[0]= (1,)+res


def p_is_set3_0(p):
    '''set_fact_with_not : element element set_element NOT
                         | element element NOT set_element
                     '''
    if p[3] == "not":
        res = (p[1][1],p[2][1],p[4])
    elif p[4] == "not":
        res = (p[1][1],p[2][1],p[3])
    p[0]= (1,)+res


def p_is_set4(p):
    '''set_element : element
                   | VAR
    '''
    if type(p[1]) == tuple:
        p[1] = p[1][1]
    p[0]= p[1]


def p_is_set5(p):
    '''conjset : '''
    pass


def p_is_set6(p):
    '''conjset : AND set_fact conjset
    '''
    if p[3] == None:
        res= []
    else:
        res= p[3]
    p[0]= [p[2]] + res


def p_is_csv(p):
    '''csvfile : NAME DOT CSV'''
    p[0]= ("csv file", p[1]+p[2]+p[3])


def p_is_pred(p):
    '''pred : NAME DOT PREDEXT'''
    p[0] = ("pred", p[1]+p[2]+p[3])


def p_check_from(p):
    '''name_type : NAME type'''
    p[0] = ("check_from", p[1], p[2])


def p_variable_list0(p):
    '''variables : VAR'''
    p[0] = [p[1]]


def p_variable_list1(p):
    '''variables : VAR morevariables'''
    p[0] = [p[1]]+p[2]


def p_variable_list2(p):
    '''morevariables : VAR morevariables'''
    p[0] = [p[1]]+p[2]


def p_variable_list3(p):
    '''morevariables : VAR'''
    p[0] = [p[1]]


def p_args0(p):
    '''args : element'''
    p[0] = [p[1][1]]


def p_args1(p):
    '''args : element moreargs'''
    p[0] = [p[1][1]]+p[2]


def p_args2(p):
    '''moreargs : element moreargs'''
    p[0] = [p[1][1]]+p[2]


def p_args3(p):
    '''moreargs : element'''
    p[0] = [p[1][1]]


# Error rule for syntax errors
def p_error(p):
    pass

# Build the parser
parser = yacc.yacc(debug=True)
