from this import d
from unittest import result
from numpy import var

from pyrsistent import v
from congruencial_mult import *
import math
import matplotlib.pyplot as plt


class uniformeContinua:
    def __init__(self, a, b, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea
        self.a = a
        self.b = b
        self.congru = congruencial_mult(semilla_congru)
        self.arrayNumAleratorios = self.formular()
        self.res_fda = self.funcion_distribucion_acumulada()
        self.res_fdp = self.funcion_densidad_probabilidad()

    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios

    def get_array_fda(self):
        return self.res_fda
    
    def get_array_fdp(self):
        return self.res_fdp

    #CALCULOS CON FUNCIONES
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar()
            x = ( self.a + ( self.b - self.a )*value )
            arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios
    
    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria <= self.a:
                res_fda.append(0)
            elif( (self.a < aleatoria) and (aleatoria <= self.b)):
                res_fda.append( ((aleatoria - self.a ) / (self.b - self.a)) )
            elif aleatoria > self.b:
                res_fda.append(1)
        return res_fda

    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            if( (self.a<= aleatoria) and (aleatoria < self.b) ):
                res_fdp.append( (1/(self.b - self.a)) )
            else:
                res_fdp.append(0)

        return res_fdp

    def graficar(self, x, y):
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)
        #ax.scatter(x, y, vmin=0, vmax=100)

        plt.show()



"""
uc = uniformeContinua(2, 4, 100, 19)
var_alea = uc.get_array() #eje horizontal en grafico

fda = uc.get_array_fda() #opcion de eje vertical en grafico
fdp = uc.get_array_fdp() #opcion de eje vertical en grafico

uc.graficar(var_alea, fda)
"""