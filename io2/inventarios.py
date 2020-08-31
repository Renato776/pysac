from sympy import plot, symbols
import sympy as ren
import re

def extract_chars(string):
    chars = ''
    nums = ''
    for char in string:
        if char.isnumeric():
            nums += char
        else:
            chars += char
    return chars, nums
def p_section(title):
    return f'\\section{{\\Huge {title}}}\n'
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
        aux = p_subsection('\\Huge Datos')
        data = []
        for key in args:
            data.append(f'{key} = {args[key]}')
        return f'{aux}\\begin{{huge}}\n{itemize(data)}\\end{{huge}}'
    def __init__(self, name,**kwargs):
        self.content = p_section(name)
        self.values = kwargs
        self.latex_symbols = {}
        self.targets = {'Q':'Inventario Optimo','S':'Inventario Maximo',\
                        'C':'Costo Normal','D':'Carencia Maxima','t2':'Tiempo en agotarse el inventario',\
                        't1':'Tiempo de produccion','t3':'Tiempo incurrido en faltantes',\
                        't4':'Tiempo en recuperar los faltantes','Ct':'Costo Total'}
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
        for s in self.symbols:
            aux = extract_chars(s)
            self.latex_symbols[s] = s if aux[1] == '' else f'{aux[0]}_{{{aux[1]}}}'
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
                self.content +='\\begin{huge}\n'
                jimin = ren.latex(getattr(self,r))
                self.content += f'${r} = {jimin}$\\rbreak\n'
                kwargs[r] = round(float(getattr(self,r).subs(self.tuplas)),4)
                self.tuplas.append((r,kwargs[r]))
                aux = jimin
                for l in self.latex_symbols:
                    ll = self.latex_symbols[l]
                    if l not in kwargs:
                        continue
                    if ll.find('}') < 0:
                        aux = re.sub(r"\b%s\b" % ll , f' ({kwargs[ll]}) ', aux)
                    else:
                        aux = aux.replace(ll,f'({kwargs[l]})')
                self.content += f'${r} = {aux}$\\rbreak\n'
                self.content += f'${r} = {round(float(self.tuplas[len(self.tuplas)-1][1]),3)}$\n'
                self.content += '\\end{huge}\n'

    def resumen(self):
        return self.content
        #return f'Q = ${ren.latex(self.Q)}$'
