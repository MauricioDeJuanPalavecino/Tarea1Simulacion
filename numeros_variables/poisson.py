from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math

class poisson:
    def __init__(self, lamb, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea
        self.lamb = lamb
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
        variables = 0
        valorU = 1
        for i in range(0,self.cant_num_alea):
            value = self.congru.generar()
            valorU*=value
            if(valorU<=math.exp(-self.lamb)):
                arrayNumAleratorios.append(variables)
            else: break
            variables+=1
        return arrayNumAleratorios
    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            valor = (math.exp(-self.lamb)*(self.lamb**aleatoria))/math.factorial(aleatoria)
            res_fdp.append(valor)
        return res_fdp

    def funcion_distribucion_acumulada(self):
        res_fda =[]
        valoresSum = 0
        for aleatoria in self.arrayNumAleratorios:
            for i in range(0, math.floor(aleatoria)):
                valoresSum = valoresSum + (self.lamb**i/math.factorial(i))
            valorFinal = math.exp(-self.lamb)*valoresSum
            res_fda.append(valorFinal)
            valoresSum = 0
        return res_fda

    def graficar(self, y):
        x = self.get_array()
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        ax.scatter(x, y, vmin=0, vmax=100)
        #ax.scatter(x, y)

        plt.show()

    def graficar_fda(self):
        y = self.get_array_fda()
        self.graficar(y)
    
    def graficar_fdp(self):
        y = self.get_array_fdp()
        self.graficar(y)
"""

#permite maximo 171 numeros
po = poisson(8, 20, 19)
var_alea = po.get_array() #eje horizontal en grafico


fda = po.get_array_fda() #opcion de eje vertical en grafico
fdp = po.get_array_fdp() #opcion de eje vertical en grafico
po.graficar(var_alea, fda)
"""


