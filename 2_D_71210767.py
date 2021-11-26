kata = input("Masukkan sebuah kata/kalimat :")
sisip = input("Masukkan karakter yang ingin disisipkan :")

def huruf():
    huruf = kata.upper()
    print(sisip.join(list(huruf)))
def kalimat():
    huruf = kata.title()
    print(sisip.join(huruf.split()))
huruf()
kalimat()