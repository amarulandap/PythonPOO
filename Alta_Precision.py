# -*- coding: utf-8 -*-

#Clase de vectores usada para realizar operaciones aritméticas entre
#números con una gran cantidad de digitos.

from Arreglos import vector

class altaPrecision(vector):
    
    def __init__(self, n):
        vector.__init__(self, n)
        self.V[0] = n
    
    def mueveALaDerecha(self):
        m = self.n
        for i in range(self.V[0], 0, -1):
            self.V[m] = self.V[i]
            m = m - 1
        self.V[0] = self.n - self.V[0]
            
    def imprime_vector(self, mensaje="vector sin nombre: "):
        print("\n", mensaje)
        for i in range(self.V[0] + 1, self.n + 1):
            print(self.V[i], end = ", ")
        
    def sumaYacarreo(self, a, b = 0):
        global acarreo
        s = a + b + acarreo
        if s > 9:
            acarreo = s // 10
            s = s - 10
        else:
            acarreo = 0
        return s

    def __add__(self, b):
        global acarreo
        i = self.tamaño_vector()
        j = b.tamaño_vector()
        k = i if i>j else j
        k = k + 2
        c = altaPrecision(k)
        acarreo = 0
        while i > self.V[0] and j > b.V[0]:
            r = self.sumaYacarreo(self.V[i], b.V[j])
            c.V[k] = r
            i = i - 1
            j = j - 1
            k = k - 1
        while i > self.V[0]:
            r = self.sumaYacarreo(self.V[i])
            c.V[k] = r
            i = i - 1
            k = k - 1
        while j > b.V[0]:
            r = self.sumaYacarreo(b.V[j])
            c.V[k] = r
            j = j - 1
            k = k - 1
        if acarreo > 0:
            c.V[k] = acarreo
            k = k - 1
        c.V[0] = k
        return c

