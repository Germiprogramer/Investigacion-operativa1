# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "4*x-4"
Z = "(7-3*x)/6"
x = symbols('x')
plot(f1, Z, (x, 0, 10))