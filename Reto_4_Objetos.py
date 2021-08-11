# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 06:57:16 2021

@author: Andres Marulanda
"""

"""RETO 4 - OBJETOS"""

class Editor_Texto:
    def __init__(self):
        self.texto_escrito = []
        self.rehacer = []
        self.texto_actual =""
    
    def Deshacer(self):
        if len(self.texto_escrito)> 0:
            self.rehacer.append(self.texto_actual)
            self.texto_actual = self.texto_escrito.pop()
            
    def Rehacer(self):
        if len(self.rehacer) > 0:
            self.texto_escrito.append(self.texto_actual)
            self.texto_actual = self.rehacer.pop()
            
    def Agregar(self, i):
        if len(self.texto_actual) > 0:
            self.texto_escrito.append(self.texto_actual)
            self.texto_actual = i
            self.rehacer = []
        else:
            self.texto_actual = i
            self.rehacer = []
            
def actualizar_estado_editor(operaciones_usuario):
    
    comando = Editor_Texto()
    
    for i in comando:
        
        if i == 'DESHACER':
            comando.Deshacer()
            
        elif i == 'REHACER':
            comando.Rehacer()
            
        else:
            comando.Agregar(i)
            
    cadena_final = ""
    
    for i in comando.texto_escrito:
        cadena_final += i
        
        cadena_final += comando.texto_actual
        
    return cadena_final

operaciones_usuario = ['']
print(actualizar_estado_editor(operaciones_usuario))
    