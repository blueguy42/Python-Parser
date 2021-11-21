import os
import re 

# cwd = os.getcwd()

def parser(filename):
    with open(filename, encoding="utf8") as f:
        stripped = f.read().split() # Split input di spasi ke dalam list
        
        # Operator yang didekomposisi
        operator = ['+','-','*','/','=','>=','<=','==','!=','%','**','//','(',')',"'",'"',':','.',',']
        # Mengembalikan operator dengan tambahan spasi. ex: '+' menjadi ' + '
        operatorReplace = [' {} '.format(elem) for elem in operator]
        
        result = stripped
        # Mengganti operator dengan operator replace
        for content,contentReplace in zip(operator,operatorReplace):
                result = [string.replace(content,contentReplace) for string in result]
                
        # Split lagi spasi pada list
        result = [word for token in result for word in token.split()]
            
        # print(result)
        # print(len(result))
    return result

def parser_line(filename):
    with open(filename, encoding="utf8") as f:
        stripped = f.readlines() # Split input di spasi ke dalam list
        new = []
        for elmt in stripped:
            new.append(elmt)
        # print(stripped)
        # for lines in f.readlines():
        #     new = new.append(lines)
        # print(new)
        
        # Operator yang didekomposisi
        operator = ['+','-','*','/','=','>=','<=','==','!=','%','**','//','(',')',"'",'"',':','.',',']
        # Mengembalikan operator dengan tambahan spasi. ex: '+' menjadi ' + '
        operatorReplace = [' {} '.format(elem) for elem in operator]
        
        result = new
        # Mengganti operator dengan operator replace
        for content,contentReplace in zip(operator,operatorReplace):
            # result = [string.replace(content,contentReplace) for token in result for string in token]
            result = [string.replace(content,contentReplace) for string in result]
        # print(result)
                
        # Split lagi spasi pada list
        for index, item in enumerate(result):
            # for i in range(len(result[index])):
            result[index] = result[index].split()
        
        print(result)
    return result

# Usage    
# print(parser("test1.txt")) # ini one line
print("\n")
parser_line("test1.txt") # ini per line, tapi aturan def sama do_something gaperlu beda bracket lagi, jadinya satu bracket untuk 1 line aja

