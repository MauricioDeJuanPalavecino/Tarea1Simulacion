from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class bernoulli:
    def __init__(self, prob, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea
        self.prob = prob
        self.congru = congruencial_mult(semilla_congru)
        self.arrayNumAleratorios = self.formular()
       
    def get_array(self):
        return self.arrayNumAleratorios
    
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar()
            x = 0
            if(value <= self.prob):
                x = 1
            else:
                x= 0
            arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
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