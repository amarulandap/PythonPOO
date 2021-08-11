# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:08:49 2021

@author: USUARIO
"""
#Clase para manipular cada uno de los nodos de una lista
class nodoSimple:
 def __init__(self, d = None):
     self.dato = d
     self.liga = None
     
 def asignarDato(self, d):
     self.dato = d
     
 def asignarLiga(self, x):
     self.liga = x
     
 def retornarDato(self):
     return self.dato
 
 def retornarLiga(self):
     return self.liga