#Variante general

# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
#ponemos las funciones de las restricciones, siendo f la diversion y x el estudio #<=
f2 = "1+x"
f3 = "x-1"
#y=4
f4 = "4" #<=
#las z son las funciones objetivo, despejamos la diversion y damos los valores que queramos a la z
Z1 = "(13-x)/2"


x = symbols('x')
#esto se pone asi siempre, 0 y 15 es el intervalo en el que queramos que se plotee
p = plot(f2, f3, f4, Z1, (x, 0, 15))

p.save('ejercicio2/dibujos/dibujo_2.png')