
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCOLADE ADD ALL AND CALC CB CHECK CHECKFROM CLEAR COUNT CP CROCHET CSB CSV DATE DELETE DISPLAY DOT EQUAL EXEC FILTER FLOAT INF LIMIT LINKS LIST MAP MAX MEAN MIN MINUS NAME NOT NUMBER OB OP OSB PARAMETER PARENTHESE PLOT PLUS PRED PREDEXT PRINT REFERENCE RENAME RESUME SELECT SHUFFLE SLICE SORT STR STRING STRINGCONTAINS STRINGEQUAL STRINGNOTEQUAL SUM SUP VARexp : cmds\n           | type\n           | comparators\n           | csvfile\n           | pred\n           cmds : cmd mcmdmcmd : mcmd : cmd mcmdcmd : CHECK type\n           | CHECK ALL\n           | ADD type\n           | DELETE type\n           | FILTER comparators\n           | DATE contour\n           | DATE NAME contour\n           | FLOAT contour\n           | STR contour\n           | EXEC contour\n           | EXEC NAME\n           | EXEC contour contour\n           | EXEC NAME contour\n           | CSV csvfile\n           | DISPLAY content\n           | PRINT contour\n           | COUNT\n           | SHUFFLE\n           | MEAN VAR\n           | MAX VAR\n           | MIN VAR\n           | RESUME VAR\n           | CALC contour\n           | CALC NAME contour\n           | CALC contour contour\n           | CALC NAME contour contour\n           | SELECT contour\n           | SELECT element contour\n           | REFERENCE element\n           | RENAME NAME contour contour\n           | RENAME NAME element element\n           | MAP ADD contour contour\n           | MAP contour contour\n           | SLICE contour contour\n           | LIST contour\n           | LIST NAME contour\n           | CLEAR\n           | SUM VAR\n           | SUM contour\n           | LIMIT NUMBER\n           | SORT contour\n           | LINKS contour\n           | PLOT contour\n           contour : PARENTHESE\n               | CROCHET\n               | ACCOLADEcontent : typecontent :comparators : comparator conjcomparatorcomparator : variable compnext\n                  | element compnextcompnext : symbol variable\n                | symbol elementcompnextelement : symbol elementconjcomparator : AND comparator conjcomparator\n    conjcomparator : symbol : EQUAL EQUAL\n              | INF EQUAL\n              | SUP EQUAL\n              | INF\n              | SUP\n              | STRINGEQUAL\n              | STRINGNOTEQUAL\n              | STRINGCONTAINS\n              type : element\n             | variable\n             | fact\n             | setvariable : VARelement : NUMBER\n               | NAME\n               | STRINGfact : element element elementset : set_fact conjsetset_fact : set_fact_classic\n                | set_fact_with_not\n    set_fact : fact\n                  set_fact_classic : set_element set_element set_element\n                        | element element VAR\n                  set_fact_with_not : NOT set_element set_element set_element\n                     | set_element NOT set_element set_element\n                     | set_element set_element NOT set_element\n                     | set_element set_element set_element NOT\n                     set_fact_with_not : element element set_element NOT\n                         | element element NOT set_element\n                     set_element : element\n                   | VAR\n    conjset : conjset : AND set_fact conjset\n    csvfile : NAME DOT CSVpred : NAME DOT PREDEXTname_type : NAME typevariables : VARvariables : VAR morevariablesmorevariables : VAR morevariablesmorevariables : VARargs : elementargs : element moreargsmoreargs : element moreargsmoreargs : element'
    
