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
        self.targets = {'Q':'Cantidad Optima','S':'Cantidad Maxima en inventario',\
                        'C':'Costo','D':'Cantidad maxima de faltantes','t2':'tiempo 2',\
                        't1':'tiempo 1','t3':'tiempo 3','t4':'tiempo 4','Ct':'Costo total'}
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
                        'p': symbols('p'),
                        'Ct': symbols('Ct')}
        if 'k' in kwargs:
            if 'c2' in kwargs:
                self.model = 1
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
        for r in self.targets:
            if hasattr(self,r):
                self.content += p_section(f'\\Huge {self.targets[r]} ({r})')
                self.content +='\\begin{Huge}\n'
                self.content += f'{r} = ${ren.latex(getattr(self,r))}$\\linebreak\\linebreak\n'
                self.tuplas.append((r,getattr(self,r).subs(self.tuplas)))
                self.content += f'{r} = {self.tuplas[len(self.tuplas)-1][1]}\n'
                self.content += '\\end{Huge}\n'

    def resumen(self):
        return self.content
        #return f'Q = ${ren.latex(self.Q)}$'
