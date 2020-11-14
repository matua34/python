# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:50:35 2020
@author: metea
"""
"""
print ("hello ai era")
type(8)
type(5.4)
type("hello si era")"""
#sayılar ve dizinler
"""
type("125")
"a"+"b"
"a " "b"
"a" -"b"
"a"*5
"a "*7
"""
#METHOTLAR İŞLEC BELİRLİ GÖREVLERİ YERİNE GETİRİR
"""len("alican")
a= "gelecge merhaba de"
b= 'come on'
a=9
b=6
^#del a
len("gelecegi yazanlar")"""
a="gelecegi yazanlar"
#upper ve lover islower isupper methotları
"""a.upper()
a.lower()
b=a.upper()
b.islower()
a.islower()
b.isupper()"""
#replace methodu
"""c=a.replace("e","ü")
a"""
#strip fonksiyonu ön tanımlı olarak boslugu siler
"""a= "gelecegi yazmayanlar"
a.strip("e")
dir(a)"""
#dir fonksiyonu uygulancak fonksiyonları
#gösterir
# SUBSTRING
"""a[20]
a[0:3]
a[3:7]
k=(2+3j)"""
#tip dönüşümü type change
"""int(v) + int(k)
type(12)

type("12")
str(12)
type(str(12))
float(11)
int(11.755)"""
#listeler[] veya list()
notlarım =[1,15,26,45,78,54]
yeni_depo = ("ali", 10, 40, 55.45,'cem', notlarım)
type(yeni_depo)
tum_list = [notlarım,yeni_depo]

notlarım
tum_list[0]
yeni_depo[1:]
yeni_notlar = [1, 15, 26, "kk", 78]
len(yeni_notlar[3])
yeni_notlar[4]
yeni_depo[4]= "cemin_babası"
yeni_notlar[3]='alinin_babası'
yeni_notlar[1]="cano"
yeni_notlar[0:2]= "karot","canonun tostosu"
yeni_notlar
yeni_notlar=yeni_notlar+ ["kask"]
yeni_notlar
#del(yeni_notlar)[2]
#APPEND VE REMOVE METHOTLARI
yeni_notlar.append("meto")
yeni_notlar.remove("meto")

yeni_notlar.insert(len(yeni_notlar),"ebruliskom")
len(yeni_notlar)
yeni_notlar
del(yeni_notlar[len(yeni_notlar)-1])

k = ("meto", 6 , 6.5)
k=(1,2,3,'turkey')
kk= [22,44,"can"]
#del(k)
#SÖZLÜKLER SIRASIZDIR,DEĞİŞTİRLEBİLİR,KAPSAYICIDIR
"""
SÖZLÜKLER :SIRASIZ,DEĞİŞİTİLEBİLİR KAPSAYICI,
indexleme yapılamaz.süslü parantez kullanılır
TUPLE LER : SIRALI,DEĞİŞİTİRİLEMEZ, KAPSAYICI,
normal parantez kullanılır
LİST LER : SIRALI DEĞİŞTİRİLEBİLİR, KAPSAYICI
köşeli parantez kullanılır.
"""
sozluk= { "K" : [60,70,80],
          "M" : [90,100,'£'],
          "T" : ["met", 'tt',50,70]}

new_sozluk= { "K" : {"k1": [60,70,80],
                     "k2": [50,20,30],
                     "k3": [10,40,90]},

              "M" : {"m1": [90,100,'£'],
                     "m2": [95,105,'##'],
                     "m3": [40,45,55]},
          
              "T" : {"t1": ['tt',50,70],
                     "t2": [22,33,45],
                     "t3": [66,77,99,100.5]
                     }}
sozluk["E"]= 55
sozluk
E=("5",)
T=["5"]
del(E)
sozluk
soz = {  "A": 66,
      "B": 77,
      "C": 88}

del(sozluk)
soz[T]= 22
soz
"""SETLER VERİ YAPILARI 
kümlere benzzerler.
essizdirler
farklı türden veri yapısı barındırabilir.
değiştirilebilir"""
#veriyapıları - setler

"""t=["ali", 22, "veli"]
t="portakalı soydum basucuma koydum """"
T= ["ali", "uzaya", "git"]
# =============================================================================
# a = set(T)
# a
# a.add("ile")
# a
# a.remove("ile")
# a
# t
# T
# a.discard("ile")
# a
# ctrl+4 tusları ile yaptık
# ============================================================================

"""set1 = set([1,2,3,4,5])
set2 = set([3,5,7,8,6])
set1,set2
set1.difference(set2)
set2.difference(set1) set 2 inin set1 den farkı
birlesim=set1.union(set2)   set1 birlesim set2
set1.symmetric_difference(set2) set1 in set2 den farkı
set2-set1
set1.intersection(set2) kumelerin kesişimi
kesisim = set1 & set2
kesisim
birlesim
birlesim - kesisim
set1.intersection_update(set2) kesisim kumsesi
set1 kumesinin elemanları olarak guncellendi
set1"""
# =============================================================================
# set1 = set([1,2,3,4,5])
# set2 = set([3,5,7,8,6])
# 
# set2.isdisjoint(kesisim)
# kesisim.issubset(set1) // kesisim kumesi set1 in alt kumesi mi sorusunu sorar
# set1.issubset(set2)
# kesisim
# set1.issuperset(kesisim) // sest1 kumesi kesisim kumesinin kapsıyor mu true
# 
# 
# 
# =============================================================================


#FONKSİYONLAR NASI YAZILIR... def kullacagız!

#LOCAL VE GLOBAL DEGİSKENLER
x= 10
y= 20
def oranla(x=3,y=5):
    return (x/y)

oranla(x=3,y=5)
oranla(x,y)
#LOCal degisken alanında gobalı etkilemek
"""x=[]

def tosun_ekle(a):
    print(str(a) + " eklendi"),
    return (x.append(a))

tosun_ekle("ali")
tosun_ekle("ebru")

tosun =5000

tosun ==5000"""
#IF YAPISI


    
























