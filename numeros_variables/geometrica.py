from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math

class geometrica:
    def __init__(self, prob, cant_num_alea, congruencial_mult):
        self.cant_num_alea = cant_num_alea
        self.prob = prob
        self.congru = congruencial_mult
        self.arrayNumAleratorios = self.formular()
        self.res_fda = self.funcion_distribucion_acumulada()
        self.res_fdp = self.funcion_densidad_probabilidad()
    
    def get_array(self):
        return self.arrayNumAleratorios
    
    def get_array_fda(self):
        return self.res_fda
    
    def get_array_fdp(self):
        return self.res_fdp

    #Generar variables aleatorias
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0,self.cant_num_alea):
            value = cm.generar()
            var_alea = int(math.log(value,math.e)/math.log(1-self.prob,math.e))
            arrayNumAleratorios.append(var_alea)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios
    
    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            valor = 1 - (1 - self.prob)**(aleatoria+1)
            res_fda.append(valor)
        return res_fda
    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            valor = self.prob*((1-self.prob)**aleatoria)
            res_fdp.append(valor)
        return res_fdp
cm = congruencial_mult(19)

g = geometrica(0.32, 1000, cm)

var_alea = g.get_array()

#Grafica

fda = g.get_array_fda() #opcion de eje vertical en grafico
fdp = g.get_array_fdp() #opcion de eje vertical en grafico

x = var_alea #variables aleratoreas FDA
y = fdp #luego de aplicar funcion de probabilidad a este resultado

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
#ax.scatter(x, y, vmin=0, vmax=100)
#ax.scatter(x, y)

plt.show()