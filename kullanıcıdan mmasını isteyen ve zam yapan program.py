"""maaslar = [2560,2850,2980,3115,3200,3340,3350,3500,4200]
maası 3220 tl üzerinde olanlara %4 zam yapılacak
Maası 3220 tl altında olanlara %6
kullanıcadan maas bilgisi iste ve zam lı sonucu göster."""


x = input("lütfen maasınızı giriniz: ")
k= int(x)

def yeni_maas(k):
    print(str(k) + " TL olan eski maaşınız %6 zam ile " +str(k*6/100 + k) + " TL' olacaktır.")
    return False
def yeni_ucret(k):
        print(str(k) + " TL olan eski maaşınız %4 zam ile " +str(k*4/100 + k) + " TL' olacaktır.")
    
if k > 3250 :
    yeni_ucret(k)
else:
    yeni_maas(k)
