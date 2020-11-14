maaslar = [2560,2850,2980,3115,3200,3340,3350,3500,4200]
#maası 3220 tl üzerinde olanlara %4 zam yapılacak
#Maası 3220 tl altında olanlara %6

def yeni_maas(x):
    print(str(x) + " TL alan personelin"+"Yeni maası: " +str(x*6/100 + x) + " TL' olacaktırdir.")
def yeni_ucret(x):
        print(str(x) + " TL alan personelin"+"Yeni maası: " +str(x*4/100 + x) + " TL' olacaktırdir.")
for i in maaslar:
    if i>3220:
          yeni_ucret(i)
    else:
        yeni_maas(i)