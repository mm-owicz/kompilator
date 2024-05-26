import os
from antlr4 import *
from listener.ExpressionListener import ExpressionListener
from generated.JuvenaliaLexer import JuvenaliaLexer
from generated.JuvenaliaParser import JuvenaliaParser


code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/funcTest1.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/funcTest2.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/funcTest3.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/ifTest1.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/ifTest2.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/repeatTest1.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/repeatTest2.juv")

code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/classTest.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/dynamicTest.juv")
code_file = FileStream("/home/magda/CS/mgstr/JFK/tests2/structTest.juv")

lexer = JuvenaliaLexer(code_file)
stream = CommonTokenStream(lexer)
parser = JuvenaliaParser(stream)
tree = parser.prog()

listener = ExpressionListener() 

walker = ParseTreeWalker()
walker.walk(listener, tree)

os.system('clang-18 code.ll -o res')
cwd = os.getcwd()
os.system(cwd + "/res")

