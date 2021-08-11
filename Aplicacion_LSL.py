# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:41:55 2021

@author: USUARIO
"""

from Listas_Ligadas import LSL
from Nodo_Simple import nodoSimple
import random

a = LSL()
b = LSL()

"""PRUEBA 1"""

#Los datos ingresan en desorden.
d = int(input("Ingrese un número diferente de 0: "))
while d != 0:
    d = random.randint(0, 20)
    #d = int(input("Ingrese un número diferente de 0: "))
    a.agregarDato(d)

    
#Los datos ingresan en orden.  
d = int(input("\nIngrese un número diferente de 0: "))    
while d != 0:
    d = random.randint(0, 20)
    #d = int(input("Ingrese un número diferente de 0: "))
    y = b.buscarDondeInsertar(d)    
    b.insertar(d,y)

print("")    
a.recorrerLista()
print("")    
b.recorrerLista()


#Para conocer el tamaño de la lista
tamagno_a = a.longitud()
tamagno_b = b.longitud()

print("")
print("\nLongitud de la lista a: ", tamagno_a)
print("\nLongitud de la lista b: ", tamagno_b)


#Buscar un dato en las listas
dato_buscar_a = int(input("Ingrese el dato que desea buscar en la primera lista: "))
dato_buscar_b = int(input("Ingrese el dato que desea buscar en la segunda lista: "))

y = nodoSimple()
y_1 = nodoSimple()

nodo_a = a.buscarDato(dato_buscar_a, y)
nodo_b = b.buscarDato(dato_buscar_b, y_1)

print("")
print("Nodo dato lista a: ", nodo_a)
print("Nodo dato lista b: ", nodo_b)


#Borrar un dato de la lista
a.borrar(nodo_a, y)
b.borrar(nodo_b, y_1)

tamagno_a = a.longitud()
tamagno_b = b.longitud()

print("")
print("\nLongitud de la lista a: ", tamagno_a)
print("\nLongitud de la lista b: ", tamagno_b)

print("")
print("\nLista a después de borrar el dato: ")   
a.recorrerLista()
print("") 
print("\nLista b después de borrar el dato: ")    
b.recorrerLista()
 

""" PRUEBA 2"""

print("\na es vacía?",a.esVacia())

p = a.primerNodo()

d = input("Entre más datos: ")
while d != "0":
    a.agregarDato(d)
    d = input("Entre más datos: ")

print("\n")
a.recorrerLista()
l = a.longitud()
print(l)

for i in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    a.agregarDato(i)

print("\n")
print("antes de borrar por primera vez:")
a.recorrerLista()
print()

y = nodoSimple()
x = a.buscarDato("A", y)
a.borrar(x, y)
print("\n")
print("despues de borrar primera vez")
a.recorrerLista()
print()

y = nodoSimple()
x = a.buscarDato("I", y)
a.borrar(x, y)
print("\n")
print("despues de borrar segunda vez:")
a.recorrerLista()
print()

y = nodoSimple()
x = a.buscarDato("Z", y)
a.borrar(x, y)
print("\n")
print("despues de borrar tercera vez:")
a.recorrerLista()
print()

l = a.longitud()
print("\nlongitud:", l)

x = a.primerNodo()
a.borrar(x, None)
print("\n")
print("despues de borrar cuarta vez")
a.recorrerLista()
l = a.longitud()
print(l)

x = a.buscarDato("z", y)
a.borrar(x)
print("\n")
print("despues de borrar terceraquinta vez")
a.recorrerLista()
l = a.longitud()
print(l)
