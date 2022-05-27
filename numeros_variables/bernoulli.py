from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class bernoulli:
    def __init__(self, prob, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea #cantidad de numeros aleatorios
        self.prob = prob #probabilidad
        self.congru = congruencial_mult(semilla_congru) #metodo de generacion de v.a. con semilla
        self.arrayNumAleratorios = self.formular() #numeros aleatorios generados
    
    
    def get_array(self):
        return self.arrayNumAleratorios
    
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar() # se genera el valor pseudo-aleatoreo con el metodo congruencial y la semilla asiganada
            x = 0
            if(value <= self.prob):
                x = 1
            else:
                x= 0
            arrayNumAleratorios.append(x)
        return arrayNumAleratorios
    
    def muestreo(self):
        print("Estas son las variables de la distribucion bernoulli")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1
#be = bernoulli(0.3, 1000, 19)


#fdp = be.get_array_fdp()
#var_alea = be.get_array()

#be.graficar(var_alea, fdp)