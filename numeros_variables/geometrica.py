from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math

class geometrica:
    def __init__(self, prob, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea #cantidad de numeros aleatorios
        self.prob = prob #probabilidad
        self.congru = congruencial_mult(semilla_congru) #metodo de generacion de v.a. con semilla
        self.arrayNumAleratorios = self.formular() #numeros aleatorios generados
    
    def get_array(self):
        return self.arrayNumAleratorios
    
   
    #Generar variables aleatorias
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0,self.cant_num_alea):
            value = self.congru.generar() # se genera el valor pseudo-aleatoreo con el metodo congruencial y la semilla asiganada
            var_alea = int(math.log(value,math.e)/math.log(1-self.prob,math.e))
            arrayNumAleratorios.append(var_alea)
        return arrayNumAleratorios
    
    def muestreo(self):
        print("Estas son las variables de la distribucion geometrica")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1
"""
g = geometrica(0.32, 1000, 19)

var_alea = g.get_array()

fda = g.get_array_fda() #opcion de eje vertical en grafico
fdp = g.get_array_fdp() #opcion de eje vertical en grafico
g.graficar(var_alea, fda)
"""