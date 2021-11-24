def parser(filename):
    with open(filename, encoding="utf8") as f:
        stripped = f.read().split() # Split input di spasi ke dalam list
        
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

    return result
