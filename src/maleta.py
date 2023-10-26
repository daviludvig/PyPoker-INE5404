from ficha import Ficha

class Maleta:
    def __init__(self):
        self.fichas = []
        self.preencher()

    def preencher(self):
        # Método que preenche a maleta com as fichas
        for i in range(800):
            self.fichas.append(Ficha().gerar_ficha())

    def get_fichas(self):
        # Método que retorna as fichas da maleta
        return self.fichas