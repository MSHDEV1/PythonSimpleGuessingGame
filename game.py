
#MSHDEV
import random
can = int(input("Kaç Hakkınız olsun: "))

puan = 0

r = random.randint(1,100)

while can > 0:

    liste = [r]
    sayı = int(input("Sayı Tahmin: "))
    liste2 = [sayı]
    can -= 1

    if liste == liste2:
        print("Sayı Doğru")
        puan += can
        r = random.randint(1,100)

    elif can == 0:
        print(f"Hakkınız Bitti Toplam Puanınız = {puan}")

    elif liste2 < liste:
        print("yukarı")
       
    elif liste2 > liste:
        print("Aşagı")



#MSHDEV

        