#website= "http://www.sadikturan.com"
#course = "python kursu : baştan sona 40 saatlik ders rehberi"
# print(len(course))
# print(website[len(website)-3:])
# print(course[:15])
# print(course[len(course)-15:len(course)])
#print(website[::-1]) tersden yazdırma


# name = "METIN"
# surname = "ALPSRLAN"
# age = 32
# job ="Pyhton Devoloper"
# print ("My name is "+ name +" "+
# surname + " I am " + str(age)+ 
# " yearsold and my jop is " + job)
#result = f'My name is {name} {surname}, my jop is "{job}"    '
#print(result.upper())
#print(result.lower())
#print(result.title())
#print(result.capitalize())
#print(result.upper().strip()) #kullanıcının girdiği bilginin başında boşlukvarsa  on temizler
#print(result.split()) # cumleyi kelimere böler dizi oluşturur. her birine ayrı ayrı ulasabiliriz.
#print(result.upper().split()[1:4] )
#print(result.upper().split(','))
#print('***'.join(result.upper().split()))
#print(result.find('jop')) mesaj içinde jop kelimesinin kcncı indexde baslıyor
#print(result.startswith('h')) bu mesaj h ile mi baslıyor true/false döner
#print(result.endswith('H')) H İLE Mİ BİTİYOR ?
#print(result.replace(' ', '-').replace('ç','c').replace('ş','s')) #turkce karekterleri ingilizceye cevirme fonksiyonu
#a = " Hello_My_Wolrd.com"
#print(a)
#print(a.center(50,'*')) metni tam ortalayck sekilde etrafına karekter koyduk.
#print(a.strip())
#print(a.count('l'))
#print(a.startswith('M'))
#print(a.endswith('d'))
#print(a.replace('Hello','MERHABA')) CUMLE İÇİNDE HELLO YERİNE MERHABA YAZAR
#print(a.find('d')) d harfinin index yerini bulmak için
#print(a.count('o',0,10)) 0 ile 10 arasında   var mı
#print(a.li('_W'))
#print(a.rindex('.cmo'))
#print(course.islower())
# print(a.center(50,'*'))
# print(a.ljust(50,'*'))
# print(a.rjust(50,'*'))
# print(result.replace(' ','-'))
# print(a.replace('Wolrd','dünya'))
# my_list= ['one','two','tree','four']
# my_list2 = ['5','4','7']
# print(my_list +my_list2)
# print(len(my_list2+my_list))
# print((my_list+my_list2)[3])
#userb= ['berk',25]
#print([usera,userb]) bu şekilde yazdırısak her liste içinde liste saklamıs olruz
#print([usera,userb][1][0]) yeni olusturulan t listede liste içinde listenni elemanlarını cagırabilirz
# oto = ['BMW','MERCEDES','OPEL','MAZDA','VOLVO']
# print(len(oto))
# print(oto[len(oto)-1])
#kalemler =(1,25,'ali')
# print(type(kalemler))
# print(kalemler[1])
# LİSTE İLE TUBLE LER AYNI MANTIK FAKAT TUBLE ELEMNALARINDA DEGİŞKLİK İZİN VERMEZ.
# names = kalemler + ('fatima','zehra')
# print(names)
#*****************DİCTİONARY LİST type KEY VALUE OLARAK ÇALIŞIR**********
# plakalar = {'01':'adana','02':'adıyaman','34':'istanbul',
# '27':'gaziantep','79':'kilis','80':'osmaniye','35':'izmir',
# '21':'diyarbakır','06':'ankara'}
# plakalar['30'] = 'yozgat'
# print(plakalar[input('kodu gir:')])
# users = {
#     'metinalp':{
#         'fullname':'METIN ALPARSLAN',
#         'role': ['admin','user'],
#         'mailadress':'metealp79@gmail.com',
#         'adress':'içerenköy mh. didem sk. no:15/1/1 selver kuzey apt.',
#         'phone': '05536197921',
#         'age':'32'},
#     'ebruli':{
#         'fullname':'EBRU ÖZTURK',
#         'role': ['grafiker','user'],
#         'mailadress':'ebruli@gmail.com',
#         'adress':'gülbahar mh.ismini unutugm sk. no 13, d:9 şişli/ist',
#         'phone': '055566662514',
#         'age':'35'}
# }
# print(users[input('kullanıcı adı gir :  ')]['role'])
#ogrenciler = {}
# ogrenciler[number] = {
#         'adı':adsoyad,
#         'yaş': yaş,
#         'telefonu': tel,
#         'sınıfı': sınıf}
#print(f'{number} nolu öğrenci öğrenciler listesine {len(ogrenciler)} eklendi')
# number = input('öğrenci numarası giriniz: ')
# adsoyad = input('öğrenci adınıve soyadını gir: ')
# yaş = input('yaşını giriniz: ')
# tel = input('telefonu giriniz: ')
# sınıf = input('sınıfını giriniz: ')
# ogrenciler.update({number:{
#     'adı':adsoyad,
#     'yaş': yaş,       
#     'telefonu': tel,
#     'sınıfı': sınıf}
# })
# print(f'{number} nolu öğrenci öğrenciler listesine {len(ogrenciler)} inci olarak eklendi')
# number = input('öğrenci numarası giriniz: ')
# adsoyad = input('öğrenci adınıve soyadını gir: ')
# yaş = input('yaşını giriniz: ')
# tel = input('telefonu giriniz: ')
# sınıf = input('sınıfını giriniz: ')
# ogrenciler.update({number:{
#     'adı':adsoyad,
#     'yaş': yaş,       
#     'telefonu': tel,
#     'sınıfı': sınıf}
# })
# print(f'{number} nolu öğrenci öğrenciler listesine {len(ogrenciler)} inci olarak eklendi')
# number = input('öğrenci numarası giriniz: ')
# adsoyad = input('öğrenci adınıve soyadını gir: ')
# yaş = input('yaşını giriniz: ')
# tel = input('telefonu giriniz: ')
# sınıf = input('sınıfını giriniz: ')
# ogrenciler.update({number:{
#     'adı':adsoyad,
#     'yaş': yaş,       
#     'telefonu': tel,
#     'sınıfı': sınıf}
# })
# print(f'{number} nolu öğrenci öğrenciler listesine {len(ogrenciler)} inci olarak eklendi')
# print(ogrenciler)
#*****************   setler (tekrar eden nesneleri teke indirir ve indexlenemzler) **********
# fruits = {'elma','armut','portakal'}
# fruits.add('muz')
# fruits.update(['karpuz','salatalık'])
# print(fruits)
# fruits.pop()
# fruits.discard('salatalık')
# fruits.clear()
# print(fruits)
# for x in fruits:
#     print(x)
# mylist = [1,2,3,3,4,4,6,5,4,6,4,6,7,8,7,4,3]
# print(mylist)
# print(set(mylist))  #tekrar edenler teke indirir setlerin özelliği

