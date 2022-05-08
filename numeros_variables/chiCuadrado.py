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
		self.res_fda = self.funcion_distribucion_acumulada()
		self.res_fdp = self.funcion_densidad_probabilidad()
    #Getters
	def get_array(self):
		return self.arrayNumAleratorios
	def get_array_fda(self):
		return self.res_fda
	def get_array_fdp(self):
		return self.res_fdp

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
	def funcion_distribucion_acumulada(self):
		res_fda = []
		for aleatoria in self.arrayNumAleratorios:
			res_fda.append(gammainc(self.grados_libertad/2, aleatoria/2) / math.gamma(self.grados_libertad/2) )
		return res_fda
	def funcion_densidad_probabilidad(self):
		res_fdp = []
		for aleatoria in self.arrayNumAleratorios:
			res_fdp.append((((1/2)**(self.grados_libertad/2))/math.gamma(self.grados_libertad/2))*((aleatoria)**((self.grados_libertad/2)-1))*math.exp(-aleatoria/2))
		return res_fdp

	def graficar(self, y):
		x = self.get_array()
		fig, ax = plt.subplots()
		ax.plot(x, y, linewidth=1.0)
		#ax.scatter(x, y, vmin=0, vmax=100)
		plt.show()
	
	def graficar_fda(self):
		y = self.get_array_fda()
		self.graficar(y)
	
	def graficar_fdp(self):
		y = self.get_array_fdp()
		self.graficar(y)

"""
cc = chiCuadrado(1, 1000, 19)

var_alea = cc.get_array()

fda = cc.get_array_fda() #opcion de eje vertical en grafico
fdp = cc.get_array_fdp() #opcion de eje vertical en grafico
cc.graficar(var_alea, fda)
"""