
from tkinter import *

def hesap():
     t = kutu.get()
     j= int(t)
     #print ("Girilen Sayı " + str(j))
     yazi2.config( text = str(j))
  
    

pencere = Tk()
pencere.title("Maas Hesap Tablosu")
#pencere.geometry("600*500+100+100")


yazi = Label(pencere)
yazi.config(text =  u"Hosgeldiniz")

yazi2 = Label(pencere)
yazi2.config(text =  u"lütfen maasınızı giriniz: ")
yazi2.pack()

kutu = Entry(pencere)
kutu.pack()

buton =Button(pencere)
buton.config(text = "Hesapla" , command = hesap)
buton.pack()

mainloop()

