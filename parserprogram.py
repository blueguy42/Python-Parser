import cyk_parser 
import py_parser
import readcnf 
import sys

inputfile = sys.argv[1]
input = py_parser.parser(inputfile)

# print("Oneliner input for CYK:")
# print(input)

variable,terminal = readcnf.read("cnf.txt")

cyk_parser.run(variable,terminal,inputfile)
