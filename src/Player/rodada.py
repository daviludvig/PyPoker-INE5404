from src.Deck.baralho import Baralho

class Rodada():
    def __init__(self, baralho, quantidade):
       self.setCartasRodada(baralho, quantidade) 

    def setCartasRodada(self, baralho, quantidade):
        self.cartasRodada = baralho.distribuir_cartas(quantidade)

    def getCartasRodada(self):
        return self.cartasRodada
        