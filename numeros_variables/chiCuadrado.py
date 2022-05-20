from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math

class chiCuadrado:
	def __init__(self, grados_libertad, cant_num_alea, semilla_congru):
		self.cant_num_alea = cant_num_alea
		self.grados_libertad = grados_libertad
		self.congru = congruencial_mult(semilla_congru)
		self.arrayNumAleratorios = self.formular()
		
    #Getters
	def get_array(self):
		return self.arrayNumAleratorios

    #Generar variables aleatorias
	def formular(self):
		arrayNumAleratorios = []
		z1 = 0
		z2 = 0
		for i in range(0, int(self.cant_num_alea/2)):
    		#Generar numeros aleatorios
			value1 = self.congru.generar()
			value2 = self.congru.generar()
			
			z1 = math.sqrt(-2*math.log(value1,math.e))*math.cos(2*math.pi*value2)
			z2 = math.sqrt(-2*math.log(value1,math.e))*math.sin(2*math.pi*value2)
     		#Estos if funcionan para evitar problemas con los numeros negativos para chicuadrado en grafica
			if(z1 >= 0):
				arrayNumAleratorios.append(z1)
			if(z2 >= 0):
				arrayNumAleratorios.append(z2)
		arrayNumAleratorios.sort()
		return arrayNumAleratorios
	
	def muestreo(self):
		print("Estas son las variables de la distribucion chi cuadrado")
		contador = 1
		for i in self.arrayNumAleratorios:
			print("Esta es la variable x"+str(contador)+":  "+str(i))
			contador+=1

"""
cc = chiCuadrado(1, 1000, 19)

var_alea = cc.get_array()

fda = cc.get_array_fda() #opcion de eje vertical en grafico
fdp = cc.get_array_fdp() #opcion de eje vertical en grafico
cc.graficar(var_alea, fda)
"""