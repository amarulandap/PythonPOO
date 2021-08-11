# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:55:37 2021

@author: andre
"""
from Arreglos import vector
from Listas_Ligadas import LSL

class cola_vector(vector):
    def __init__(self, n):
        vector.__init__(self, n)
        self.primero = 0
        self.ultimo = 0
        
    def esLlena (self):
        return self.primero == self.ultimo
    
    def esVacia (self):
        return self.primero == self.ultimo
    
    def encolar (self, d):
        self.ultimo = (self.ultimo + 1) % self.n
        if self.esLlena():
            print("cola llena, no se puede encolar\n")
            self.ultimo = (self.ultimo - 1 + self.n) % self.n
            return
        self.V[self.ultimo] = d #cambio
        
    def desencolar (self):
        if self.esVacia():
            print("cola vacía, no se puede desencolar\n")
            return None
        self.primero = (self.primero + 1) % self.n
        return self.V[self.primero] #cambio
    
    def siguiente (self):
        if self.esVacia():
            print("cola vacía, no hay siguiente\n")
            return None
        aux = (self.primero + 1) % self.n
        return self.V[aux]
    
    def muestra_cola(self):
        if self.primero < self.ultimo:
            limite = self.ultimo + 1
        else:
            limite=self.n
        #limite = self.ultimo + 1 if self.primero < self.ultimo else self.n
        for i in range(self.primero+1, limite):
            print(self.V[i], end=", ")
        if self.primero > self.ultimo:
            for i in range(1, self.ultimo + 1):
                print(self.V[i], end=", ")
        print()

class cola_LSL(LSL):
    def __init__(self):
        LSL.__init__(self)
    
    def encolar (self, d):
        self.agregarDato(d)
    
    def desencolar (self):
        if self.esVacia():
            print("\nCola vacía no hay datos para desencolar")
            return None
        d = self.primero.retornarDato()
        p = self.primerNodo()
        self.borrar(p)
        return d
    
    def siguiente (self):
        if self.esVacia():
            print("\nCola vacía no hay siguiente")
            return None
        d = self.primero.retornarDato()
        return d

class cola_lista():
    def __init__(self, n):
        self.n = n
        self.lista = []
        
    def esVacia(self):
        return len(self.lista) == 0
    
    def esLlena(self):
        return len(self.lista) == self.n
    
    def agregar_dato(self, d):
        if self.esLlena():
            print("la Lista está llena")
            return
        else:
            self.lista.insert(0, d)
            
    def eliminar_dato(self):
        if self.esVacia():
            print("La Lista está vacia")
            return
        else:
            del self.lista[self.n]
            
    def mostrar_tope(self):
        x = self.lista[0]
        return x
    
    def imprimir_lista(self):
        print(self.lista)

"""
qu = cola(23)

for i in range(1,18):
    qu.encolar(i)

qu.encolar("a")
qu.encolar("b")
qu.encolar(316)
qu.muestra_cola()
d = qu.desencolar()
d = qu.desencolar()
d = qu.desencolar()
d = qu.desencolar()
d = qu.desencolar()
d = qu.desencolar()
d = qu.desencolar()
print("\nDato desencolado:", d)

qu.encolar("x1")
qu.encolar("x2")
qu.encolar("x3")
qu.encolar("x4")
qu.encolar("x5")
qu.encolar("x6")
d = qu.desencolar()
qu.encolar("x7")
qu.muestra_cola()

-----

a = cola()
b = a.esVacia()
print(b)
a.encolar("a")
a.encolar("e")
a.encolar("i")
a.encolar("o")
a.recorrerLista()
b = a.esVacia()
print("\n", b)
d = a.desencolar()
print("\ndato desencolado es: ", d)
a.recorrerLista()
d = a.siguiente()
print("\nel siguiente es:", d)
a.recorrerLista()
"""