_lr_action_items = {'NAME':([0,8,13,14,15,16,17,18,19,22,23,28,32,33,34,35,38,42,46,50,51,54,56,57,59,60,61,62,63,66,72,101,114,115,116,117,118,119,124,127,128,129,141,148,150,151,152,161,],[13,56,-79,69,56,56,56,56,81,88,56,-95,97,56,56,101,106,-78,-80,56,56,56,-79,56,-68,-69,-70,-71,-72,56,56,56,56,56,56,-94,-95,56,56,-65,-66,-67,56,56,56,56,56,56,]),'CHECK':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[15,15,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,15,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'ADD':([0,7,10,11,12,23,25,26,28,36,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[16,16,-75,-76,-64,-56,-25,-26,-77,102,-45,-78,-80,-96,-83,-84,16,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'DELETE':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[17,17,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,17,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'FILTER':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[18,18,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,18,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'DATE':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[19,19,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,19,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'FLOAT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[20,20,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,20,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'STR':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[21,21,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,21,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'EXEC':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[22,22,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,22,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'CSV':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,67,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,133,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[14,14,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,14,-59,-79,-58,-57,131,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,131,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'DISPLAY':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[23,23,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,23,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'PRINT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[24,24,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,24,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'COUNT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[25,25,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,25,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'SHUFFLE':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[26,26,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,26,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'MEAN':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[27,27,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,27,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'MAX':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[29,29,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,29,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'MIN':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[30,30,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,30,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'RESUME':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[31,31,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,31,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'CALC':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[32,32,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,32,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'SELECT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[33,33,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,33,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'REFERENCE':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[34,34,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,34,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'RENAME':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[35,35,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,35,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'MAP':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[36,36,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,36,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'SLICE':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[37,37,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,37,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'LIST':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[38,38,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,38,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'CLEAR':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[39,39,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,39,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'SUM':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[40,40,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,40,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'LIMIT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[41,41,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,41,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'SORT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[43,43,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,43,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'LINKS':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[44,44,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,44,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'PLOT':([0,7,10,11,12,23,25,26,28,39,42,46,47,48,49,52,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,121,122,125,126,130,131,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[45,45,-75,-76,-64,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,45,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-81,-87,-60,-61,-64,-98,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'NUMBER':([0,8,13,15,16,17,18,23,28,33,34,41,42,46,50,51,54,56,57,59,60,61,62,63,66,72,101,114,115,116,117,118,119,124,127,128,129,141,148,150,151,152,161,],[42,42,-79,42,42,42,42,42,-95,42,42,109,-78,-80,42,42,42,-79,42,-68,-69,-70,-71,-72,42,42,42,42,42,42,-94,-95,42,42,-65,-66,-67,42,42,42,42,42,42,]),'STRING':([0,8,13,15,16,17,18,23,28,33,34,42,46,50,51,54,56,57,59,60,61,62,63,66,72,101,114,115,116,117,118,119,124,127,128,129,141,148,150,151,152,161,],[46,46,-79,46,46,46,46,46,-95,46,46,-78,-80,46,46,46,-79,46,-68,-69,-70,-71,-72,46,46,46,46,46,46,-94,-95,46,46,-65,-66,-67,46,46,46,46,46,46,]),'VAR':([0,8,13,15,16,17,18,23,27,28,29,30,31,40,42,46,50,51,54,56,57,59,60,61,62,63,66,72,114,115,116,117,118,119,124,127,128,129,148,150,151,152,161,],[28,-94,-79,28,28,28,79,28,92,-95,93,94,95,107,-78,-80,118,118,122,-79,79,-68,-69,-70,-71,-72,79,-94,118,118,118,-94,-95,118,118,-65,-66,-67,-94,118,118,118,122,]),'NOT':([0,8,13,15,16,17,23,28,42,46,50,54,56,72,114,115,117,118,121,122,123,148,149,161,],[51,-94,-79,51,51,51,51,-95,-78,-80,116,124,-79,-94,51,150,-94,-95,-94,-95,153,-94,162,124,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,23,25,26,28,39,42,46,47,48,49,52,53,55,56,64,65,68,70,71,72,73,74,75,76,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,100,105,107,108,109,110,111,112,113,117,118,120,121,122,125,126,130,131,132,134,135,136,137,138,139,143,144,145,146,147,149,153,154,155,156,157,158,159,160,162,163,164,165,],[0,-1,-2,-3,-4,-5,-7,-73,-74,-75,-76,-64,-79,-56,-25,-26,-77,-45,-78,-80,-96,-83,-84,-7,-6,-59,-79,-58,-57,-22,-9,-10,-73,-74,-11,-12,-13,-77,-14,-52,-53,-54,-16,-17,-18,-19,-23,-55,-24,-27,-28,-29,-30,-31,-35,-37,-43,-46,-47,-48,-49,-50,-51,-82,-94,-95,-8,-81,-87,-60,-61,-64,-98,-99,-15,-20,-21,-33,-32,-36,-41,-42,-44,-96,-85,-86,-92,-93,-63,-34,-38,-39,-40,-97,-91,-90,-89,-88,]),'EQUAL':([8,9,13,28,42,46,56,58,59,60,77,78,79,],[58,58,-79,-77,-78,-80,-79,127,128,129,58,58,-77,]),'INF':([8,9,13,28,42,46,56,77,78,79,],[59,59,-79,-77,-78,-80,-79,59,59,-77,]),'SUP':([8,9,13,28,42,46,56,77,78,79,],[60,60,-79,-77,-78,-80,-79,60,60,-77,]),'STRINGEQUAL':([8,9,13,28,42,46,56,77,78,79,],[61,61,-79,-77,-78,-80,-79,61,61,-77,]),'STRINGNOTEQUAL':([8,9,13,28,42,46,56,77,78,79,],[62,62,-79,-77,-78,-80,-79,62,62,-77,]),'STRINGCONTAINS':([8,9,13,28,42,46,56,77,78,79,],[63,63,-79,-77,-78,-80,-79,63,63,-77,]),'AND':([10,12,42,46,47,48,49,55,56,64,79,117,118,121,122,125,126,130,146,147,149,153,154,162,163,164,165,],[-85,66,-78,-80,114,-83,-84,-59,-79,-58,-77,-94,-95,-81,-87,-60,-61,66,114,-85,-86,-92,-93,-91,-90,-89,-88,]),'DOT':([13,69,],[67,133,]),'ALL':([15,],[71,]),'PARENTHESE':([19,20,21,22,24,32,33,36,37,38,40,42,43,44,45,46,56,81,82,83,84,87,88,96,97,99,101,102,103,104,106,138,140,142,],[82,82,82,82,82,82,82,82,82,82,82,-78,82,82,82,-80,-79,82,-52,-53,-54,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'CROCHET':([19,20,21,22,24,32,33,36,37,38,40,42,43,44,45,46,56,81,82,83,84,87,88,96,97,99,101,102,103,104,106,138,140,142,],[83,83,83,83,83,83,83,83,83,83,83,-78,83,83,83,-80,-79,83,-52,-53,-54,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'ACCOLADE':([19,20,21,22,24,32,33,36,37,38,40,42,43,44,45,46,56,81,82,83,84,87,88,96,97,99,101,102,103,104,106,138,140,142,],[84,84,84,84,84,84,84,84,84,84,84,-78,84,84,84,-80,-79,84,-52,-53,-54,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'PREDEXT':([67,],[132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,],[1,]),'cmds':([0,],[2,]),'type':([0,15,16,17,23,],[3,70,74,75,90,]),'comparators':([0,18,],[4,76,]),'csvfile':([0,14,],[5,68,]),'pred':([0,],[6,]),'cmd':([0,7,52,],[7,52,52,]),'element':([0,8,15,16,17,18,23,33,34,50,51,54,57,66,72,101,114,115,116,119,124,141,148,150,151,152,161,],[8,54,72,72,72,78,72,99,100,117,117,121,126,78,54,141,148,117,117,117,117,158,161,117,117,117,121,]),'variable':([0,15,16,17,18,23,57,66,],[9,73,73,73,77,73,125,77,]),'fact':([0,15,16,17,23,114,],[10,10,10,10,10,147,]),'set':([0,15,16,17,23,],[11,11,11,11,11,]),'comparator':([0,18,66,],[12,12,130,]),'set_fact':([0,15,16,17,23,114,],[47,47,47,47,47,146,]),'set_fact_classic':([0,15,16,17,23,114,],[48,48,48,48,48,48,]),'set_fact_with_not':([0,15,16,17,23,114,],[49,49,49,49,49,49,]),'set_element':([0,15,16,17,23,50,51,54,114,115,116,119,124,150,151,152,161,],[50,50,50,50,50,115,119,123,50,149,151,152,154,163,164,165,123,]),'mcmd':([7,52,],[53,120,]),'compnext':([8,9,77,78,],[55,64,64,55,]),'symbol':([8,9,77,78,],[57,57,57,57,]),'conjcomparator':([12,130,],[65,155,]),'contour':([19,20,21,22,24,32,33,36,37,38,40,43,44,45,81,87,88,96,97,99,101,102,103,104,106,138,140,142,],[80,85,86,87,91,96,98,103,104,105,108,110,111,112,134,135,136,137,138,139,140,142,143,144,145,156,157,159,]),'content':([23,],[89,]),'conjset':([47,146,],[113,160,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> cmds','exp',1,'p_exp','typeParser.py',154),
  ('exp -> type','exp',1,'p_exp','typeParser.py',155),
  ('exp -> comparators','exp',1,'p_exp','typeParser.py',156),
  ('exp -> csvfile','exp',1,'p_exp','typeParser.py',157),
  ('exp -> pred','exp',1,'p_exp','typeParser.py',158),
  ('cmds -> cmd mcmd','cmds',2,'p_cmds','typeParser.py',164),
  ('mcmd -> <empty>','mcmd',0,'p_mcmd0','typeParser.py',173),
  ('mcmd -> cmd mcmd','mcmd',2,'p_mcmd1','typeParser.py',178),
  ('cmd -> CHECK type','cmd',2,'p_cmd','typeParser.py',187),
  ('cmd -> CHECK ALL','cmd',2,'p_cmd','typeParser.py',188),
  ('cmd -> ADD type','cmd',2,'p_cmd','typeParser.py',189),
  ('cmd -> DELETE type','cmd',2,'p_cmd','typeParser.py',190),
  ('cmd -> FILTER comparators','cmd',2,'p_cmd','typeParser.py',191),
  ('cmd -> DATE contour','cmd',2,'p_cmd','typeParser.py',192),
  ('cmd -> DATE NAME contour','cmd',3,'p_cmd','typeParser.py',193),
  ('cmd -> FLOAT contour','cmd',2,'p_cmd','typeParser.py',194),
  ('cmd -> STR contour','cmd',2,'p_cmd','typeParser.py',195),
  ('cmd -> EXEC contour','cmd',2,'p_cmd','typeParser.py',196),
  ('cmd -> EXEC NAME','cmd',2,'p_cmd','typeParser.py',197),
  ('cmd -> EXEC contour contour','cmd',3,'p_cmd','typeParser.py',198),
  ('cmd -> EXEC NAME contour','cmd',3,'p_cmd','typeParser.py',199),
  ('cmd -> CSV csvfile','cmd',2,'p_cmd','typeParser.py',200),
  ('cmd -> DISPLAY content','cmd',2,'p_cmd','typeParser.py',201),
  ('cmd -> PRINT contour','cmd',2,'p_cmd','typeParser.py',202),
  ('cmd -> COUNT','cmd',1,'p_cmd','typeParser.py',203),
  ('cmd -> SHUFFLE','cmd',1,'p_cmd','typeParser.py',204),
  ('cmd -> MEAN VAR','cmd',2,'p_cmd','typeParser.py',205),
  ('cmd -> MAX VAR','cmd',2,'p_cmd','typeParser.py',206),
  ('cmd -> MIN VAR','cmd',2,'p_cmd','typeParser.py',207),
  ('cmd -> RESUME VAR','cmd',2,'p_cmd','typeParser.py',208),
  ('cmd -> CALC contour','cmd',2,'p_cmd','typeParser.py',209),
  ('cmd -> CALC NAME contour','cmd',3,'p_cmd','typeParser.py',210),
  ('cmd -> CALC contour contour','cmd',3,'p_cmd','typeParser.py',211),
  ('cmd -> CALC NAME contour contour','cmd',4,'p_cmd','typeParser.py',212),
  ('cmd -> SELECT contour','cmd',2,'p_cmd','typeParser.py',213),
  ('cmd -> SELECT element contour','cmd',3,'p_cmd','typeParser.py',214),
  ('cmd -> REFERENCE element','cmd',2,'p_cmd','typeParser.py',215),
  ('cmd -> RENAME NAME contour contour','cmd',4,'p_cmd','typeParser.py',216),
  ('cmd -> RENAME NAME element element','cmd',4,'p_cmd','typeParser.py',217),
  ('cmd -> MAP ADD contour contour','cmd',4,'p_cmd','typeParser.py',218),
  ('cmd -> MAP contour contour','cmd',3,'p_cmd','typeParser.py',219),
  ('cmd -> SLICE contour contour','cmd',3,'p_cmd','typeParser.py',220),
  ('cmd -> LIST contour','cmd',2,'p_cmd','typeParser.py',221),
  ('cmd -> LIST NAME contour','cmd',3,'p_cmd','typeParser.py',222),
  ('cmd -> CLEAR','cmd',1,'p_cmd','typeParser.py',223),
  ('cmd -> SUM VAR','cmd',2,'p_cmd','typeParser.py',224),
  ('cmd -> SUM contour','cmd',2,'p_cmd','typeParser.py',225),
  ('cmd -> LIMIT NUMBER','cmd',2,'p_cmd','typeParser.py',226),
  ('cmd -> SORT contour','cmd',2,'p_cmd','typeParser.py',227),
  ('cmd -> LINKS contour','cmd',2,'p_cmd','typeParser.py',228),
  ('cmd -> PLOT contour','cmd',2,'p_cmd','typeParser.py',229),
  ('contour -> PARENTHESE','contour',1,'p_contour','typeParser.py',244),
  ('contour -> CROCHET','contour',1,'p_contour','typeParser.py',245),
  ('contour -> ACCOLADE','contour',1,'p_contour','typeParser.py',246),
  ('content -> type','content',1,'p_content1','typeParser.py',251),
  ('content -> <empty>','content',0,'p_content2','typeParser.py',256),
  ('comparators -> comparator conjcomparator','comparators',2,'p_is_comparators','typeParser.py',261),
  ('comparator -> variable compnext','comparator',2,'p_is_comparator','typeParser.py',270),
  ('comparator -> element compnext','comparator',2,'p_is_comparator','typeParser.py',271),
  ('compnext -> symbol variable','compnext',2,'p_is_comparator2','typeParser.py',276),
  ('compnext -> symbol element','compnext',2,'p_is_comparator2','typeParser.py',277),
  ('compnextelement -> symbol element','compnextelement',2,'p_is_comparator3','typeParser.py',282),
  ('conjcomparator -> AND comparator conjcomparator','conjcomparator',3,'p_conjcomparator2','typeParser.py',287),
  ('conjcomparator -> <empty>','conjcomparator',0,'p_conjcomparator','typeParser.py',297),
  ('symbol -> EQUAL EQUAL','symbol',2,'p_symbol','typeParser.py',302),
  ('symbol -> INF EQUAL','symbol',2,'p_symbol','typeParser.py',303),
  ('symbol -> SUP EQUAL','symbol',2,'p_symbol','typeParser.py',304),
  ('symbol -> INF','symbol',1,'p_symbol','typeParser.py',305),
  ('symbol -> SUP','symbol',1,'p_symbol','typeParser.py',306),
  ('symbol -> STRINGEQUAL','symbol',1,'p_symbol','typeParser.py',307),
  ('symbol -> STRINGNOTEQUAL','symbol',1,'p_symbol','typeParser.py',308),
  ('symbol -> STRINGCONTAINS','symbol',1,'p_symbol','typeParser.py',309),
  ('type -> element','type',1,'p_is_type','typeParser.py',315),
  ('type -> variable','type',1,'p_is_type','typeParser.py',316),
  ('type -> fact','type',1,'p_is_type','typeParser.py',317),
  ('type -> set','type',1,'p_is_type','typeParser.py',318),
  ('variable -> VAR','variable',1,'p_is_variable','typeParser.py',323),
  ('element -> NUMBER','element',1,'p_is_element','typeParser.py',328),
  ('element -> NAME','element',1,'p_is_element','typeParser.py',329),
  ('element -> STRING','element',1,'p_is_element','typeParser.py',330),
  ('fact -> element element element','fact',3,'p_is_fact','typeParser.py',335),
  ('set -> set_fact conjset','set',2,'p_is_set0','typeParser.py',340),
  ('set_fact -> set_fact_classic','set_fact',1,'p_is_set1','typeParser.py',349),
  ('set_fact -> set_fact_with_not','set_fact',1,'p_is_set1','typeParser.py',350),
  ('set_fact -> fact','set_fact',1,'p_is_set1_0','typeParser.py',356),
  ('set_fact_classic -> set_element set_element set_element','set_fact_classic',3,'p_is_set2','typeParser.py',363),
  ('set_fact_classic -> element element VAR','set_fact_classic',3,'p_is_set2','typeParser.py',364),
  ('set_fact_with_not -> NOT set_element set_element set_element','set_fact_with_not',4,'p_is_set3','typeParser.py',374),
  ('set_fact_with_not -> set_element NOT set_element set_element','set_fact_with_not',4,'p_is_set3','typeParser.py',375),
  ('set_fact_with_not -> set_element set_element NOT set_element','set_fact_with_not',4,'p_is_set3','typeParser.py',376),
  ('set_fact_with_not -> set_element set_element set_element NOT','set_fact_with_not',4,'p_is_set3','typeParser.py',377),
  ('set_fact_with_not -> element element set_element NOT','set_fact_with_not',4,'p_is_set3_0','typeParser.py',391),
  ('set_fact_with_not -> element element NOT set_element','set_fact_with_not',4,'p_is_set3_0','typeParser.py',392),
  ('set_element -> element','set_element',1,'p_is_set4','typeParser.py',402),
  ('set_element -> VAR','set_element',1,'p_is_set4','typeParser.py',403),
  ('conjset -> <empty>','conjset',0,'p_is_set5','typeParser.py',411),
  ('conjset -> AND set_fact conjset','conjset',3,'p_is_set6','typeParser.py',416),
  ('csvfile -> NAME DOT CSV','csvfile',3,'p_is_csv','typeParser.py',426),
  ('pred -> NAME DOT PREDEXT','pred',3,'p_is_pred','typeParser.py',431),
  ('name_type -> NAME type','name_type',2,'p_check_from','typeParser.py',436),
  ('variables -> VAR','variables',1,'p_variable_list0','typeParser.py',441),
  ('variables -> VAR morevariables','variables',2,'p_variable_list1','typeParser.py',446),
  ('morevariables -> VAR morevariables','morevariables',2,'p_variable_list2','typeParser.py',451),
  ('morevariables -> VAR','morevariables',1,'p_variable_list3','typeParser.py',456),
  ('args -> element','args',1,'p_args0','typeParser.py',461),
  ('args -> element moreargs','args',2,'p_args1','typeParser.py',466),
  ('moreargs -> element moreargs','moreargs',2,'p_args2','typeParser.py',471),
  ('moreargs -> element','moreargs',1,'p_args3','typeParser.py',476),
]