#*****************VALUE TYPES*********************
#VALUE TYPES İLGİLENİRKEN VERİNİN KENDİSİYLE,
# x=6
# y =10
# x =y
# y =  15
# print(x,y) # buraday den yapılan degişklk x i etkilemez.

#REFENCE TYPES İLE İLGİLENİRKEN VERİNİN ADRESYLE İLGİLENİYORUZ.
# a = ['ELMA','ARMUT','HIYAR']
# b = ['elma','armut','hıyar']
# a = b
# b[0]='UZUM'
# print(a, b) # B den yapılan degişklik a yı da etkiler. 
# burada önemli olan vale degil adresdir.
#**************************************
#x,y,z = 5,10,15
# x += 5 # x = x+5
# y -= 5 # y = y5
# z/=3 # z = z/3
# x **=3
# y//= 3 
# z%=7
# values = 1,15,30,45
# *x,y,z = values # x in basına yıldzı koyunca fazla olan degerlerı x e dizi şeklinde atar
# print(values)
# print(x[0])
#x,y,z = 2,5,10
#numbers= 1,5,7,10,6
# a = int(input('birinci sayıyı gir: '))
# b = int(input('ikinci sayıyı gir: '))
# print('sonuc: ',  a*b-(x+y+z))
# print(y//x)
# print((x+y+z)%3)
# print(y**x)
# x,*y,z = numbers
# print(z**3)
# print(y[0]+y[1]+y[2])
#***************************KARSILASTIRMA OPARATORLER*********
# a == b, a eşit mi b ? ture /false döner
# a != b, a eşit degil mi b ? eşit değilse true eşitse false döner.
# a = int(input('birinci sayıyı gir: '))
# b = int(input('ikinci sayıyı gir: '))
# if a>b:
#     print('birinci sayı büyüktür.')
# if a<b:
#     print('ikinci sayı daha büyüktur.')
# if a == b :
#     print('sayılar eşittir.')
#a = float(input('vize1 notu gir : '))
#b = int(input('vize2 notu gir : '))
# c = int(input('final notu gir : '))
# d = ((a+b)/2)*0.6 + c*0.4
# if d >= 50:
#     print(f'NOT ORTALAMANIZ: {d} geçtiniz.')
# if d < 50:
#     print(f'NOT ORTALAMANIZ: {d} kaldınız.')
# if a>0:
#     print('pozitif sayı girdiniz')
# if a <0:
#     print('negatif sayı girdiniz')
# if a ==0:
#     print('notr sayı girdiniz')
# eposta = 'metealp79@gmail.com'
#parola = 'Metinalp79'
 #a = input('mail adresinizi giriniz:')
