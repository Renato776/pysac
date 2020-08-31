from sympy import symbols
from base import *
import sympy as ren
class Estocastico:
    def __init__(self,name,**kwargs):
        self.values = kwargs
        c1 = kwargs['c1'] #c1 must always be provided.
        c2 = kwargs['c2'] #c2 must always be provided.
        distribution = kwargs['dist'] #A distribution must always be provided.
        # it can be expressed as an array of tuples (Discrete) or as a Sympy expression (Continuous)
        # Whatever is the way it must always be provided
        s_c1 = symbols('c1')
        s_c2 = symbols('c2')
        setattr(self,'F',s_c2 / (s_c1 + s_c2))
        self.content = print_data(kwargs)
        self.content += p_section(name)
        self.targets ={ 'S':'Cantidad a ordenar',
                        'C':'Costo Asociado'}
        self.symbols = {'F': symbols('F'),
                        'c1': symbols('c1'),
                        'c2': symbols('c2'),
                        'C': symbols('C'),
                        'S': symbols('S')}
        get_tuplas(self)
        get_latex_symbols(self)
