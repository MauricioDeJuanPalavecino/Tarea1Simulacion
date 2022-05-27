from unittest import result
from congruencial_mult import *
import math
import matplotlib.pyplot as plt

class erlang:
    def __init__(self, lamb, cant_num_alea, k, arraySemillas):
        self.k = k #valor k de la distribucion erlang debe ser mayor a 0 y entero (es validado por interfaz grafica)
        self.cant_num_alea = cant_num_alea #cantidad de numeros aleatorios
        self.lamb = lamb #valor de lambda
        self.ArraySemillas = arraySemillas #array de semillas asignado
        self.arrayNumAleratorios = self.formular() #numeros aleatorios generados
        

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
                valor = congruencial_mult(j) #generacion del metodo congruencial con cada una de las semillas asignadas en la entrada
                value *= valor.generar() # generacion del valor del met. congruencial con la semilla asignada
                self.ArraySemillas[self.ArraySemillas.index(j)] = valor.seed #asignacion de la nueva semilla por el valor generado, por ejemplo si el arraySemilla era [1,2,3,4], para la siguiente iteracion sera [77,22,45,76]
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