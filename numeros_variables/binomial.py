from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
from scipy.special import betainc
import math

class binomial:
    def __init__(self, prob, cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea
        self.prob = prob
        self.congru = congruencial_mult(semilla_congru)
        self.arrayNumAleratorios = self.formular()

    def get_array(self):
        return self.arrayNumAleratorios
    
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0,self.cant_num_alea):
            value = self.congru.generar()
            valor = int((self.prob*self.cant_num_alea-value+value*self.prob)/(value-value*self.prob+self.prob))
            arrayNumAleratorios.append(valor)
        return arrayNumAleratorios
  
    def muestreo(self):
        print("Estas son las variables de la distribucion binomial")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1


#bi = binomial(0.5, 40, 20).graficar_fda()
#bi = binomial(0.5, 40, 20).graficar_fdp()
#var_alea = bi.get_array() #eje horizontal en grafico

#fda = bi.get_array_fda() #opcion de eje vertical en grafico
#fdp = bi.get_array_fdp() #opcion de eje vertical en grafico

#bi.graficar(fdp)
