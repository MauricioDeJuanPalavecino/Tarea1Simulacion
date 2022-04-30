from congruencial_mult import *
import matplotlib.pyplot as plt
from scipy.special import gammainc
import math
import statistics
#Nota mauri: esto sera subido al github solo para tener respaldo ante cualquier caso
#falta crear las clases y el resto de funciones pero eso se hara en el debido tiempo
array = []
k = 3
n = 500
cm = congruencial_mult(19)

z1= 0
z2 = 0
for i in range(0, n):
     value1 = cm.generar()
     value2 = cm.generar()
     
     z1= math.sqrt(-2*math.log(value1,math.e))*math.cos(2*math.pi*value2)
     z2= math.sqrt(-2*math.log(value1,math.e))*math.sin(2*math.pi*value2)
     
    

     
     if(z1>=0):
     	array.append(z1)
     if(z2>=0):
     	array.append(z2)
     array.sort()


arrayFDA = []
arrayFDP = []

#Funcion de distribucion acumulada
for i in array:
    arrayFDA.append( gammainc(k/2, i/2) / math.gamma(k/2) )


#Funcion de densidad de probabilidad
for h in array:
	arrayFDP.append((((1/2)**(k/2))/math.gamma(k/2))*((h)**((k/2)-1))*math.exp(-h/2))
#graficoooooooooooooooooooooooooooo
x = array #variables aleratoreas FDA
y = arrayFDA #luego de aplicar funcion de probabilidad a este resultado

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
#ax.scatter(x, y, vmin=0, vmax=100)
#ax.scatter(x, y)

plt.show()
