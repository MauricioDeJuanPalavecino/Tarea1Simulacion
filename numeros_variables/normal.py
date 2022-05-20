from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class normal:
    def __init__(self, media, varianza, cant_num_alea, semilla_congru):
        self.media = media
        self.desv_tipica = math.sqrt(varianza)
        self.cant_num_alea = cant_num_alea
        self.congru = congruencial_mult(semilla_congru)
        self.arrayNumAleratorios = self.formular()
        

    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios
    
    #Simulacion
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
    
    def muestreo(self):
       print("Estas son las variables de la distribucion normal")
       contador = 1
       for i in self.arrayNumAleratorios:
           print("Esta es la variable x"+str(contador)+":  "+str(i))
           contador+=1

"""   
ex = normal(0, 1, 600, 19)
var_alea = ex.get_array() #eje horizontal en grafico
ex.muestreo()    
fda = ex.get_array_fda() #opcion de eje vertical en grafico
fdp = ex.get_array_fdp() #opcion de eje vertical en grafico
ex.graficar(var_alea, fda)
"""


