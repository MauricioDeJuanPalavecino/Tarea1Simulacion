from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class erlang:
    def __init__(self, lamb, cant_num_alea, k, semilla_congru):
        self.k = k
        self.cant_num_alea = cant_num_alea
        self.lamb = lamb
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
            value = 1
            for j in range(0, self.k):
                value *= self.congru.generar()
            x = ( -(1 / self.k * self.lamb) * math.log(value, math.e))
            if x >= 0:
                arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios
    
    
    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            residuo = 0
            for i in range(0, self.k):
                residuo += ( ( ((self.lamb*aleatoria)**i) * (math.e**(-self.lamb * aleatoria)) ) / math.factorial(i) )
            res_fda.append( (1 - residuo))
        return res_fda


    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            valorFinal = ( ( self.lamb * ( (self.lamb * aleatoria)**(self.k - 1) ) * (math.e ** (-self.lamb * aleatoria) ) ) / ( math.factorial(self.k - 1) ) )
            res_fdp.append(valorFinal)
        return res_fdp
   
    def graficar(self, y):
        fig, ax = plt.subplots()
        ax.plot(y, linewidth=2.0)
        x = self.get_array()
        #ax.scatter(x, y, vmin=0, vmax=100)
        plt.show()
    def graficar_fda(self):
        y = self.get_array_fda()
        self.graficar(y)
    
    def graficar_fdp(self):
        y = self.get_array_fdp()
        self.graficar(y)


"""
er = erlang(2, 100, 2, 19)
var_alea = er.get_array() #eje horizontal en grafico

fda = er.get_array_fda() #opcion de eje vertical en grafico
fdp = er.get_array_fdp() #opcion de eje vertical en grafico
er.graficar(var_alea, fda)

"""