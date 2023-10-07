
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
#ponemos las funciones de las restricciones, siendo f la diversion y x el estudio
f1 = "10-x" #<=
f2 = "1+x"
f3 = "x-1"
#y=4
f4 = "10" #<=
#las z son las funciones objetivo, despejamos la diversion y damos los valores que queramos a la z

#en este caso, la f es el estudio y la x la diversion, para poder poner la condicion 4
Z1 = "(10-2*x)"



x = symbols('x')
#esto se pone asi siempre, 0 y 15 es el intervalo en el que queramos que se plotee
p = plot(f1, f2, f3, f4, Z1, (x, 0, 15))

p.save('ejercicio2/dibujos/dibujo_4.png')

# d = 10
