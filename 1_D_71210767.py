a = input("Masukkan string :")
def string(a):
    if a.isdigit():
        angka=int(a)
        if angka%2==0:
            angka=int(angka/2)
            print(angka)
        else:
            angka=int((angka+5)/2)
            print(angka)
    else:
        a =a[::-1]
        print(a)
string(a)