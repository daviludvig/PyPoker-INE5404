from src.Deck.baralho import Baralho

class Rodada():
    def __init__(self, baralho, quantidade):
        self.cartasRodada = baralho.distribuir_cartas(quantidade)
        