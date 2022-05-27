from unittest import result
from numpy import var

from congruencial_mult import *
import math
import matplotlib.pyplot as plt


class uniformeContinua:
    def __init__(self, a, b, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea #cantidad de numeros aleatorios
        self.a = a #valor a para uniforme continua
        self.b = b #valor b para uniforme continua
        self.congru = congruencial_mult(semilla_congru) #metodo de generacion de v.a. con semilla
        self.arrayNumAleratorios = self.formular() #numeros aleatorios generados
       
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios


    #CALCULOS CON FUNCIONES
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar() # se genera el valor pseudo-aleatoreo con el metodo congruencial y la semilla asiganada
            x = ( self.a + ( self.b - self.a )*value )
            arrayNumAleratorios.append(x)
        return arrayNumAleratorios
    
    def muestreo(self):
        print("Estas son las variables de la distribucion uniforme continua")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1

"""
uc = uniformeContinua(2, 4, 100, 19)
var_alea = uc.get_array() #eje horizontal en grafico

fda = uc.get_array_fda() #opcion de eje vertical en grafico
fdp = uc.get_array_fdp() #opcion de eje vertical en grafico

uc.graficar(var_alea, fda)
"""