HEADER_F:ILE = open('header.tex', 'r')
HEADER = HEADER_FILE.read()
HEADER_FILE.close()
FOOTER_FILE = open('footer.tex', 'r')
FOOTER = FOOTER_FILE.read()
FOOTER_FILE.close()


class Doc:
    def __init__(self, name):
        self.name = name
        self.path = f'/home/renato/PycharmProjects/pysac/out/{self.name}.tex'
        test = 'Some cool latex contents.'
        self.content = HEADER + test + '\n'

    def append(self, subject):
        self.content += subject.resumen() + '\n'

    def save(self):
        self.content += FOOTER
        file = open(self.path, "w")
        file.write(self.content)
        file.close()
