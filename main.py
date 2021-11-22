import cyk_parser 
import py_parser
import os

# current_directory = os.getcwd()
# print(current_directory)

def listToString(s): 
    str1 = "" 
    return (str1.join(s))

input = py_parser.parser("test1.txt")
input_multiline = py_parser.parser_line("test1.txt")

inputCyk = listToString(input)
print('\n')
print("Oneliner input for CYK:")
print(inputCyk)
print('\n')
print("Multiline input for CYK:")
print(input_multiline)