# if a == eposta:
#     print('Mailiniz dogru.')
#     b = input('şifrenizi giriniz: ')
#     if b == parola:
#         print('HOŞGELDİNİZ')
#     if b != parola:
#         print('şifreniz yanlış')
# if a != eposta:
#     print('MailiniZ yanlış efendim.')

# a = int(input('bir sayı giriniz: '))
# result = a>0  and a%2 ==0
# if result == True:
#      print(f'Girdiğiniz sayı istenilen araalıktadır >> {a}')
# else:
#      print(f'Girdiğiniz sayı istenilen şartları sağlamamaktadır >> {a}')
# mail= 'metealp79@gmail.com'
# pasvord = '123456'
# a = input('email adresini gir : ')
# b = input('şifreni gir : ')
# isEmail = (a.strip().lower()== mail)
# isPasvord = (b.strip() == pasvord)
# print(f'mail bilgisi: {isEmail} ')
# print(f'şifre bilgisi : {isPasvord} HOŞGELDİNİZ')
# print(a.strip().lower())
# x = int(input('x degerini giriniz: '))
# y = int(input('y degerini giriniz: '))
# z = int(input('z degerini giriniz: '))
# if x>y  and x>z:
#     if y > z :
#         print('x en buyuk z en kücük y ortancadır.')
#     else:
#         print('x en buyuk y en küçuktur z ortancadır.')

# elif y >x and y>z:
#     if x > z :
#         print('y en buyuk z en kücük x ortancadır.')
#     else:
#         print('y en buyuk x en küçuktur z ortancadır.')

# elif z >y and z>x:
#     if y > x :
#         print('z en buyuk x en kücük y ortancadır.')
#     else:
#         print('z en buyuk z en küçuktur y ortancadır.')

# x= int(input('vize_1 notunu giriniz: '))
# y= int(input('vize_2 notunu giriniz: '))
# z= int(input('final notunu giriniz: '))
# not_ort = (x+y)/2*0.6 +0.4*z
# if not_ort >=50 and z >= 50:
#     print('BAŞARILI BİR ÖGRENCİSİNİZ.BİR UST SINIFA GEÇMEYE HAK KAZANDINIZ. NOT ORTALAMANIZ :',not_ort)
# elif z>= 70:
#     print('BAŞARILI BİR ÖGRENCİSİNİZ.BİR UST SINIFA GEÇMEYE HAK KAZANDINIZ. NOT ORTALAMANIZ :',not_ort)
# else :
#     print('BAŞARSIZSINIZ.NOT ORTALAMANIZ:',not_ort)
# x = float(input('Lütfen boyunuzu giriniz: '))
# y = float(input('Lütfen kilonuzu giriniz: '))
# ort = y/x**2
# if ort > 0 and  ort <= 18.4:
#     print('ÇOK ZAYIFSINIZ. VUCUT KITLE ENDEXİNİZ:',ort )
# elif ort > 18.4 and ort <= 24.9:
#     print('normal ve saglıklısınız.VUCUT KITLE ENDEXİNİZ:', ort)
# elif ort > 24.9 and ort <=29.9:
#     print('Fazla Kilolusunuz. VUCUT KITLE ENDEXİNİZ:', ort)
# elif ort > 29.9:
#     print('HASTA BİR OBEZSİN. VUCUT KITLE ENDEXİNİZ:', ort)
# else:
#     pass
#**********************   is ve in operatorleri  ****************

