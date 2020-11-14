# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 07:09:13 2020
@author: metea
"""
#Vektörel  çarpım nesne yönelimli prgarmda döngü ile yapılır
a= [5,8,4,6,7]
b= [4,5,15,10,3]
ab=[]
for i in range(0,len(a)):
    ab.append(a[i]*b[i])
 ab   
#şimdide fonk.programlamada nasıl yapıdgına bakalım
# import ile modül cagırırz kutuphaneden
 
import numpy as nb
a= nb.array([5,8,4,6,7])
b= nb.array([4,5,15,10,3])
a*b
