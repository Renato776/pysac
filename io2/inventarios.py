from sympy import plot, symbols
import sympy as ren

def p_section(title):
    return f'\\section{{{title}}}\n'
def p_subsection(title):
    return f'\\subsection{{{title}}}\n'
def p_subsubsection(title):
    return f'\\subsubsection{{{title}}}\n'
def itemize(data):
    aux = '\\begin{itemize}\n'
    for d in data:
        aux += f'\\item {d}\n'
    return aux + '\\end{itemize}\n'

class Inventario:
    def print_data(self,args):
        aux = p_subsection('Datos')
        data = []
        for key in args:
            data.append(f'{key} = {args[key]}')
        return aux + itemize(data)
    def __init__(self, name,**kwargs):
        self.content = p_section(name)
        self.values = kwargs
        self.tuplas = []
        for v in kwargs:
            self.tuplas.append((symbols(v),kwargs[v]))
        self.content += self.print_data(kwargs)
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
                        'p': symbols('p')}
        if 'k' in kwargs:
            if 'c2' in kwargs:
                self.model = 1
                self.Q = ren.sqrt((2 * self.symbols['r'] * self.symbols['c3'] *
                                   (self.symbols['c1'] + self.symbols['c2'])) /
                                  (self.symbols['c1'] * self.symbols['c2'] * (
                                              1 - self.symbols['r'] / self.symbols['k'])))
                self.content += p_subsection('Cantidad Optima (Q)')
                self.content += f'Q = ${ren.latex(self.Q)}$\n'
                self.content += f'Q = {self.Q.subs(self.tuplas)}\n'
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
                self.model = 2
                self.Q = ren.sqrt((2*self.symbols['r']*self.symbols['c3'])/
                                  (self.symbols['c1']*(1-self.symbols['r']/self.symbols['k'])))
                self.C = ren.sqrt(2 * self.symbols['r']* self.symbols['c1']*
                                  self.symbols['c3']*(1-self.symbols['r']/self.symbols['k']))
                self.t2 = ren.sqrt((2*self.symbols['c3']*(1-self.symbols['r']/self.symbols['k']))
                                   /(self.symbols['r'] * self.symbols['c1']))
                self.Ct = self.symbols['c3']*self.symbols['r']/self.symbols['Q'] \
                          + self.symbols['c1']*self.symbols['Q']*(self.symbols['k']-self.symbols['r'])\
                          /(2*self.symbols['k']) + self.symbols['p']*self.symbols['r']
        else:
            if 'c2' in kwargs:
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
                self.Ct = self.symbols['S'] ** 2 * self.symbols['c1']/(2*self.symbols['Q']) \
                         + self.symbols['D']**2 * self.symbols['c2']/(2*self.symbols['Q']) \
                          + self.symbols['c3']*self.symbols['r']/self.symbols['Q'] + \
                          self.symbols['p']*self.symbols['r']

            else:
                self.model = 4
                self.Q = ren.sqrt(2*self.symbols['r']*self.symbols['c3']/self.symbols['c1'])
                self.C = ren.sqrt(2*self.symbols['r']*self.symbols['c1']*self.symbols['c3'])
                self.t2 = ren.sqrt(2*self.symbols['c3']/(self.symbols['r']*self.symbols['c1']))
                self.Ct = self.symbols['c3'] * self.symbols['r'] / self.symbols['Q'] \
                          + self.symbols['c1']*self.symbols['Q']/2 + self.symbols['p']*self.symbols['r']
        if 'c2' not in kwargs:
            self.values['c2'] = 0
        if 'k' not in kwargs:
            self.values['k'] = 0


    def resumen(self):
        return self.content
        #return f'Q = ${ren.latex(self.Q)}$'
