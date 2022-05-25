from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math

class tstudent:
    def __init__(self, grados_libertad, cant_num_alea, semilla_congru1, semilla_congru2, semilla_congru3):
        self.cant_num_alea = cant_num_alea
        self.grados_libertad = grados_libertad
        self.congru1 = congruencial_mult(semilla_congru1)
        self.congru2 = congruencial_mult(semilla_congru2)
        self.congru3 = congruencial_mult(semilla_congru3)
        self.arrayNumAleratorios = self.formular()
       
    #GETTERS
    def get_array(self):
        return self.arrayNumAleratorios

    #Generar variables aleatorias
    def formular(self):
        arrayNumAleratorios = []
        valoresChi = 1
        for i in range(0, int(self.cant_num_alea/2)):
            value1 = self.congru1.generar()
            value2 = self.congru2.generar()
            z1= math.sqrt(-2*math.log(value1,math.e))*math.cos(2*math.pi*value2)
            z2= math.sqrt(-2*math.log(value1,math.e))*math.sin(2*math.pi*value2)
            if(self.grados_libertad==1):
                for h in range(0, self.grados_libertad):
                    valorChi = self.congru3.generar()
                    valoresChi = valoresChi*valorChi
            else: 
                for h in range(0, round(self.grados_libertad/2)):
                    valorChi = self.congru3.generar()
                    valoresChi = valoresChi*valorChi
            if(self.grados_libertad%2==0):
                aleatorioChi = -2*math.log(valoresChi,math.e)
            else:
                aleatorioChi = -2*math.log(valoresChi,math.e) + z1**2
    
   
            aleatorioStudent1 = (z1)/math.sqrt(aleatorioChi/self.grados_libertad)
            aleatorioStudent2 = (z2)/math.sqrt(aleatorioChi/self.grados_libertad)
            if(aleatorioStudent1>=-5 and aleatorioStudent1<=5):
                arrayNumAleratorios.append(aleatorioStudent1)
            if(aleatorioStudent2>=-5 and aleatorioStudent2<=5):
                arrayNumAleratorios.append(aleatorioStudent2)
            valoresChi = 1
        return arrayNumAleratorios

    def muestreo(self):
        print("Estas son las variables de la distribucion T de Student")
        contador = 1
        for i in self.arrayNumAleratorios:
            print("Esta es la variable x"+str(contador)+":  "+str(i))
            contador+=1

"""
ts = tstudent(3, 10000, 19)

var_alea = ts.get_array()

fda = ts.get_array_fda() #opcion de eje vertical en grafico
fdp = ts.get_array_fdp() #opcion de eje vertical en grafico

ts.graficar(var_alea, fda)
"""