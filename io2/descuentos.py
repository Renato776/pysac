from sympy import plot, symbols
from base import *
class Descuento:
    def __init__(self,name,**kwargs):
        self.content = p_section(name) + print_data(kwargs)
        self.values = kwargs
        self.targets = {'Q':'Cantidad optima','Ct':'Costo total'}
        self.symbols = {'r':symbols('r'),
                        'c1':symbols('c1'),
                        'c3':symbols('c3'),
                        'p':symbols('p'),
                        'Q':symbols('Q'),
                        'Ct':symbols('Ct')}
        get_latex_symbols(self)
        self.Q = ren.sqrt(2 * self.symbols['r'] * self.symbols['c3'] / self.symbols['c1'])
        self.Ct = self.symbols['c3'] * self.symbols['r'] / self.symbols['Q'] \
                  + self.symbols['c1'] * self.symbols['Q'] / 2 + self.symbols['p'] * self.symbols['r']
        prices = self.values['prices']
        jk = self.values['p']
        jm = self.values['c1']
        self.table = [('Cantidad','Descuento','Precio','q*','Q*','Costo')]
        for price_entry in prices:
            lower = price_entry[0][0]
            upper = price_entry[0][1]
            price = price_entry[1]
            self.values['p'] = round(price.subs(symbols('p'),jk),4)
            self.values['c1'] = round(jm.subs(symbols('p'),self.values['p']),4)
            self.content += p_section(f'\\Huge q in [{lower},{upper}] p = {self.values["p"]}')
            get_tuplas(self,['Q','Ct'])
            qr = process(self,'Q',True)
            if not (lower <= qr <= upper):
                if qr < lower:
                    self.values['Q'] = lower
                elif qr > upper:
                    self.values['Q'] = upper
            self.tuplas.pop()
            self.tuplas.append((ren.symbols('Q'), self.values['Q']))
            cr = process(self,'Ct',True)
            self.table.append((f'{lower}-{upper}',str(-1*get_discount(self.values['p'],jk))+'\\%',
                               str(self.values['p']),str(qr),str(self.values['Q']),str(cr)))
        self.content += p_section('Resumen')+'\\begin{large}\n'
        self.content += print_table(self.table) +'\\end{large}\n\\pagebreak\n'
    def resumen(self):
        return self.content