from base import LATEX_HEADER
from sympy import plot
from sympy.abc import x,y,z,n,t
class Inventario:
    def __init__(self):
        self.someText = f'Hello imported text: {LATEX_HEADER}'

    def resumen(self):
        graph = plot(x**2, show=False)
        graph.save('./out/parabola.png')
        return 'I printed my own text {}.'.format(self.someText)
