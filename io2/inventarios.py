from base import LATEX_HEADER


class Inventario:
    def __init__(self):
        self.someText = f'Hello imported text: {LATEX_HEADER}'

    def resumen(self):
        return 'I printed my own text {}.'.format(self.someText)
