from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class weibull:
    def __init__(self, alpha, beta, cant_num_alea, semilla_congru1, semilla_congru2):
        self.alpha = alpha #valor alpha para weibull
        self.beta = beta #valor beta para weibull
        self.cant_num_alea = cant_num_alea #cantidad de numeros aleatorios
        self.congru1 = congruencial_mult(semilla_congru1) #metodo de generacion de v.a. con primera semilla
        self.congru2 = congruencial_mult(semilla_congru2) #metodo de generacion de v.a. con segunda semilla
        self.arrayNumAleratorios = self.formular() #numeros aleatorios generados
       
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios
    
    #CALCULOS CON FUNCIONES
    def formular(self):
        arrayNumAleratorios = []
        z1 = 0
        z2 = 0 
        for i in range(0, self.cant_num_alea):
            value1 = self.congru1.generar() # se genera el valor pseudo-aleatoreo con el metodo congruencial y la priemra semilla asiganada
            value2 = self.congru2.generar() # se genera el valor pseudo-aleatoreo con el metodo congruencial y la segunda semilla asiganada
            z1 = math.sqrt(-2*math.log(value1,math.e))*math.cos(2*math.pi*value2)
            z2 = math.sqrt(-2*math.log(value1,math.e))*math.sin(2*math.pi*value2)
            if(z1 >= 0):
                arrayNumAleratorios.append(z1)
            if(z2 >= 0):
                arrayNumAleratorios.append(z2)
        return arrayNumAleratorios

    def muestreo(self):
       print("Estas son las variables de la distribucion weibull")
       contador = 1
       for i in self.arrayNumAleratorios:
           print("Esta es la variable x"+str(contador)+":  "+str(i))
           contador+=1
"""
ex = weibull(5, 1, 100, 19)
var_alea = ex.get_array() #eje horizontal en grafico

fda = ex.get_array_fda() #opcion de eje vertical en grafico
fdp = ex.get_array_fdp() #opcion de eje vertical en grafico
ex.graficar(var_alea, fda)
"""
