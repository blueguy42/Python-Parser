import os
import re 

# cwd = os.getcwd()

terminals = ['input','print','exit','#','type','global','str','int','float','complex','list','tuple','range','dict','set','bool','bytes',"'",'"',"'''",'"""','(',')','[',']','{','}','+','-','*','/','%','//','**','=','+=','-=','*=','/=','%=','//=','**=','&','^','~','<<','>>','&=','^=','>>=','<<=','==','!=','>','<','>=','<=','and','or','not','is','in','\"','\'','\\','\n','\r','True','False','None','for','while','if','else','elif','pass','break','continue','def','return','class','import','dir','from','as','open','read','readline','close','write',':','.','_',',',';']

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def parser(filename):
    with open(filename, encoding="utf8") as f:
        stripped = f.read().split() # Split input di spasi ke dalam list

        a = []

        comment = False
        for i in stripped:
            if i in ["'''",'"""','"',"'"] and not comment:
                a.append(i)
                comment = True
            elif i in ["'''",'"""','"',"'"] and comment:
                comment = False
                a.append('COMMENT')

            if not comment:
                    a.append(i)
        stripped = a
                
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

        print(result)

        a = []
        for i in result:
            if i in terminals or i=="COMMENT":
                a.append(i)
            elif is_number(i):
                a.append("INTEGER")
            else:
                a.append("VAR")
        result = a
            
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
        # # Mengganti operator dengan operator replace
        for content,contentReplace in zip(operator,operatorReplace):
            # result = [string.replace(content,contentReplace) for token in result for string in token]
            result = [string.replace(content,contentReplace) for string in result]
                
        # Split lagi spasi pada list
        for index, item in enumerate(result):
            # for i in range(len(result[index])):
                result[index] = result[index].split(' ')
                
    return result

# Usage    
a = parser("test1.txt") # ini one line
print(a)
# print("\n")
# print(parser_line("test1.txt")) # ini per line, tapi aturan def sama do_something gaperlu beda bracket lagi, jadinya satu bracket untuk 1 line aja

