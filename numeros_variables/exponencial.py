from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt


class exponencial:
    def __init__(self, lamb, cant_num_alea, congruencial_mult):
        self.cant_num_alea = cant_num_alea
        self.lamb = lamb
        self.congru = congruencial_mult
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
            x = -( (1 / self.lamb) * math.log(value, math.e))
            arrayNumAleratorios.append(x)
            arrayNumAleratorios.sort()
        return arrayNumAleratorios
    
    def funcion_distribucion_acumulada(self):
        res_fda = []
        
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria >= 0:
                res_fda.append( 1 - math.exp(-self.lamb*aleatoria))
        return res_fda

    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            if aleatoria >= 0:
                res_fdp.append( self.lamb *  math.exp(-self.lamb*aleatoria))
        return res_fdp
        


cm = congruencial_mult(19)

ex = exponencial(2, 1000, cm)
var_alea = ex.get_array() #eje horizontal en grafico


fda = ex.get_array_fda() #opcion de eje vertical en grafico
fdp = ex.get_array_fdp() #opcion de eje vertical en grafico





#---------------- GRAFICA -------------------
x = var_alea #variables aleratoreas FDA
y = fda #luego de aplicar funcion de probabilidad a este resultado

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
#ax.scatter(x, y, vmin=0, vmax=100)


plt.show()
