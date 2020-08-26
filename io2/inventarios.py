from sympy import plot, symbols
import sympy as ren


class Inventario:
    def __init__(self, **kwargs):
        self.r = kwargs['r']
        self.c1 = kwargs['c1']
        self.c3 = kwargs['c3']
        self.symbols = {'r': symbols('r'),
                        'k': symbols('k'),
                        'c1': symbols('c1'),
                        'c2': symbols('c2'),
                        'c3': symbols('c3'),
                        'Q': symbols('Q'),
                        't': symbols('t'),
                        't1': symbols('t1'),
                        't2': symbols('t2'),
                        't3': symbols('t3'),
                        't4': symbols('t4'),
                        'C': symbols('C'),
                        'S': symbols('S'),
                        'D': symbols('D')}
        if 'k' in kwargs:
            if 'c2' in kwargs:
                self.model = 1
                self.Q = ren.sqrt((2 * self.symbols['r'] * self.symbols['c3'] *
                                   (self.symbols['c1'] + self.symbols['c2'])) /
                                  (self.symbols['c1'] * self.symbols['c2'] * (
                                              1 - self.symbols['r'] / self.symbols['k'])))
                self.S = ren.sqrt((2 * self.symbols['r'] * self.symbols['c3'] *
                                   (1 - self.symbols['r']/self.symbols['k']))/self.symbols['c1'])
                self.C = ren.sqrt(2 * self.symbols['r'] * self.symbols['c1'] * self.symbols['c3'] * (1 - self.symbols['r']/self.symbols['k']))

            else:
                self.a = 2
        else:
            if 'c2' in kwargs:
                self.a = 3
            else:
                self.model = 4

    def resumen(self):
        return f'Q = ${ren.latex(self.Q)}$'
