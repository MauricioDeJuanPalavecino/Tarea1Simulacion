from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class weibull:
    def __init__(self, alpha, beta, cant_num_alea, semilla_congru):
        self.alpha = alpha
        self.beta = beta
        self.cant_num_alea = cant_num_alea
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
        z1 = 0
        z2 = 0 
        for i in range(0, self.cant_num_alea):
            value1 = self.congru.generar()
            value2 = self.congru.generar()
            z1 = math.sqrt(-2*math.log(value1,math.e))*math.cos(2*math.pi*value2)
            z2 = math.sqrt(-2*math.log(value1,math.e))*math.sin(2*math.pi*value2)
            if(z1 >= 0):
                arrayNumAleratorios.append(z1)
            if(z2 >= 0):
                arrayNumAleratorios.append(z2)

        arrayNumAleratorios.sort()
        return arrayNumAleratorios

    def funcion_distribucion_acumulada(self):
        res_fda = []
        
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria > 0:
                res_fda.append( 1 - math.exp(-(self.beta*aleatoria)**self.alpha))
        return res_fda

    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria > 0:
                res_fdp.append(self.beta*self.alpha*((self.beta*aleatoria)**(self.alpha-1))*math.exp(-((self.beta*aleatoria)**self.alpha)))
                #res_fdp.append( (self.alpha/(self.beta**self.alpha)) * (aleatoria**(self.alpha-1)) * math.exp(-(aleatoria/self.beta)**self.alpha))
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
ex = weibull(5, 1, 100, 19)
var_alea = ex.get_array() #eje horizontal en grafico

fda = ex.get_array_fda() #opcion de eje vertical en grafico
fdp = ex.get_array_fdp() #opcion de eje vertical en grafico
ex.graficar(var_alea, fda)
"""
