from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class erlang:
    def __init__(self, lamb, cant_num_alea, k, arraySemillas):
        self.k = k
        self.cant_num_alea = cant_num_alea
        self.lamb = lamb
        self.ArraySemillas = arraySemillas
        self.arrayNumAleratorios = self.formular()
        

    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios

    def get_arraySemillas(self):
        return self.ArraySemillas
  

    #CALCULOS CON FUNCIONES
    def formular(self):
        arrayNumAleratorios = []
        for i in range(0, self.cant_num_alea):
            value = 1
            for j in self.ArraySemillas:
                valor = congruencial_mult(self.ArraySemillas[j])
                value *= valor.generar()
            x = ( -(1 / self.k * self.lamb) * math.log(value, math.e))
            if x >= 0:
                arrayNumAleratorios.append(x)
        return arrayNumAleratorios
    
    
    def muestreo(self):
        print("Estas son las variables de la distribucion erlang")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1

"""
er = erlang(2, 100, 2, 19)
var_alea = er.get_array() #eje horizontal en grafico

fda = er.get_array_fda() #opcion de eje vertical en grafico
fdp = er.get_array_fdp() #opcion de eje vertical en grafico
er.graficar(var_alea, fda)

"""