import tkinter as tk
from tkinter import ttk
from turtle import right
from tkinter import messagebox

from numpy import array

from binomial import *
from erlang import *
from exponencial import *
from normal_estandar import *
from normal import *
from uniformeContinua import *
from chiCuadrado import *
from tStudent import *
from pareto import *
from weibull import *
from triangular import *
from uniformeDiscreta import *
from bernoulli import *
from poisson import *
from geometrica import *

#Crear ventana
root = tk.Tk()
root.title('Simulación')
root.resizable(0, 0)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#Crear frame principal
main_frame = ttk.Frame(root)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.grid(row=0, sticky=tk.EW, padx=5, pady=5)

#Crear frame de districución
dist_frame = ttk.Frame(root, borderwidth=2, relief="groove")
dist_frame.columnconfigure(0, weight=1)
dist_frame.columnconfigure(1, weight=1)

#Función para eliminar frame de districubión
def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
    frame.grid_forget()

#Verificar que un número sea decimal
def es_decimal(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#Verificar que un número sea decimal positivo
def es_decimal_positivo(s):
    try:
        if float(s) > 0:
            return True
        return False
    except ValueError:
        return False

#Verificar que un campo sea entero, ejemplo: -21, 21 o 21.0
def es_entero(i):
    try:
        if float(i).is_integer():
            return True
        return False
    except ValueError:
        return False

#Verificar que un campo sea entero positivo, ejemplo: 21 o 21.0
def es_entero_positivo(i):
    try:
        if float(i).is_integer() and int(i) > 0:
            return True
        return False
    except ValueError:
        return False
#Verificar que los campos no están vacios
def campo_vacio(campo, nombre):
    if campo == "":    
        messagebox.showinfo(message="El campo '" + nombre + "' es obligatorio", title="Campos vacíos")
        return True
    return False

#Verificar que los valores principales sean enteros
def error_in_main(semilla_congru, cant_alea):
    if campo_vacio(semilla_congru, "Semilla Congruencial Multiplicativo"):   
        return True
    elif not es_entero(semilla_congru):
        messagebox.showinfo(message="El campo 'Semilla Congruencial Multiplicativo' debe ser un número entero", title="Valor incorrecto")
        return True
    elif campo_vacio(cant_alea, "Cantidad de Números Aleatorios"):
        return True
    elif not es_entero(cant_alea):
        messagebox.showinfo(message="El campo 'Cantidad de Números Aleatorios' debe ser un número entero", title="Valor incorrecto")
        return True
    return False

#Funciones para crear Widgets
def init_label(frame, fila, nombre):
    label = ttk.Label(frame, text=nombre)
    label.grid(column=0, row=fila, sticky=tk.W, padx=5, pady=5)
    return label
def init_entry(frame, fila):
    entry = ttk.Entry(frame)
    entry.grid(column=1, row=fila, sticky=tk.EW, padx=5, pady=5)
    return entry
def init_muestrear_button(frame, fila):
    buttonM = ttk.Button(frame, text="Muestrear")
    buttonM.grid(column=0, row=fila, columnspan=2, sticky=tk.E, padx=5, pady=5)
    return buttonM

def init_distframe():
    dist_frame.grid(row=1, sticky=tk.EW, padx=5, pady=5)


#Frames para las distribuciones
def tk_exp():
    init_distframe()
    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    lambda_label = init_label(dist_frame, 1, "Lambda:")
    lambda_entry = init_entry(dist_frame, 1)
    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 2)
    buttonM.config(command= lambda: run_exp(semilla_entry, lambda_entry))

def tk_erlang():
    init_distframe()

    semillas_label = init_label(dist_frame, 0, "Semillas Con. Mul. (Separadas por ';'):")
    semillas_entry = init_entry(dist_frame, 0)

    lambda_label = init_label(dist_frame, 1, "Lambda:")
    lambda_entry = init_entry(dist_frame, 1)
    k_label = init_label(dist_frame, 2, "K:")
    k_entry = init_entry(dist_frame, 2)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 3)
    buttonM.config(command= lambda: run_erlang(semillas_entry, lambda_entry, k_entry))

