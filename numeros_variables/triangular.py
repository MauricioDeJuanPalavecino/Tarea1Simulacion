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
            if(value <= ((self.c-self.a)/(self.b-self.a))):
                x =self.a + math.sqrt(value * ((self.b - self.a)*(self.c - self.a)))
                arrayNumAleratorios.append(x)
            else:    
                x = self.b - ( math.sqrt((1-value)*(self.b - self.a)*(self.b - self.c)))
                arrayNumAleratorios.append(x)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios

    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            if (aleatoria <= self.a):
                fdavalue = 0
                res_fda.append(fdavalue)
            elif(self.a < aleatoria and aleatoria <= self.c):
                fdavalue = (math.pow((aleatoria - self.a), 2)/((self.b - self.a)*(self.c - self.a)))
                res_fda.append(fdavalue)
            elif(self.c < aleatoria and aleatoria < self.b):
                fdavalue = (1 - math.pow((self.b - aleatoria),2)/((self.b - self.a)*(self.b - self.c)))
                res_fda.append(fdavalue)
            else:
                fdavalue = 1
                res_fda.append(fdavalue)    

        return res_fda
    
    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            if (self.a <= aleatoria and aleatoria <= self.c):
                fdpvalue = (2*(aleatoria - self.a)/((self.b - self.a)*(self.c-self.a)))
                res_fdp.append(fdpvalue)
            elif (aleatoria == self.c):
                fdpvalue = (2/(self.b - self.a))
                res_fdp.append(fdpvalue)
            elif (self.c < aleatoria and aleatoria <= self.b):
                fdpvalue = (2*(self.b - aleatoria)/((self.b - self.a)*(self.b - self.c))) 
                res_fdp.append(fdpvalue)
            else:
                fdpvalue = 0
                res_fdp.append(fdpvalue)           
        return res_fdp

    def graficar(self, y):
        x = self.get_array()
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        #ax.scatter(x, y, vmin=0, vmax=100)
        plt.show()

    def graficar_fda(self):
        y = self.get_array_fda()
        self.graficar(y)
    
    def graficar_fdp(self):
        y = self.get_array_fdp()
        self.graficar(y)

#trlar = triangular(2, 10, 5,100, 19)
#var_alea = trlar.get_array() #eje horizontal en grafico

#fda = trlar.get_array_fda() #opcion de eje vertical en grafico
#fdp = trlar.get_array_fdp() #opcion de eje vertical en grafico
#trlar.graficar(var_alea, fdp)