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
        self.res_fda = self.funcion_distribucion_acumulada()
        self.res_fdp = self.funcion_densidad_probabilidad()
    
    def get_array(self):
        return self.arrayNumAleratorios
    
    def get_array_fda(self):
        return self.res_fda
    
    def get_array_fdp(self):
        return self.res_fdp

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
    
    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            valor = (self.prob**aleatoria)*((1-self.prob)**(1-aleatoria))
            res_fdp.append(valor)
        return res_fdp
    
    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            valor = 0
            if(aleatoria ==0):
                valor = 1 - self.prob
            else:
                valor = 1
            res_fda.append(valor)
        return res_fda

    def graficar(self, x, y):
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)
        ax.scatter(x, y, vmin=0, vmax=100)

        plt.show()

be = bernoulli(0.3, 1000, 19)


fdp = be.get_array_fdp()
var_alea = be.get_array()

be.graficar(var_alea, fdp)