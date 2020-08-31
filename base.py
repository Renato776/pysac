HEADER_FILE = open('header.tex', 'r')
HEADER = HEADER_FILE.read()
HEADER_FILE.close()
FOOTER_FILE = open('footer.tex', 'r')
FOOTER = FOOTER_FILE.read()
FOOTER_FILE.close()
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

# This method expects self to have the following attributes:
# self.r  = Expr; where r is the name of the variable to evaluate (i.e Q) and expr is a Sympy expression.
# self.content = str; The buffer where the output is written to.
# self.values = kwargs; You must always assign kwargs to the values in constructor.
# self.tuplas = array[tuples]; An array of tuplas del tipo [(r,numeric value of r)...] where r is the variable to evaluate. r must be a symbol NOT an string.
# self.latex_symbols = dictionary; A dictionary del tipo {r:r_name} where r is a string name of the var to evaluate. r_name is
#       the latex name given r. (i.e the r var: c1 has latex name c_{1}) therefore: {'c1':'c_{1}'}
# self.symbols = dictionary; A dictionary containing a string name of the values & a sympy symbol for it.
def get_latex_symbols(self):
    self.latex_symbols = {}
    for s in self.symbols:
        aux = extract_chars(s)
        self.latex_symbols[s] = s if aux[1] == '' else f'{aux[0]}_{{{aux[1]}}}'

def get_tuplas(self,ignore=[]):
    self.tuplas = []
    for v in self.values:
        if v not in ignore: self.tuplas.append((ren.symbols(v), self.values[v]))
def get_discount(num,og):
    return num * 100 /og - 100
def print_table(table):
    template = '\\begin{center}\n'
    template += f'\\begin{{tabular}}{{ {" ".join(["c"] * len(table[0]))} }}\n'
    template += '\\\\\n'.join([' & '.join(t) for t in table])
    template += '\n\\end{tabular}\n\\end{center}\n'
    return template
def process(self,r,silent = False):
    if hasattr(self, r):
        if not silent: self.content += p_section(f'\\Huge {self.targets[r]} ({r})')
        self.content += '\\begin{huge}\n'
        jimin = ren.latex(getattr(self, r))
        self.content += f'${r} = {jimin}$\\rbreak\n'
        self.values[r] = round(float(getattr(self, r).subs(self.tuplas)), 4)
        self.tuplas.append((r, self.values[r]))
        aux = jimin
        for l in self.latex_symbols:
            ll = self.latex_symbols[l]
            if l not in self.values:
                continue
            if ll.find('}') < 0:
                aux = re.sub(r"\b%s\b" % ll, f' ({self.values[ll]}) ', aux)
            else:
                aux = aux.replace(ll, f'({self.values[l]})')
        self.content += f'${r} = {aux}$\\rbreak\n'
        self.content += f'${r} = {round(float(self.tuplas[len(self.tuplas) - 1][1]), 3)}$\n'
        self.content += '\\end{huge}\n'
        return round(float(self.values[r]),4)


def print_data(args):
    aux = p_subsection('\\Huge Datos')
    data = []
    for key in args:
        data.append(f'{key} = {args[key]}')
    return f'{aux}\\begin{{huge}}\n{itemize(data)}\\end{{huge}}'

class Doc:
    def __init__(self, name):
        self.name = name
        self.path = f'/home/renato/PycharmProjects/pysac/out/{self.name}.tex'
        self.content = HEADER + '\n'

    def append(self, subject):
        self.content += subject.resumen() + '\n'

    def save(self):
        self.content += FOOTER
        file = open(self.path, "w")
        file.write(self.content)
        file.close()
