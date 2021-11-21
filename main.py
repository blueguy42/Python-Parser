import cyk_parser 
import py_parser
import os
# current_directory = os.getcwd()
# print(current_directory)
# f = open("grammar.txt")
# cyk = cyk_parser.Parser('c:/Users/FikriRanjabi/Desktop/Tubes Clean/TBFO-Parser/grammar.txt',"I shot an elephant in my pajamas")
# cyk.print_tree()

input = py_parser.parser("test1.txt")

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
        
        
# Driver code    
# s = ['Geeks', 'for', 'Geeks']
# print(listToString(s)) 

inputCyk = listToString(input)
print(inputCyk)