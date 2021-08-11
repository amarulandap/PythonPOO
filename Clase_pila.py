# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:48:12 2021

@author: andre
"""
from Arreglos import vector
from Listas_Ligadas import LSL

#Representación de pilas en un vector
class pila_vector(vector):
    def __init__(self, n):
        vector.__init__(self, n)
        
    def apilar(self, d):
        self.agregar_dato(d)
        
    def apilar_1(self, n, r1, r2):
        self.construye_vector(n, r1, r2)
        
    def muestraPila(self):
        self.imprime_vector(mensaje = "Pila: ")
        
    def desapilar(self):
        if self.V[0] == 0:
            print("Pila vacía")
            return None
        d = self.V[self.V[0]]
        self.V[0] = self.V[0] - 1
        return d


#Representación de pilas en una lista simplemnte ligada    
class pila_LSL(LSL):
    def __init__(self):
        LSL.__init__(self)
    
    def apilar(self, d):
        self.insertar(d)
    
    def muestraPila(self):
        self.recorrerLista()
    
    def desapilar(self):
        p = self.primerNodo()
        d = p.retornarDato()
        self.borrar(p)
        return d


#Representación de una pila como una lista
#n es el tamaño de la pila
class pila_lista():
    def __init__(self, n):
        self.n = n
        self.lista = []
        
    def esVacia(self):
        return len(self.lista) == 0
            
    def esLlena(self):
        return len(self.lista) == self.n
    
    def agregar_dato(self, d):
        if self.esLlena():
            print("la Lista esta llena")
            return
        else:
            self.lista.append(d)
            
    def eliminar_dato(self, m):
        self.m = m
        if self.esVacia():
            print("la Lista esta vacia")
            return
        else:
            del self.lista [self.m-1]
            
    def mostrar_tope(self, m):
        self.m = m
        x = self.lista[self.m-1]
        return x
    
    def imprimir_lista(self):
        print(self.lista)


