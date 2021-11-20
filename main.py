import cyk_parser 
import os
# current_directory = os.getcwd()
# print(current_directory)
# f = open("grammar.txt")
cyk = cyk_parser.Parser('c:/Users/FikriRanjabi/Desktop/Tubes Clean/TBFO-Parser/grammar.txt',"I shot an elephant in my pajamas")
cyk.print_tree()