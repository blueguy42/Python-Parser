# Parser Bahasa Python
Tugas Besar IF2124 Teori Bahasa Formal dan Otomata

## Daftar Isi
* [Informasi Umum](#informasi-umum)
* [Anggota Kelompok](#anggota-kelompok)
* [Penggunaan](#penggunaan)

## Informasi Umum
Pada Tugas Besar IF2124 Teori Bahasa Formal dan Otomata kali ini kita diminta untuk membuat sebuah program parser/compiler yang dapat menganalisis struktur sintaks dari suatu program yang ditulis pada Bahasa Python dan menentukan apakah program tersebut mempunyai sintaks yang benar atau tidak menurut Python.

## Anggota Kelompok
### Kelompok 2 – Nasgor Jawara
| Nama                           | NIM      |
| ------------------------------ | -------- |
| Muhammad Fikri Ranjabi         | 13520002 |
| Gede Prasidha Bhawarnawa       | 13520004 |
| Ahmad Alfani Handoyo           | 13520023 |

## Penggunaan
Untuk menjalankan program pastikan Python 3 sudah terinstall pada komputer anda, lalu jalankan
```
py parserprogram.py “testcase/<nama file>.py”
```
dengan file .py diletakkan pada folder `/testcase`. Sehingga sebagai contoh bila ingin mengecek program `test1.py` yang sudah ada pada folder `/testcase` jalankan
```
py parserprogram.py “testcase/test1.py”
```

Program akan mengembalikan "Accepted" bila sintaks sudah benar dan "Syntax Error!" bila sintaks salah.

Converter dari CFG ke CNF diambil dari referensi https://github.com/adelmassimo/CFG2CNF yang terdapat pada file `CFG2CNF.py` dan `helper.py` dan dapat digunakan untuk menghasilkan grammar CNF yang terbaru dengan menjalankan
```
py CFG2CNF.py “grammar.txt”
```
dengan grammar CFG diletakkan pada file `grammar.txt` dan hasil grammar CNF disimpan pada file `cnf.txt`.