def tk_normal_estandar():
    init_distframe()

    semilla1_label = init_label(dist_frame, 0, "Semilla Con. Mul. 1:")
    semilla1_entry = init_entry(dist_frame, 0)

    semilla2_label = init_label(dist_frame, 1, "Semilla Con. Mul. 2:")
    semilla2_entry = init_entry(dist_frame, 1)

    media_label = init_label(dist_frame, 2, "Media:")
    media_entry = init_entry(dist_frame, 2)
    media_entry.insert(-1, 0)
    media_entry.config(state='disabled')
    var_label = init_label(dist_frame, 3, "Varianza:")
    var_entry = init_entry(dist_frame, 3)
    var_entry.insert(-1, 1)
    var_entry.config(state='disabled')

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 4)
    buttonM.config(command= lambda: run_normal_estandar(semilla1_entry, semilla2_entry))
    
def tk_normal():
    init_distframe()

    semilla1_label = init_label(dist_frame, 0, "Semilla Con. Mul. 1:")
    semilla1_entry = init_entry(dist_frame, 0)

    semilla2_label = init_label(dist_frame, 1, "Semilla Con. Mul. 2:")
    semilla2_entry = init_entry(dist_frame, 1)

    media_label = init_label(dist_frame, 2, "Media:")
    media_entry = init_entry(dist_frame, 2)
    var_label = init_label(dist_frame, 3, "Varianza:")
    var_entry = init_entry(dist_frame, 3)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 4)
    buttonM.config(command= lambda: run_normal(media_entry, var_entry, semilla1_entry, semilla2_entry))


def tk_continua():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    a_label = init_label(dist_frame, 1, "Valor mínimo:")
    a_entry = init_entry(dist_frame, 1)
    b_label = init_label(dist_frame, 2, "Valor máximo:")
    b_entry = init_entry(dist_frame, 2)
    
    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 3)
    buttonM.config(command= lambda: run_continua(a_entry, b_entry, semilla_entry))

def tk_chi():
    init_distframe()

    semilla1_label = init_label(dist_frame, 0, "Semilla Con. Mul. 1:")
    semilla1_entry = init_entry(dist_frame, 0)

    semilla2_label = init_label(dist_frame, 1, "Semilla Con. Mul. 2:")
    semilla2_entry = init_entry(dist_frame, 1)

    grados_label = init_label(dist_frame, 2, "Grados de libertad:")
    grados_entry = init_entry(dist_frame, 2)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 3)
    buttonM.config(command= lambda: run_chi(grados_entry, semilla1_entry, semilla2_entry))


def tk_student():
    init_distframe()

    semilla1_label = init_label(dist_frame, 0, "Semilla Con. Mul. 1:")
    semilla1_entry = init_entry(dist_frame, 0)

    semilla2_label = init_label(dist_frame, 1, "Semilla Con. Mul. 2:")
    semilla2_entry = init_entry(dist_frame, 1)

    semilla3_label = init_label(dist_frame, 2, "Semilla Con. Mul. 3:")
    semilla3_entry = init_entry(dist_frame, 2)

    grados_label = init_label(dist_frame, 3, "Grados de libertad")
    grados_entry = init_entry(dist_frame, 3)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 4)
    buttonM.config(command= lambda: run_student(grados_entry, semilla1_entry, semilla2_entry, semilla3_entry))


def tk_pareto():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    a_label = init_label(dist_frame, 1, "Forma:")
    a_entry = init_entry(dist_frame, 1)
    b_label = init_label(dist_frame, 2, "Escala:")
    b_entry = init_entry(dist_frame, 2)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 3)
    buttonM.config(command= lambda: run_pareto(a_entry, b_entry, semilla_entry))

def tk_weibull():
    init_distframe()

    semilla1_label = init_label(dist_frame, 0, "Semilla Con. Mul. 1:")
    semilla1_entry = init_entry(dist_frame, 0)

    semilla2_label = init_label(dist_frame, 1, "Semilla Con. Mul. 2:")
    semilla2_entry = init_entry(dist_frame, 1)

    a_label = init_label(dist_frame, 2, "Forma:")
    a_entry = init_entry(dist_frame, 2)
    b_label = init_label(dist_frame, 3, "Escala:")
    b_entry = init_entry(dist_frame, 3)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 4)
    buttonM.config(command= lambda: run_weibull(a_entry, b_entry, semilla1_entry, semilla2_entry))

def tk_triangular():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    a_label = init_label(dist_frame, 1, "Valor mínimo:")
    a_entry = init_entry(dist_frame, 1)
    b_label = init_label(dist_frame, 2, "Valor máximo:")
    b_entry = init_entry(dist_frame, 2)
    m_label = init_label(dist_frame, 3, "Moda:")
    m_entry = init_entry(dist_frame, 3)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 4)
    buttonM.config(command= lambda: run_triangular(a_entry, b_entry, m_entry, semilla_entry))

