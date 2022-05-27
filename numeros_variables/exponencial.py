from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt


class exponencial:
    def __init__(self, lamb, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea #cantidad de numeros aleatorios que seran generados
        self.lamb = lamb #lambda
        self.congru = congruencial_mult(semilla_congru) #metodo de generacion de v.a. con semilla
        self.arrayNumAleratorios = self.formular() #numeros aleatorios generados
        
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios
    
    #CALCULOS CON FUNCIONES
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar()  # se genera el valor pseudo-aleatoreo con el metodo congruencial y la semilla asiganada
            x = -( (1 / self.lamb) * math.log(value, math.e))
            arrayNumAleratorios.append(x)
        return arrayNumAleratorios
    
    def muestreo(self):
        print("Estas son las variables de la distribucion exponencial")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1

"""
ex = exponencial(2, 1000, 19)
var_alea = ex.get_array() #eje horizontal en grafico


fda = ex.get_array_fda() #opcion de eje vertical en grafico
fdp = ex.get_array_fdp() #opcion de eje vertical en grafico
ex.graficar(var_alea, fda)
"""
