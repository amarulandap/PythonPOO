# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 09:08:31 2021

@author: Andres Marulanda
"""

""" EJERCICIOS VARIOS POO"""

"""1. VECTORES CLASE DERIVADA ALTA PRECISIÓN"""

from Alta_Precision import altaPrecision

a = altaPrecision(20)
b = altaPrecision(20)

a.V=[10,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9]
b.V=[9,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,1]

a.imprime_vector("Vector a")
b.imprime_vector("Vector b")

c = a + b

c.imprime_vector("Vector c = a + b")
print("")
print("len(a.V):",len(a.V))
print("len(b.V):",len(b.V))
print("len(c.V):",len(c.V))
print("a.n:",a.n)
print("b.n:",b.n)
print("c.n:",c.n)


"""2. """














 


