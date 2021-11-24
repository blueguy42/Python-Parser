import cyk_parser 
import py_parser
import readgrammar 
import sys

inputfile = sys.argv[1]
input = py_parser.parser(inputfile)

print("Oneliner input for CYK:")
print(input)

variable,terminal = readgrammar.read_grammar("cnf.txt")

cyk_parser.run(variable,terminal,inputfile)
