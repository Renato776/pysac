from base import LATEX_HEADER
from sympy import plot
from sympy.abc import x, y, z, n, t


class Inventario:
    def __init__(self):
        self.someText = f'Hello imported text: {LATEX_HEADER}'

    def resumen(self):
        graph = plot(x**2, show=False)
        fig = 'parabola-1'
        graph.save(f'/home/renato/PycharmProjects/pysac/out/plots/{fig}.png')
        return 'I printed my own text {}.'.format(self.someText)
