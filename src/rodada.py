from baralho import Baralho

class Rodada():
    def __init__(self, baralho, quantidade):
       self.set_cartas_rodada(baralho, quantidade) 

    def set_cartas_rodada(self, baralho, quantidade):
        # Método que distribui cartas para os jogadores
        self.rodada = baralho.distribuir_primeiras_cartas()

    def get_cartas_rodada(self):
        # Método que retorna as cartas da mão do jogador nesta rodada
        return self.rodada
