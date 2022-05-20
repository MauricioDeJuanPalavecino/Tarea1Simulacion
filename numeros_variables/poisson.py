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
      
    def get_array(self):
        return self.arrayNumAleratorios
    


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
    
    def muestreo(self):
       print("Estas son las variables de la distribucion poisson")
       contador = 1
       for i in self.arrayNumAleratorios:
           print("Esta es la variable x"+str(contador)+":  "+str(i))
           contador+=1

"""

#permite maximo 171 numeros
po = poisson(8, 20, 19)
var_alea = po.get_array() #eje horizontal en grafico


fda = po.get_array_fda() #opcion de eje vertical en grafico
fdp = po.get_array_fdp() #opcion de eje vertical en grafico
po.graficar(var_alea, fda)
"""


