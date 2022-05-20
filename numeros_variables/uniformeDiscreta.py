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
      
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios
    
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar()
            x = int(self.cant_num_alea*value) + 1
            if(x >= self.a and x<= self.b):
                arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios
    
    def muestreo(self):
        print("Estas son las variables de la distribucion uniforme discreta")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1

#z = congruencial_mult(19)

#ud = uniformeDiscreta(1, 5, 10000, 19)


#fdp = ud.get_array_fdp()
#var_alea = ud.get_array()

#ud.graficar(var_alea, fdp)