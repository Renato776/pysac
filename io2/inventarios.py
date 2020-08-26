from sympy import plot
from sympy.abc import x, y, z, n, t


class Inventario:
    def __init__(self):
        self.something = 0


    def resumen(self):
        graph = plot(x**2, show=False)
        fig = 'parabola-1'
        graph.save(f'/home/renato/PycharmProjects/pysac/out/plots/{fig}.png')
        return 'I printed my own text'
