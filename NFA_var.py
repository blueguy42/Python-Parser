def stateP(string):
    # 
    PtoQ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
    #
    if(len(string)==0):
        return False
          
    else: 
        if (string[0] in PtoQ):
            return stateQ(string[1:]) 
        else:
            return False
         
def stateQ(string):
    QtoQ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789'
    if(len(string)==0):
        return True
          
    else:  
        if (string[0] in QtoQ):
            return stateQ(string[1:])
        else:
            return False

#take input
var = input()
  
print(stateP(var))