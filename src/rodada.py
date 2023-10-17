import sys
from Deck.baralho import Baralho
sys.path(0, "../Deck")

class Rodada():
    def __init__(self, baralho, quantidade):
       self.setCartasRodada(baralho, quantidade) 

    def setCartasRodada(self, baralho, quantidade):
        # Método que distribui cartas para os jogadores
        self.cartasRodada = baralho.distribuir_cartas(quantidade)

    def getCartasRodada(self):
        # Método que retorna as cartas da mão do jogador nesta rodada
        return self.cartasRodada
