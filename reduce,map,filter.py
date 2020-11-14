#filter,map,reduce fonksiyonlar
a=[1.5,2.3,3.4,4.5]
for i in a:
    print(i*10)
"for döngüsü ile listedeki her sayıyı 10 ile çarptık"

list(map(lambda x: x*10, a ))
#map(vektörel operasyon fonksiyonu) fonksiyonu
#bir nesnenin üzerinde bir(isimsiz)
#fonksiyon çalıştırmamıza imkan sağlar

"""FİLTER FONKSİYONU"""
#BİR LİSTE İÇİNE GİDER BİR ŞARTI SAĞLAYAN DURUMLARI FİLTRELER
#TIPKI İF YAPISI GİBİ ÇALIŞIR
liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
list(filter(lambda x : x%2==0, liste))
#yukarıda ki listenin içinde mod2 ye göre true olan
#sonucları bize filtreledi
"""REDUCE FONKSİYONU"""
#İNDİRGEME İŞLEMİ YAPAR
from functools import reduce #kütüphanede modül import ettik
liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
reduce(lambda a,b: a+b, liste)
#liste içindeki tüm elemanları toplr 
#sonucları da toplar en son degere indrger





