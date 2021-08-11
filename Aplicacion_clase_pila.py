# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:48:16 2021

@author: andre
"""

from Clase_pila import pila_vector
from Clase_pila import pila_LSL
from Clase_pila import pila_lista
import random

def est_pila_vector():
   
    print("ESTRUCTURA PILA COMO VECTOR")
    n = int(input("Ingrese el tamaño de la Pila: "))
    pila_1 = pila_vector(n)
    #Crear una pila de n posiciones con datos numéricos.
    select = int(input("Desea usar la pila completa? 1. SI, 2. NO: \n"))

    if select == 1:
        for i in range(1, n):
            pila_1.apilar_1(n, 1, 10)
    elif select == 2:
        m = int(input("Cuántos campos desea utilizar? "))
        for i in range(1, m):
            pila_1.apilar_1(m, 1, 10)

    pila_1.muestraPila()    

    #Verificar si la pila aun tiene espacio para agregar un dato
    esta_llena = pila_1.lleno()
    if esta_llena == True:
        print("la pila esta llena")
    else:
        i = m
        while i < n:
            d = int(input("\nIngrese el dato que desea agregar: "))
            pila_1.apilar(d)
            pila_1.muestraPila()
        
            select_1 = int(input("Desea agregar mas datos: 1. SI, 2. NO "))
            if select_1 == 1:
                i += 1
            else:
                i = n + 1

    #Retirar un dato de la pila
    pila_1.desapilar()
    print("\nPila después de desapilar: ")
    pila_1.muestraPila()


def est_pila_LSL():
    
    print("\nESTRUCTURA PILA COMO LSL")
    pila_2 = pila_LSL()

    n_1 = int(input("\nCuántos datos desea apilar? "))

    i = 0
    while i < n_1:
        d_1 = input("Ingrese el dato: ")
        pila_2.apilar(d_1)
        i += 1

    pila_2.muestraPila()
    print("")
    pila_2.desapilar()
    print("\nPila después de desapilar: ")
    pila_2.muestraPila()


def est_pila_lista():
    print("\nESTRUCTURA PILA COMO LISTA")

    n_2 = int(input("Ingrese el tamaño de la lista: "))
    pila_3 = pila_lista(n_2)

    select_2 = int(input("Desea usar la lista completa? 1. SI, 2. NO: \n"))

    if select_2 == 1:
        for i in range(0, n_2):
            d_2 = random.randint(1, 10) 
            pila_3.agregar_dato(d_2)
        pila_3.imprimir_lista()

        print("")
        tope = pila_3.mostrar_tope(n_2)
        print("Tope de la lista: ", tope)

        pila_3.eliminar_dato(n_2)
        n_2 -= 1
        print("\nLista después de desapilar: ")
        pila_3.imprimir_lista()
        
        print("")
        tope = pila_3.mostrar_tope(n_2)
        print("Tope de la lista: ", tope)
    
        pila_3.eliminar_dato(n_2)
        n_2 -= 1
        print("\nLista después de desapilar: ")
        pila_3.imprimir_lista()
        
        print("")
        tope = pila_3.mostrar_tope(n_2)
        print("Tope de la lista: ", tope)
   
    elif select_2 == 2:
        m = int(input("Cuántos campos desea utilizar? "))
        for i in range(1, m+1):
            d_2 = random.randint(1, 10)
            pila_3.agregar_dato(d_2) 
        pila_3.imprimir_lista()
        
        print("")
        tope = pila_3.mostrar_tope(m)
        print("Tope de la lista: ", tope)

        pila_3.eliminar_dato(m)
        m -= 1
        print("\nLista después de desapilar: ")
        pila_3.imprimir_lista()

        print("")
        tope = pila_3.mostrar_tope(m)
        print("Tope de la lista: ", tope)
        
        pila_3.eliminar_dato(m)
        m -= 1
        print("\nLista después de desapilar: ")
        pila_3.imprimir_lista()
        
        print("")
        tope = pila_3.mostrar_tope(m)
        print("Tope de la lista: ", tope)

print("Menu principal: ")
print("1. Pila como objeto vector.")
print("2. Pila como objeto LSL.")
print("3. Pila como objeto lista.")

seleccion = int(input("Cómo desea usar la pila: "))

if seleccion == 1:
    est_pila_vector()
elif seleccion == 2:
    est_pila_LSL()
else:
    est_pila_lista()
    


"""
Mediante pilas, con la siguiente aplicación podemos comprobar si un grupo de 
paréntesis está bien apareado

print("\n\n\n *****Una aplicación sencilla*****\n")
st = pila()
cadena = "(()(()))"
bandera = False

print(f"Vamos a averiguar si en {cadena} los paréntesis están bien apareados")
for caracter in cadena:
    if caracter=="(":
        st.apilar("(")
    elif caracter==")":
        if not st.esVacia():
            st.desapilar()
        else:
            print("La cadena tiene más paréntesis derechos")
            bandera = True
            break
    else:
        print("La cadena ccontiene caracteres inválidos")

if bandera==False:
    if st.esVacia():
        print("Los paréntesis están bien apareados")
    else:
        print("La cadena tiene más paréntesis izquierdos")
"""

    

