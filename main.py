import cyk_parser 
import py_parser
import os
import readgrammar 

# current_directory = os.getcwd()
# print(current_directory)

def listToString(s): 
    str1 = "" 
    return (str1.join(s))

input = py_parser.parser("test2.txt")
input_multiline = py_parser.parser_line("test1.txt")

# ini input dari test case spek
# inputCyk = listToString(input)
print('\n')
print("Oneliner input for CYK:")
# print(inputCyk)
print(input)
print('\n')
# print("Multiline input for CYK:")
# print(input_multiline)

variable,terminal = readgrammar.read_grammar("cnftest.txt")
# print('vavriable\n')
# print(variable)
# print('terminal\n')
# print(terminal)
# variable = [['S', 'AB'], ['S', 'BC'], ['A', 'BA'], ['B', 'CC'], ['C', 
# 'AB']]
# terminal = [['A', 'a'], ['B', 'b'], ['C', 'a']]

cyk_parser.run(variable,terminal,"test2.txt")