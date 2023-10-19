from mao import Mao
from pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.rodada = Mao()
        self.fichas = []
    
    def limpa_mao(self):
        # Método que limpa a mão do jogador
        self.rodada._reset_mao()
