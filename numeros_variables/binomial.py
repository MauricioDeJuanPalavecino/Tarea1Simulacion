from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
from scipy.special import betainc
import math

class binomial:
    def __init__(self, prob, cant_num_alea, congruencial_mult):
        self.cant_num_alea = cant_num_alea
        self.prob = prob
        self.congru = congruencial_mult
        self.arrayNumAleratorios = self.formular()
        self.res_fda = self.funcion_distribucion_acumulada()
        self.res_fdp = self.funcion_masa_probabilidad()

    def get_array(self):
        return self.arrayNumAleratorios
    
    def get_array_fda(self):
        return self.res_fda
    
    def get_array_fdp(self):
        return self.res_fdp

    def formular(self):
        arrayNumAleratorios = []
        for i in range(0,self.cant_num_alea):
            value = self.congru.generar()
            valor = int((self.prob*self.cant_num_alea-value+value*self.prob)/(value-value*self.prob+self.prob))
            arrayNumAleratorios.append(valor)
        arrayNumAleratorios.sort()
        return arrayNumAleratorios
    def funcion_masa_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            valor_nk = math.factorial(self.cant_num_alea)/(math.factorial(aleatoria)*math.factorial(self.cant_num_alea - aleatoria))
            valor = valor_nk*(self.prob**aleatoria)*((1-self.prob)**(self.cant_num_alea-aleatoria))
            res_fdp.append(valor)
        return res_fdp

    def funcion_distribucion_acumulada(self):
        res_fda =[]
        for aleatoria in self.arrayNumAleratorios:
            res_fda.append(betainc(self.cant_num_alea - aleatoria, aleatoria +1, 1 - self.prob))
        return res_fda
cm = congruencial_mult(20)


#permite maximo 171 numeros
bi = binomial(0.5, 40, cm)
var_alea = bi.get_array() #eje horizontal en grafico
print(var_alea)

fda = bi.get_array_fda() #opcion de eje vertical en grafico
fdp = bi.get_array_fdp() #opcion de eje vertical en grafico






x = var_alea #variables aleratoreas FDA
y = fda #luego de aplicar funcion de probabilidad a este resultado

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
ax.scatter(x, y, vmin=0, vmax=100)
#ax.scatter(x, y)

plt.show()
#print(array)
