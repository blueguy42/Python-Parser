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

#take input
var = input()
  
print(accepts(var, stateP))