def tk_discreta():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    a_label = init_label(dist_frame, 1, "Valor mínimo:")
    a_entry = init_entry(dist_frame, 1)
    b_label = init_label(dist_frame, 2, "Valor máximo:")
    b_entry = init_entry(dist_frame, 2)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 3)
    buttonM.config(command= lambda: run_discreta(a_entry, b_entry, semilla_entry))

def tk_bernoulli():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    prob_label = init_label(dist_frame, 1, "Probabilidad:")
    prob_entry = init_entry(dist_frame, 1)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 2)
    buttonM.config(command= lambda: run_bernoulli(prob_entry, semilla_entry))

def tk_poisson():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    lambda_label = init_label(dist_frame, 1, "Lambda:")
    lambda_entry = init_entry(dist_frame, 1)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 2)
    buttonM.config(command= lambda: run_poisson(lambda_entry, semilla_entry))

def tk_binomial():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    prob_label = init_label(dist_frame, 1, "Probabilidad:")
    prob_entry = init_entry(dist_frame, 1)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 2)
    buttonM.config(command= lambda: run_binomial(prob_entry, semilla_entry))

def tk_geometrica():
    init_distframe()

    semilla_label = init_label(dist_frame, 0, "Semilla Congruencial Multiplicativo:")
    semilla_entry = init_entry(dist_frame, 0)

    prob_label = init_label(dist_frame, 1, "Probabilidad:")
    prob_entry = init_entry(dist_frame, 1)

    #Muestreo
    buttonM = init_muestrear_button(dist_frame, 2)
    buttonM.config(command= lambda: run_geometrica(prob_entry, semilla_entry))

