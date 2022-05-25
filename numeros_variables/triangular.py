from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt


class triangular:
    def __init__(self, a, b, c,cant_num_alea, semilla_congru):
        self.cant_num_alea = cant_num_alea
        self.a = a
        self.b = b
        self.c = c
        self.congru = congruencial_mult(semilla_congru)
        self.arrayNumAleratorios = self.formular()
       
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios

  

    #CALCULOS CON FUNCIONES
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = self.congru.generar()
            if(value <= ((self.c-self.a)/(self.b-self.a))):
                x =self.a + math.sqrt(value * ((self.b - self.a)*(self.c - self.a)))
                arrayNumAleratorios.append(x)
            else:    
                x = self.b - ( math.sqrt((1-value)*(self.b - self.a)*(self.b - self.c)))
                arrayNumAleratorios.append(x)
        return arrayNumAleratorios

    
    def muestreo(self):
       print("Estas son las variables de la distribucion triangular")
       contador = 1
       for i in self.arrayNumAleratorios:
           print("Esta es la variable x"+str(contador)+":  "+str(i))
           contador+=1

#trlar = triangular(2, 10, 5,100, 19)
#var_alea = trlar.get_array() #eje horizontal en grafico

#fda = trlar.get_array_fda() #opcion de eje vertical en grafico
#fdp = trlar.get_array_fdp() #opcion de eje vertical en grafico
#trlar.graficar(var_alea, fdp)