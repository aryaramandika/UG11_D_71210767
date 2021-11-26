import random


def tabakangka(a,b):
    acak=random.randint(a,b)
    global angka
    angka=acak
    print("Apakah ", angka, "?")
    angka=int((a+b)/2)



a=1
b=7
c=int((a+b)/2)

mini=1
maks=7
mulai=input("Untuk memulai program masukkan (-1) untuk memulai: ")
if mulai == "-1":
    tabakangka(mini,maks)
    print("Apakah ", c, "?")
    jawaban=input("Apakah sudah benar? \nLebih kecil (0) \nLebih besar (1) \nbenar (2) \n:")
    if jawaban == "0":
        tabakangka(mini,angka-1)
        tabakangka(a,c-1)
        print("Apakah ", angka, "?")
        print("Jumlah tebakan : 2")
        jawaban=input("Apakah sudah benar? \nLebih kecil (0) \nLebih besar (1) \nbenar (2) \n:")
        if jawaban == "0":
            tabakangka(mini,angka-1)
            tabakangka(a,angka)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "1":
            tabakangka(angka+1,maks)
            tabakangka(angka,c)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "2":
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 2 \nProgram selesai")
    elif jawaban == "1":
        tabakangka(angka+1,maks)
        tabakangka(c+1,b)
        print("Apakah ", angka, "?")
        print("Jumlah tebakan : 2")
        jawaban=input("Apakah sudah benar? \nLebih kecil (0) \nLebih besar (1) \nbenar (2) \n:")
        if jawaban == "0":
            tabakangka(mini,angka-1)
            tabakangka(c,angka)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "1":
            tabakangka(angka+1,maks)
            tabakangka(angka,b)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "2":
            print("Jumlah tebakan : 2 \nProgram selesai")