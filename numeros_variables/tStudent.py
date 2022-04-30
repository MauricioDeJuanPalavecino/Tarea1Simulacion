from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math

class tstudent:
    def __init__(self, grados_libertad, cant_num_alea, congruencial_mult):
        self.cant_num_alea = cant_num_alea
        self.grados_libertad = grados_libertad
        self.congru = congruencial_mult
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

    #Generar variables aleatorias
    def formular(self):
        arrayNumAleratorios = []
        valoresChi = 1
        for i in range(0, self.cant_num_alea):
            value1 = self.congru.generar()
            value2 = self.congru.generar()
            z1= math.sqrt(-2*math.log(value1,math.e))*math.cos(2*math.pi*value2)
            z2= math.sqrt(-2*math.log(value1,math.e))*math.sin(2*math.pi*value2)
            if(self.grados_libertad==1):
                for h in range(0, self.grados_libertad):
                    valorChi = self.congru.generar()
                    valoresChi = valoresChi*valorChi
            else: 
                for h in range(0, round(self.grados_libertad/2)):
                    valorChi = self.congru.generar()
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

    def funcion_distribucion_acumulada(self):
        res_fda = []
        for aleatoria in self.arrayNumAleratorios:
            if(self.grados_libertad==1):
                res_fda.append(1/2 + (1/math.pi)*math.atan(aleatoria))
            elif(self.grados_libertad==2):
                res_fda.append(1/2 + (aleatoria/(2*math.sqrt(2)*math.sqrt(1+(aleatoria**2)/2))))
            elif(self.grados_libertad==3):
                valorcorchetes = (aleatoria/(math.sqrt(3)*(1+(aleatoria**2)/3))+ math.atan(aleatoria/math.sqrt(3)))
                res_fda.append(1/2 + (1/math.pi)*valorcorchetes)
            else:
                res_fda.append((1/2)*(1+math.erf(aleatoria/math.sqrt(2))))
        return res_fda
    def funcion_densidad_probabilidad(self):
        res_fdp = []
        for aleatoria in self.arrayNumAleratorios:
            if(self.grados_libertad==1):
                res_fdp.append(1/(math.pi*(1+aleatoria**2)))
            elif(self.grados_libertad==2):
                valorparentesis = 1+ (aleatoria**2)/2
                res_fdp.append(1/(2*math.sqrt(2)*(valorparentesis**3/2)))
            elif(self.grados_libertad==3):
                valorparentesis = (1+ (aleatoria**2)/3)**2
                res_fdp.append(2/(math.pi*math.sqrt(3)*valorparentesis))
            else:
                res_fdp.append((1/math.sqrt(2*math.pi))*math.exp(-aleatoria**2/2))
        return res_fdp

cm = congruencial_mult(19)

ts = tstudent(3, 10000, cm)

var_alea = ts.get_array()

fda = ts.get_array_fda() #opcion de eje vertical en grafico
fdp = ts.get_array_fdp() #opcion de eje vertical en grafico

x = var_alea #variables aleratoreas FDA
y = fdp #luego de aplicar funcion de probabilidad a este resultado

fig, ax = plt.subplots()

#ax.plot(x, y, linewidth=2.0)
ax.scatter(x, y, vmin=0, vmax=100)
#ax.scatter(x, y)

plt.show()
