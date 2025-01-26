
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "0'a bolme islemi yapilamaz!"
    else:
        return a / b
    
while True:
    print("1. Toplama\n2. Cikarma\n3. Carpma\n4. Bolme\n5. Cikis")
    secim = input("Secim yapiniz: ")

    if secim == '5':
        break

    if secim not in ["1","2","3","4"]:
        print("Gecersiz secim")
    
    sayi1 = float(input("Birinci sayiyi girin: "))
    sayi2 = float(input("Ikinci sayiyi girin: "))

    if secim == '1':
        sonuc = topla(sayi1, sayi2)
    elif secim == '2':
        sonuc = cikar(sayi1, sayi2)
    elif secim == '3':
        sonuc = carp(sayi1, sayi2)
    elif secim == '4':
        sonuc = bol(sayi1, sayi2)

    print("Sonuç:", sonuc)
