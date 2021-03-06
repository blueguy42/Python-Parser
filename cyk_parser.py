import py_parser
import re 

def run(variable,terminal,filename):
    # Algoritma CYK

    input = py_parser.parser(filename)
    
    # Regex untuk string, number, dan variable
    regexInput = [r'[A-z0-9]*', r'[0-9]*', r'[A-Za-z_][A-Za-z_0-9]*', r'\s']
    regexMap = {
    r'[A-z0-9]*' : ["string"],
    r'[0-9]*' : ["number"],
    r'[A-Za-z_][A-Za-z_0-9]*' : ["variable"],
    r'\s' : ["space"],
    }

    length = len(input)
    
    # Inisialisasi table kosong segitiga atas
    table = [[[] for j in range(length-i)] for i in range(length)]

    def list_duplicate(list,elmt):
    # Mengembalikan list yang berisi indeks elemen list masukan yang bernilai sama dengan elmt masukan
        start_at = -1
        loc = []
        while True:
            try:
                idx = list.index(elmt,start_at+1)
            except ValueError:
                break
            else:
                loc.append(idx)
                start_at = idx
        return loc

    def concatenate(a,b):
    # Mengembalikan set yang berupa hasil concatenate variable a dan b
        result = set()
        if a == set() or b == set():
            return set()
        for elmt_a in a:
            for elmt_b in b:
                result.add(elmt_a+elmt_b)
        return result

    def check_duplicate(list,elmt):
    # Mengembalikan True jika elmt sudah berada di list
        for i in range(len(list)):
            if list[i] == elmt:
                return True

    # LHS dan RHS pada production variable (non terminal)
    LHS = [var[0] for var in variable]
    RHS = [var[1] for var in variable]

    # Mengisi baris pertama tabel dengan  production rule yang berkoresponden
    empty = []
    for i in range(length):
        for term in terminal:
            if input[i] == term[1]:
                table[0][i].extend([term[0]])
        if (table[0][i]):
            continue
        else:
            for term2 in terminal:
                for val in term2: # untuk setiap terminal nya
                    for pattern in regexInput:
                        if ([val] == regexMap[pattern]):
                            if (re.match(pattern, input[i])):
                                table[0][i].extend([term2[0]])
            
    # Mengisi baris kedua sampai baris terakhir pada tabel
    for i in range(1,length):
        for j in range(length-i):
            for k in range(i):
                var_concat = concatenate(table[k][j],table[i-k-1][j+k+1])
                for elmt_RHS in RHS:
                    for elmt in var_concat:
                        if elmt == elmt_RHS:
                            index = list_duplicate(RHS,elmt_RHS)
                            for m in range(len(index)):
                                if check_duplicate(table[i][j],LHS[index[m]]) == True:
                                    continue
                                else:
                                    table[i][j].append(LHS[index[m]])

    # print("CYK Table:")
    # for z in range(length):
    #     print(table[z])
    for elmt in table[length-1]:
        if elmt:
            for char in elmt:
                if (char == 'S') or (char == 'S0'):
                    print("Accepted!")
                    break
        else:
            print("Syntax Error!")
            break