# x = y= [1,2,3,4]
# z = [1,2,3,4]
# # print(x==z)
# # print(x is not y)
# # print(x is z)
# print (4 not in x)
# if ((input('kullanıcı adını giriniz: ')).lower().strip() == 'metinalp'):

#     if ((input('şifrenizigiriniz: ')).lower().strip() == '123456'):
#         print('HOSGELDİNİZ')
#     else:
#         print('şifrreniz yanlış')
        
# else:
#     print('Kullanıcı adınız hatalı')
# X = input('adınızı ve soyadınız: ')
# y = int(input('yaşınızı giriniz: '))
# z= input('Mezuniyet durmunuz giriniz:')
# if y >=18 and (z.strip().lower()== 'lise' or z.strip().lower()=='üniversite' ):
#     print('EHLİYET ALMAYA HAK KAZANDINIZ.')
# else :
#     print('Ehliyet başvurusu yapamazsınız.')
# import datetime
# simdi = datetime.datetime.now()
# trf_cks_tar = input('aracınızın trafige çıkış tarhini giriniz(2019/01/01): ')
# trf_cks_tar = trf_cks_tar.split('/')
# top_day = datetime.datetime(int(trf_cks_tar[0]),int(trf_cks_tar[1]),int(trf_cks_tar[2]))
# fark = (simdi-top_day).days
# if fark <=360:
#     print('bu sene mauyeneye gitmeyecek')
# elif fark >360 and  fark<=360*2:
#     print('ilk servis zamanı gelmiş.')
# elif fark >360*2 and fark<=360*3:
#     print('ikinci servis zamanı gelmiş.')
# else:
#     print(' üçüncü servis zamanı gelmiş.')

# list =[1,22,55,44,77]
# for t in list:
#     print(t)
# list2 = (23,44,55,77,56,54)
# print(type(list2))
# for i in list2:
#     print(i)
# users = {
#     'user1':{
#         'name': 'metin',
#         'surname': 'alparslan',
#         'age': 32
#             },
#     'user2':{
#         'name': 'ebru',
#         'surname': 'cenk',
#         'age': 35
#             },
#     'user3':{
#         'name': 'ali',
#         'surname': 'türk',
#         'age': 55
#             }
# }
 #tuple = ((1,2,3),(45,55,77))
# for i,h,g in tuple:
#     print(i,h,g)
# plakalar = {1:'ankara',2 :'istanbul', 3 :'kayseri'}
# for x,y in plakalar.items(): #eger itemlere ulasmak istersek plakar.items demek lazım
#     print(x,y)
sayılar=[1,3,5,7,9,11,15,22,27,29]
toplam = 0
# for i in sayılar:
#     if  i%3==0:
#         print(i)
#     toplam +=i
# print('toplam:', toplam)
# for i in sayılar:
#     if i %2 !=0:
#         print(i**2)
# sehirler =['ankara','izmir','manisa','istanbul','rize']
# for i in sehirler:
#     if len(i) <=5:
#         print(i)
# urunler =[
#     {'name':'samsung s6', 'price': 6000},
#     {'name':'huavei p  30', 'price': 5000},
#     {'name':'xomia noe 7', 'price': 4000},
#     {'name':'arcatel v15', 'price': 1500}
# ]
# toplam = 0
# for i in urunler:
#     if i['price'] >= 5000:
#         print(i['price'])
#         toplam += i['price']
# print('toplamları:', toplam)
#******************************while dongusu ********************##
#100 den kuck sayıları ekrana yazdıralım.
# x = 1
# while x <100:
#     if x%14==0:
#         print(f'sayı 7 nin katı: {x}')
#     else:
#         print(f'sayı 7 ye tam bölünmez: {x}')
#     x +=1
# print('bitti...')
import random
x =random.randint(0,100)

y = int(input('lütfen bir sayı giriniz: '))
while y < x:
    y = int(input('sayınızı arttırın: '))
while y > x:
    y = int(input('Lütfen sayınızı azaltın: '))
if x == y:
    print('Dogru tahmin:' , x)

