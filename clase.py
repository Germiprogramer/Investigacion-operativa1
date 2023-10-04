https://collabedit.com/evjh5
https://campus.uax.es/moodle/course/view.php?id=8799

# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "5+0*x"
f2 = "8-2*x"
x = symbols('x')
plot(f1, f2, (x, 0, 5))


# Modelo 1
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x"
f2 = "1+x"
#y=4
f3 = "4" 
x = symbols('x')
plot(f1, f2, f3, (x, 15, 0))


# Modelo 1b
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x"
f2 = "x-1"
# x=4
#f3 = "4"
x = symbols('x')
plot(f1, f2, (x, 15, 0))
