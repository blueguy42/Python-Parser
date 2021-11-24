import os

def read(filename):
    # Membaca cnf.txt dan menghasilkan variabel dan terminal
    filename = os.path.join(os.curdir, filename)
    with open(filename) as file:
        aturan_list = file.readlines()
        
        var = []
        terminal = []

        for aturan in aturan_list:
            kiri, kanan = aturan.split(" -> ")

            # memecah hasil bila lebih dari satu
            kanan = kanan[:-1].split(" | ")
            for k in kanan:

                # apa bila terminal (direpresentasikan huruf terminal)
                if not(k.isupper()): # bukan kapital maka masuk ke terminal
                    terminal.append([kiri, k])

                # apa bila variabel
                else:
                    var.append([kiri, k.replace(" ", "")])

        return var, terminal