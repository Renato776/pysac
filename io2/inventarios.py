from sympy import symbols

from base import *

class Inventario:
    def __init__(self, name,**kwargs):
        self.values = kwargs
        self.content = print_data(kwargs)
        self.targets = {'Q':'Inventario Optimo','S':'Inventario Maximo',\
                        'C':'Costo Normal','D':'Carencia Maxima','t2':'Tiempo en agotarse el inventario',\
                        't1':'Tiempo de produccion','t3':'Tiempo incurrido en faltantes',\
                        't4':'Tiempo en recuperar los faltantes','Ct':'Costo Total','tp':'Tiempo de produccion',\
                        'tc':'tiempo de consumo','tt':'Tiempo total'}
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
                        'D': symbols('D'),
                        'p': symbols('p'),
                        'Ct': symbols('Ct'),
                        'tc': symbols('tc'),
                        'tp':symbols('tp'),
                        'tt':symbols('tt')}
        get_tuplas(self)
        get_latex_symbols(self)
        if 'k' in kwargs:
            if 'c2' in kwargs:
                self.model = 'Ciclo productivo con faltantes permitidos'
                self.Q = ren.sqrt((2 * self.symbols['r'] * self.symbols['c3'] *
                                   (self.symbols['c1'] + self.symbols['c2'])) /
                                  (self.symbols['c1'] * self.symbols['c2'] * (
                                              1 - self.symbols['r'] / self.symbols['k'])))
                self.S = ren.sqrt((2 * self.symbols['r'] * self.symbols['c2'] * self.symbols['c3']
                                   * (1 - self.symbols['r']/self.symbols['k']))/((self.symbols['c1']
                                  + self.symbols['c2'])*self.symbols['c1']))
                self.C = ren.sqrt((2 * self.symbols['r'] * self.symbols['c1']
                                   * self.symbols['c2'] * self.symbols['c3']
                                   * (1 - self.symbols['r']/self.symbols['k']))
                                  /(self.symbols['c1']+self.symbols['c2']))
                self.D = self.symbols['Q'] - self.symbols['S']
                self.t2 = ren.sqrt((2*self.symbols['c2'] * self.symbols['c3']
                                    * (1 - self.symbols['r'] / self.symbols['k']))
                                   /(self.symbols['r']*(self.symbols['c1'] + self.symbols['c2'])
                                     *self.symbols['c1']))
                self.t3 = ren.sqrt((2*self.symbols['c1'] * self.symbols['c3'] *
                                    (1 - self.symbols['r'] / self.symbols['k']))
                                   /(self.symbols['r']*(self.symbols['c1'] +
                                self.symbols['c2'])*self.symbols['c2']))
                self.t1 = ren.sqrt((self.symbols['t2']*self.symbols['r'])
                                   /(self.symbols['k'] - self.symbols['r']))
                self.t4 = ren.sqrt((self.symbols['t3']*self.symbols['r'])
                                   /(self.symbols['k'] - self.symbols['r']))

            else:
                self.model = 'Ciclo productivo sin faltantes'
                self.Q = ren.sqrt((2*self.symbols['r']*self.symbols['c3'])/
                                  (self.symbols['c1']*(1-self.symbols['r']/self.symbols['k'])))
                self.S = ren.sqrt(2 * self.symbols['r'] * self.symbols['c3']*(1 - self.symbols['r']/self.symbols['k'])/self.symbols['c1'])
                self.C = ren.sqrt(2 * self.symbols['r']* self.symbols['c1']*
                                  self.symbols['c3']*(1-self.symbols['r']/self.symbols['k']))
                self.t2 = ren.sqrt((2*self.symbols['c3']*(1-self.symbols['r']/self.symbols['k']))
                                   /(self.symbols['r'] * self.symbols['c1']))
                if 'p' in kwargs:
                    self.Ct = self.symbols['c3']*self.symbols['r']/self.symbols['Q'] \
                          + self.symbols['c1']*self.symbols['Q']*(self.symbols['k']-self.symbols['r'])\
                          /(2*self.symbols['k']) + self.symbols['p']*self.symbols['r']
        else:
            if 'c2' in kwargs:
                self.model = 'Reabastecimiento instantaneo con faltantes'
                self.Q = ren.sqrt(2*self.symbols['r']*self.symbols['c3']*(self.symbols['c1']+self.symbols['c2'])
                                  /(self.symbols['c1']+self.symbols['c2']))
                self.C = ren.sqrt(2*self.symbols['r']*self.symbols['c1']*self.symbols['c2']*self.symbols['c3']
                                  /(self.symbols['c1']+self.symbols['c2']))
                self.S = ren.sqrt(2*self.symbols['r']*self.symbols['c2']*self.symbols['c3']
                                  /((self.symbols['c1']+self.symbols['c2'])*self.symbols['c1']))
                self.D = self.symbols['Q'] - self.symbols['S']
                self.t2 = ren.sqrt(2*self.symbols['c2']*self.symbols['c3']/(self.symbols['r']
                                *(self.symbols['c1']+self.symbols['c2'])*self.symbols['c1']))
                self.t3 = ren.sqrt(2*self.symbols['c1']*self.symbols['c3']/(self.symbols['r']
                                *(self.symbols['c1']+self.symbols['c2'])*self.symbols['c2']))
                if 'p' in kwargs:
                    self.Ct = self.symbols['S'] ** 2 * self.symbols['c1']/(2*self.symbols['Q']) \
                         + self.symbols['D']**2 * self.symbols['c2']/(2*self.symbols['Q']) \
                          + self.symbols['c3']*self.symbols['r']/self.symbols['Q'] + \
                          self.symbols['p']*self.symbols['r']

            else:
                self.model = 'Reabastecimiento instantaneo sin faltantes'
                self.Q = ren.sqrt(2*self.symbols['r']*self.symbols['c3']/self.symbols['c1'])
                self.C = ren.sqrt(2*self.symbols['r']*self.symbols['c1']*self.symbols['c3'])
                self.t2 = ren.sqrt(2*self.symbols['c3']/(self.symbols['r']*self.symbols['c1']))
                if 'p' in kwargs:
                    self.Ct = self.symbols['c3'] * self.symbols['r'] / self.symbols['Q'] \
                          + self.symbols['c1']*self.symbols['Q']/2 + self.symbols['p']*self.symbols['r']
        if 'k' in kwargs:
            self.tp = self.symbols['Q'] / self.symbols['k']
        self.tc = self.symbols['Q'] / self.symbols['r']
        if 'k' in kwargs:
            self.tt = self.symbols['tc'] + self.symbols['tp']
        else:
            self.tt = self.symbols['tc']
        self.content = p_section(name) + f'\\Huge {self.model}\n' + self.content
        for r in self.targets:
            process(self,r)
    def resumen(self):
        return self.content
        #return f'Q = ${ren.latex(self.Q)}$'
