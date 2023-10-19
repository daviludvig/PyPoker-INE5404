from ficha import Ficha

class Maleta:
    def __init__(self):
        self.fichas = []
        self.preencher(10)

    # def gerar_ficha(self):
    #     # Método que gera as fichas
    #     return Ficha()

    def preencher(self, jogadores):
        # Método que preenche a maleta com as fichas
        for i in range(jogadores*10):
            self.fichas.append(Ficha().gerar_ficha())

    def get_fichas(self):
        # Método que retorna as fichas da maleta
        return self.fichas