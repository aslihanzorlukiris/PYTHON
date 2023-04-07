# Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu Mükemmel Sayıdır. 
#Örnek: 1 + 2 + 3 = 6
#Kullanıcıdan aldığı sayıyının mükemmel olup olmadığını söyleyen bir program yazın. 

sayi= int(input("Bir sayı giriniz: "))
toplam = 0
for i in range(1,sayi):
    if sayi % i == 0:
        toplam += i 
if toplam == sayi:
    print("Mükemmel sayı")
else:
    print("Mükemmel sayı değildir")        
