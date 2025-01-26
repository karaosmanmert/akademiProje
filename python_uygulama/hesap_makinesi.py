
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    return a / b
    

while True:
    print("1. Toplama\n2. Cikarma\n3. Carpma\n4. Bolme\n5. Cikis")
    secim = input("Secim yapiniz: ")

    if secim == '5':
        break

    sayi1 = float(input("Birinci sayiyi girin: "))
    sayi2 = float(input("Ikinci sayiyi girin: "))

    if secim == '1':
        print("Sonuc:", sayi1 + sayi2)
    elif secim == '2':
        print("Sonuc:", sayi1 - sayi2)
    elif secim == '3':
        print("Sonuc:", sayi1 * sayi2)
    elif secim == '4':
        if sayi2 != 0:
            print("Sonuc:", sayi1 / sayi2)
        else:
            print("0'a bolme islemi yapilamaz!")
    else:
        print("Gecersiz secim.")

