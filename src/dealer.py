from pessoa import Pessoa
from baralho import Baralho

class Dealer(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def distribuir_primeiras_cartas(self, alvo, baralho):
        # Método que distribui as duas primeiras cartas para os jogadores
        cartas_jogadores = []
        for i in range(2):
            cartas_jogadores.append(baralho.get_carta())
        alvo._set_cartas(cartas_jogadores)
    
