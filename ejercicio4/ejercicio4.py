#Plan original

# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "600"
f2 = "1200"
f3 = "800 - x"
f4 = "x + 450"
#los otros dos cortes son los ejes
Z = "(7-5*x)/8"
x = symbols('x')
p = plot(f1, f2, f3, Z, (x, 0, 850))

p.save('ejercicio4/dibujos/dibujo_ejer4a.png')