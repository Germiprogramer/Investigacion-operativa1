# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "4-2*x"
f2 = "4*x-4"
f3 = "x+2"
#los otros dos cortes son los ejes
Z = "(7-3*x)/6"
x = symbols('x')
p = plot(f1, f2, f3, Z, (x, 0, 10))

p.save('ejercicio3/dibujos/dibujo_ejer3.png')