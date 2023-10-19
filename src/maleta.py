from ficha import Ficha

class Maleta:
    def __init__(self):
        self.fichas = []

    def gerar_ficha(self, valor):
        # Método que gera as fichas
        return Ficha(valor)

    def preencher(self):
        # Método que preenche a maleta com as fichas
        for valor in [1, 5, 10, 25, 50, 100, 500]:
            for i in range(10):
                self.fichas.append(self.gerar_ficha(valor))

    def get_fichas(self):
        # Método que retorna as fichas da maleta
        return self.fichas