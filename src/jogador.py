from rodada import Rodada
from pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def _set_cartas(self, cartas):
        # Método que seta as cartas do jogador
        self.cartas = cartas