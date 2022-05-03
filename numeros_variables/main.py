import tkinter as tk
from tkinter import ttk
from binomial import *

root = tk.Tk()
root.geometry("350x100")
root.title('Simulación')
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Semilla
semilla_label = ttk.Label(root, text="Semilla:")
semilla_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

semilla_entry = ttk.Entry(root)
semilla_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

# Distribución
dist_label = ttk.Label(root, text="Distribución:")
dist_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

dist = ('Exponencial', 'Erlang', 'Normal(0,1)', 'Normal', 'Uniforme continua', 'Chi-cuadrado','t-student',
 'Pareto', 'Weibull', 'Triangular', 'Uniforme discreta', 'Bernoulli', 'Poisson', 'Binomial', 'Geométrica')

dist_seleccionada = tk.StringVar()
dist_cb = ttk.Combobox(root, textvariable=dist_seleccionada)
dist_cb.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)
dist_cb['values'] = dist
dist_cb['state'] = 'readonly'

def checkDist():
    if semilla_entry.get() != "":
        if dist_seleccionada.get() != "":

            if dist_seleccionada.get() == "Binomial":
                print("hola mundo") #en vez de hola mundo, se debiese abrir una ventana para ingresar parametros especificos de la binomial y asi para cada caso

        else:
            print("Mostrar mensaje de que falta rellenar distribucion")
    else:
        print("Mostrar mensaje de que falta rellenar semilla")

# Botón generar
login_button = ttk.Button(root, text="Generar", command= checkDist)
login_button.grid(column=0, row=3, columnspan=2, sticky=tk.EW, padx=5, pady=5)

root.mainloop()