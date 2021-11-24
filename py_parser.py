import os
import re 

# Initial state
def stateP(string):
    # alphabet that allows transition from P to Q
    PtoQ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
    # check if string is empty
    if(len(string)==0):
        return False
    # process first input      
    else: 
        if (string[0] in PtoQ):
            # input is True, recursively check rest of strings
            return stateQ(string[1:]) 
        else:
            return False

# Final state         
def stateQ(string):
    # alphabet that allows transition from Q to Q
    QtoQ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789'
    # check if string is empty
    if(len(string)==0):
        return True
    # process first input
    else:  
        if (string[0] in QtoQ):
            # input is True, recursively check rest of strings
            return stateQ(string[1:])
        else:
            return False

# NFA
def accepts(string, initial):
    return initial(string)


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
        # a = []

        # comment = False
        # for i in stripped:
        #     if i in ["'''",'"""','"',"'"] and not comment:
        #         a.append(i)
        #         comment = True
        #     elif i in ["'''",'"""','"',"'"] and comment:
        #         comment = False
        #         a.append('string')

        #     if not comment:
        #             a.append(i)
        # stripped = a

        
        comparison = ['>','>=','<','<=','==','!=']
        assignment = ['=','+=','-=','*=','+=','-=','*=','/=','%=','//=','**=']
        other_ops = ['(',')',"'",'"',':','.',',','%','**','//','+','-','*','/']
        # Operator yang didekomposisi
        operator = ['>','>=','<','<=','==','!=','+=','-=','*=','+=','-=','*=','/=','%=','//=','**=','%','**','//','+','-','*','/','=','(',')',"'",'"',':','.',',']
        # Mengembalikan operator dengan tambahan spasi. ex: '+' menjadi ' + '
        operatorReplace = [' {} '.format(elem) for elem in operator]
        
        result = stripped
        # Mengganti operator dengan operator replace
        for content,contentReplace in zip(operator,operatorReplace):
                result = [string.replace(content,contentReplace) for string in result]
        
        # Split lagi spasi pada list
        result = [word for token in result for word in token.split()]

        # a = []
        # print(result)
        # for i in result:
        #     if i in terminals or i=="comment":
        #         a.append(i)
        #     elif is_number(i):
        #         a.append("number")
        #     else:
        #         # if accepts(i,stateP):
        #         a.append("variable")
        #         # a[i].append('string')
        #         # else:
        #         #     return "Invalid variable name!"
        # result = a
            
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
a = parser("test2.txt") # ini one line
# print(a)
# print("\n")
# print(parser_line("test1.txt")) # ini per line, tapi aturan def sama do_something gaperlu beda bracket lagi, jadinya satu bracket untuk 1 line aja

# # KALO MAU DILANJUTIN KE CYK
# if a != "Invalid variable name!":
#     pass