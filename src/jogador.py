from mao import Mao
from pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.rodada = Mao()