
def calculator():
    print("1. Toplama")
    print("2. Cikarma")
    print("3. Carpma")
    print("4. Bolme")
    
    secim = input("Secim yapiniz (1/2/3/4): ")
    num1 = float(input("Birinci sayiyi girin: "))
    num2 = float(input("Ikinci sayiyi girin: "))
    
    if secim == '1':
        print("Sonuc:", num1 + num2)
    elif secim == '2':
        print("Sonuc:", num1 - num2)
    elif secim == '3':
        print("Sonuc:", num1 * num2)
    elif secim == '4':
        if num2 != 0:
            print("Sonuc:", num1 / num2)
        else:
            print("Hata: Bolme işlemi sifira bolunemez.")
    else:
        print("Gecersiz secim.")

calculator()