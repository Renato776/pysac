LATEX_HEADER = '''Hello Latex World'''


class Doc:
    def __init__(self,name):
        self.name = name
        self.path = f'/home/renato/PycharmProjects/pysac/out/{self.name}.tex'
        self.content = LATEX_HEADER + '\n'

    def append(self,subject):
        self.content += subject.resumen() + '\n'

    def save(self):
        file = open(self.path, "w")
        file.write(self.content+'Some extra stuff')
        file.close()