#Graficar distribuciones
def run_exp(semilla_entry, lambda_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    lamb = lambda_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(lamb, "Lambda"):   
        return True
    if not es_entero(lamb):    
        messagebox.showinfo(message="El campo 'Lambda' debe ser un número entero", title="Valor incorrecto")
        return
    exponencial(int(float(lamb)), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_erlang(semillas_entry, lambda_entry, k_entry):
    semillas_congru =  semillas_entry.get()
    cant_alea =  cant_alea_entry.get()
    lamb = lambda_entry.get()
    k = k_entry.get()
    arraySemillas = semillas_congru.split(';')
    arraySemillas = list(map(int, arraySemillas))
    for semilla in arraySemillas:
        if error_in_main(semilla, cant_alea):
            return
    if campo_vacio(lamb, "Lambda"):   
        return True
    if not es_decimal_positivo(lamb):
        messagebox.showinfo(message="El campo 'Lambda' debe ser un número real positivo", title="Valor incorrecto")
        return
    if campo_vacio(k, "K"):   
        return True
    if not es_entero_positivo(k):
        messagebox.showinfo(message="El campo 'K' debe ser un número entero positivo", title="Valor incorrecto")
        return
    if int(k) != len(arraySemillas):   
        messagebox.showinfo(message="El campo 'K' debe ser igual a la cantidad de semillas", title="Valor incorrecto")
        return True
    print(arraySemillas)
    erlang(int(float(lamb)), int(float(cant_alea)),int(float(k)), arraySemillas).muestreo()

def run_normal_estandar(semilla1_entry, semilla2_entry):
    semilla1 =  semilla1_entry.get()
    semilla2 =  semilla2_entry.get()
    cant_alea =  cant_alea_entry.get()
    if error_in_main(semilla1, cant_alea) or error_in_main(semilla2, cant_alea):
        return
    normal_estandar(int(float(cant_alea)), int(float(semilla1)), int(float(semilla2))).muestreo()

def run_normal(media_entry, var_entry, semilla1_entry, semilla2_entry):
    semilla1 =  semilla1_entry.get()
    semilla2 =  semilla2_entry.get()
    cant_alea =  cant_alea_entry.get()
    media =  media_entry.get()
    varianza =  var_entry.get()
    if error_in_main(semilla1, cant_alea) or error_in_main(semilla2, cant_alea):
        return
    if campo_vacio(media, "Media"):   
        return True
    if campo_vacio(varianza, "Varianza"):   
        return True
    if not es_decimal_positivo(varianza):
        messagebox.showinfo(message="El campo 'Varianza' debe ser un número real positivo", title="Valor incorrecto")
        return
    normal(float(media), float(varianza), int(float(cant_alea)), int(float(semilla1)), int(float(semilla2))).muestreo()

def run_continua(a_entry, b_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    a =  a_entry.get()
    b =  b_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(a, "Valor mínimo"):   
        return True
    if campo_vacio(b, "Valor máximo"):   
        return True
    if a >= b:
        messagebox.showinfo(message="El campo 'Valor mínimo' debe ser menor que el campo 'Valor máximo'", title="Valor incorrecto")
        return
    uniformeContinua(float(a), float(b), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_chi(grados_entry, semilla1_entry, semilla2_entry):
    semilla1 =  semilla1_entry.get()
    semilla2 =  semilla2_entry.get()
    cant_alea =  cant_alea_entry.get()
    grados =  grados_entry.get()
    if error_in_main(semilla1, cant_alea) or error_in_main(semilla2, cant_alea):
        return
    if campo_vacio(grados, "Grados de Libertad"):   
        return True
    if not es_entero_positivo(grados):
        messagebox.showinfo(message="El campo 'Grados de Libertad' debe ser un número entero positivo", title="Valor incorrecto")
        return
    chiCuadrado(int(float(grados)), int(float(cant_alea)), int(float(semilla1)), int(float(semilla2))).muestreo()

def run_student(grados_entry, semilla1_entry, semilla2_entry, semilla3_entry):
    semilla1 =  semilla1_entry.get()
    semilla2 =  semilla2_entry.get()
    semilla3 =  semilla3_entry.get()
    cant_alea =  cant_alea_entry.get()
    grados =  grados_entry.get()
    if error_in_main(semilla1, cant_alea) or error_in_main(semilla2, cant_alea) or error_in_main(semilla3, cant_alea):
        return
    if campo_vacio(grados, "Grados de Libertad"):   
        return True
    if not es_entero_positivo(grados):
        messagebox.showinfo(message="El campo 'Grados de Libertad' debe ser un número entero positivo", title="Valor incorrecto")
        return
    tstudent(int(float(grados)), int(float(cant_alea)), int(float(semilla1)), int(float(semilla2)), int(float(semilla3))).muestreo()

def run_pareto(a_entry, b_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    a =  a_entry.get()
    b =  b_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(a, "Forma"):   
        return True
    if campo_vacio(b, "Escala"):   
        return True
    if not es_decimal_positivo(a):
        messagebox.showinfo(message="El campo 'Forma' debe ser un número real positivo", title="Valor incorrecto")
        return
    if not es_decimal_positivo(b):
        messagebox.showinfo(message="El campo 'Escala' debe ser un número real positivo", title="Valor incorrecto")
        return
    pareto(float(a), float(b), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_weibull(a_entry, b_entry, semilla1_entry, semilla2_entry):
    semilla1 =  semilla1_entry.get()
    semilla2 =  semilla2_entry.get()
    cant_alea =  cant_alea_entry.get()
    a =  a_entry.get()
    b =  b_entry.get()
    if error_in_main(semilla1, cant_alea) or error_in_main(semilla2, cant_alea):
        return
    if campo_vacio(a, "Forma"):   
        return True
    if campo_vacio(b, "Escala"):   
        return True
    if not es_decimal_positivo(a):
        messagebox.showinfo(message="El campo 'Forma' debe ser un número real positivo", title="Valor incorrecto")
        return
    if not es_decimal_positivo(b):
        messagebox.showinfo(message="El campo 'Escala' debe ser un número real positivo", title="Valor incorrecto")
        return
    weibull(float(a), float(b), int(float(cant_alea)), int(float(semilla1)), int(float(semilla2))).muestreo()

def run_triangular(a_entry, b_entry, m_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    a =  a_entry.get()
    b =  b_entry.get()
    m = m_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(a, "Valor mínimo"):   
        return True
    if campo_vacio(b, "Valor máximo"):   
        return True
    if campo_vacio(m, "Moda"):   
        return True
    if a >= b:
        messagebox.showinfo(message="El campo 'Valor mínimo' debe ser menor que el campo 'Valor máximo'", title="Valor incorrecto")
        return
    if m < a or m > b:
        messagebox.showinfo(message="El campo 'Moda' debe ser mayor o igual que el campo 'Valor mínimo' y menor o igual al campo 'Valor máximo'", title="Valor incorrecto")
        return
    triangular(float(a), float(b), float(m), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_discreta(a_entry, b_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    a =  a_entry.get()
    b =  b_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(a, "Valor mínimo"):   
        return True
    if campo_vacio(b, "Valor máximo"):   
        return True
    if not es_entero_positivo(a):
        messagebox.showinfo(message="El campo 'Valor mínimo' debe ser un número entero positivo", title="Valor incorrecto")
        return
    if not es_entero_positivo(b):
        messagebox.showinfo(message="El campo 'Valor máximo' debe ser un número entero positivo", title="Valor incorrecto")
        return
    if a >= b:
        messagebox.showinfo(message="El campo 'Valor mínimo' debe ser menor que el campo 'Valor máximo'", title="Valor incorrecto")
        return
    uniformeDiscreta(float(a), float(b), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_bernoulli(prob_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    prob = prob_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(prob, "Probabilidad"):   
        return True
    if (not es_decimal(prob)) or float(prob) < 0 or float(prob) > 1:    
        messagebox.showinfo(message="El campo 'Probabilidad' debe ser un número entre 0 y 1", title="Valor incorrecto")
        return
    bernoulli(float(prob), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_poisson(lambda_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    lamb = lambda_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(lamb, "Lambda"):   
        return True
    if not es_entero_positivo(lamb):    
        messagebox.showinfo(message="El campo 'Lambda' debe ser un número entero positivo", title="Valor incorrecto")
        return
    poisson(int(float(lamb)), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_binomial(prob_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    prob = prob_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(prob, "Probabilidad"):   
        return True
    if (not es_decimal(prob)) or float(prob) < 0 or float(prob) > 1:    
        messagebox.showinfo(message="El campo 'Probabilidad' debe ser un número entre 0 y 1", title="Valor incorrecto")
        return
    binomial(float(prob), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

def run_geometrica(prob_entry, semilla_entry):
    semilla_congru =  semilla_entry.get()
    cant_alea =  cant_alea_entry.get()
    prob = prob_entry.get()
    if error_in_main(semilla_congru, cant_alea):
        return
    if campo_vacio(prob, "Probabilidad"):   
        return True
    if (not es_decimal(prob)) or float(prob) < 0 or float(prob) > 1:    
        messagebox.showinfo(message="El campo 'Probabilidad' debe ser un número entre 0 y 1", title="Valor incorrecto")
        return
    geometrica(float(prob), int(float(cant_alea)), int(float(semilla_congru))).muestreo()

# Selección de Distribución
def dist_changed(event):
    distSelect = dist_seleccionada.get()
    clear_frame(dist_frame)
    if distSelect == "Exponencial":
        tk_exp()
    elif distSelect == "Erlang":
        tk_erlang()
    elif distSelect == "Normal(0,1)":
        tk_normal_estandar()
    elif distSelect == "Normal":
        tk_normal()
    elif distSelect == "Uniforme continua":
        tk_continua()
    elif distSelect == "Chi-cuadrado":
        tk_chi()
    elif distSelect == "t-student":
        tk_student()
    elif distSelect == "Pareto":
        tk_pareto()
    elif distSelect == "Weibull":
        tk_weibull()
    elif distSelect == "Triangular":
        tk_triangular()
    elif distSelect == "Uniforme discreta":
        tk_discreta()
    elif distSelect == "Bernoulli":
        tk_bernoulli()
    elif distSelect == "Poisson":
        tk_poisson()
    elif distSelect == "Binomial":
        tk_binomial()
    elif distSelect == "Geométrica":
        tk_geometrica()
    else:
        messagebox.showinfo(message="Selección inválida", title="Error")

# Semilla
#semilla_label = ttk.Label(main_frame, text="Semilla Congruencial Multiplicativo:")
#semilla_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

#semilla_entry = ttk.Entry(main_frame)
#semilla_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

# Cantidad numeros aleatorios
cant_alea_label = ttk.Label(main_frame, text="Cantidad de Números Aleatorios:")
cant_alea_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

cant_alea_entry = ttk.Entry(main_frame)
cant_alea_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

# Distribución
dist_label = ttk.Label(main_frame, text="Distribución:")
dist_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

dist = ('Exponencial', 'Erlang', 'Normal(0,1)', 'Normal', 'Uniforme continua', 'Chi-cuadrado','t-student',
 'Pareto', 'Weibull', 'Triangular', 'Uniforme discreta', 'Bernoulli', 'Poisson', 'Binomial', 'Geométrica')

dist_seleccionada = tk.StringVar()
dist_cb = ttk.Combobox(main_frame, textvariable=dist_seleccionada)
dist_cb.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)
dist_cb['values'] = dist
dist_cb['state'] = 'readonly'
dist_cb.bind('<<ComboboxSelected>>', dist_changed)
dist_cb.set(dist[0])
dist_changed(1)

root.mainloop()