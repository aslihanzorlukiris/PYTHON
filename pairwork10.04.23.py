def calculator ():
    sayi1 = int(input("Bir sayı giriniz: "))
    sayi2 = int(input("Bir sayı giriniz: "))
    toplam = sayi1 + sayi2
    carpim = sayi1 * sayi2
    cikarma = sayi1 - sayi2
    bolme = sayi1 / sayi2
    mod = sayi1 % sayi2

    islem = input("İşlem seçiniz:")
    if islem == "+":
        print(toplam)
    elif islem == "-":
        print(cikarma)
    elif islem == "/":
        print(bolme)
    elif islem == "*":
        print(carpim)
    elif islem == "%":
        print(mod)
    else :
        print("Hatalı seçim")

cikis = input("Çıkmak istiyorsanız 'q' basın.")
while cikis != 'q':
    calculator()
    cikis = input("Çıkmak istiyorsanız 'q' basın.")
    
    


        
        
        
