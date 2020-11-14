# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:41:30 2020
@author: metea
"""

#try axcept yapıları/ hata yapıları
a=10
b=0
a/b
try:
    print(a/b)
except ZeroDivisionError :
    print ("sayı sıfıra bölunmez")
    
def topla(x,y):
    print("toplamları" + x+y)

try:
    print(topla(10,30))
except TypeError:
    print("sıktır et go on")
    