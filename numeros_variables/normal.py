from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class normal:
    def __init__(self, media, desv_tipica, cant_num_alea, congruencial_mult):
        self.media = media
        self.desv_tipica = desv_tipica
        self.cant_num_alea = cant_num_alea
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
        z1 = 0
        z2 = 0
        for i in range(0, int(self.cant_num_alea/2)):
            value1 = self.congru.generar()
            value2 = self.congru.generar()
            z1 = math.sqrt(-2 * math.log(value1,math.e)) * math.cos(2 * math.pi * value2)
            z2 = math.sqrt(-2 * math.log(value1,math.e)) * math.sin(2 * math.pi * value2)
            arrayNumAleratorios.append(z1)
            arrayNumAleratorios.append(z2)
        arrayNumAleratorios.sort()

        return arrayNumAleratorios
    
    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            res_fda.append( (1/2) * (1 + math.erf( (aleatoria - self.media) / (self.desv_tipica*math.sqrt(2)))))
        return res_fda

    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            res_fdp.append( (1 / (self.desv_tipica*math.sqrt(2*math.pi))) * math.exp(-(1/2) * ((aleatoria-self.media)/self.desv_tipica)**2) )
        return res_fdp
cm = congruencial_mult(19)

ex = normal(0, 1, 600, cm)
var_alea = ex.get_array() #eje horizontal en grafico


fda = ex.get_array_fda() #opcion de eje vertical en grafico
fdp = ex.get_array_fdp() #opcion de eje vertical en grafico





#---------------- GRAFICA -------------------
x = var_alea #variables aleratoreas FDA
y = fda #luego de aplicar funcion de probabilidad a este resultado

print(x)
print(y)

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
#ax.scatter(x, y, vmin=0, vmax=100)


plt.show()