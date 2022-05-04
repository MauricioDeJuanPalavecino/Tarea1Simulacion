from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class uniformeDiscreta:
    def __init__(self, a, b, cant_num_alea, semilla_congru):
        self.a = a
        self.b = b
        self.cant_num_alea = cant_num_alea
        self.congru = congruencial_mult(semilla_congru)
        self.arrayNumAleratorios = self.formular()
        self.res_fdp = self.funcion_probabilidad()
      
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios
    
    def get_array_fdp(self):
        return self.res_fdp

    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar()
            x = int(self.cant_num_alea*value) + 1
            if(x >= self.a and x<= self.b):
                arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios
    
    def funcion_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios: 
            valor = 1/ len(self.arrayNumAleratorios)
            res_fdp.append(valor)
        return res_fdp
    
    def graficar(self, x, y):
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)
        ax.scatter(x, y, vmin=0, vmax=100)

        plt.show()
#z = congruencial_mult(19)

ud = uniformeDiscreta(1, 5, 10000, 19)


fdp = ud.get_array_fdp()
var_alea = ud.get_array()

ud.graficar(var_alea, fdp)