from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt


class pareto:
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
            x = ( self.b / (math.pow(1 - value, (1 / self.a)) ) )
            arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios

    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria >= self.b:
                res_fda.append( (1 - math.pow( (self.b / aleatoria), self.a )) )  
        return res_fda
    
    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria >= self.b:
                res_fdp.append( (  (self.a * math.pow(self.b, self.a)) / (math.pow(aleatoria, (self.a + 1))) ) )
        return res_fdp

    def graficar(self, y):
        x = self.get_array() 
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        #ax.scatter(x, y, vmin=0, vmax=100)
        plt.show()

    def graficar_fda(self):
        y = self.get_array_fda()
        self.graficar(y)
    
    def graficar_fdp(self):
        y = self.get_array_fdp()
        self.graficar(y)

"""
pa = pareto(2, 10, 100, 19)
var_alea = pa.get_array() #eje horizontal en grafico

fda = pa.get_array_fda() #opcion de eje vertical en grafico
fdp = pa.get_array_fdp() #opcion de eje vertical en grafico
pa.graficar(var_alea, fda)
"""