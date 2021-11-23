def run(variable,terminal):
    # Algoritma CYK

    # Input variable production dan terminal dalam bentuk di bawah
    # di split pada tanda ->. Pasangan LHS dan RHS
    # variable = [['S', 'AB'], ['S', 'BC'], ['A', 'BA'], ['B', 'CC'], ['C', 
    # 'AB']]
    # terminal = [['A', 'a'], ['B', 'b'], ['C', 'a']]

    # Test input
    # input = ['print','(','x','x',')']
    
    # input = ['a','a','=','3']
    
    # input = ['if','x','>','3',':','import','n','u','m','p','y']
    
    # input = ['while','true',':','x','x','=','3']
    
    input = ['def', 'd', '(', 'x', ')',':','if','x','==','2',':','b','=','3']

    # input = ['def', 'd', '(', 'x', ')', ':', 'if', 'x', '>', '0', ':', 'x','=', '0', 'elif', 'x', '>', '4',':', 'if', 'true', ':', 'x','=', '3', 'else', ':', 'x','=', '2', 'elif', 'x', '>', '3', ':', 'x','=', '4'] # GABISA
    
    # input = ['if','true',':','a','=','2','else',':','b','=','3'] # GABISA
    
    # INPUT 2
    # string abc dengan jumlah a dan b sama
    # variable = [['S', 'AB'], ['A', 'CD'], ['A', 'CF'], ['B', 'EB'], ['F', 'AD']]
    # terminal = [['B', 'c'], ['C', 'a'], ['D', 'b'], ['E', 'c']]
    # input = "aaabbbc"

    length = len(input)
    # '
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
    print("Production Rule Variable:")
    LHS = [var[0] for var in variable]
    print('LHS:')
    print(LHS)
    RHS = [var[1] for var in variable]
    print('RHS:')
    print(RHS)
    print('\n')
    print("Production Rule Terminal:")
    print(terminal)
    print('\n')

    # Mengisi baris pertama tabel dengan  production rule yang berkoresponden
    for i in range(length):
        for term in terminal:
            if input[i] == term[1]:
                # print(term[0])
                table[0][i].append(term[0])
            
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

    print("CYK Table:")
    for z in range(length):
        # print(z)
        print(table[z])