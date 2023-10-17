from carta import Carta
from random import shuffle as shuffle_cards, choice as choice_card


class Baralho(): 
    # Classe formada por objetos de Carta
    def __init__(self):
        naipes = ["Paus", "Copas", "Espadas", "Ouro"]
        valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

        self._set_baralho(naipes, valores)

    def _set_baralho(self, naipes, valores):
        # Método que cria um baralho com 52 cartas
        self.baralho = []

        for naipe in naipes:
            for valor in valores:

                if naipe == "Ouro" or naipe == "Copas":
                    cor = "Vermelho"
                else:
                    cor = "Preto"
                self.baralho.append(Carta(naipe, valor, cor))
    
    def get_baralho(self):
        # Método que retorna o baralho
        return self.baralho
    
    def embaralhar(self):
        # Método que embaralha o baralho
        shuffle_cards(self.baralho)

    # Método aplicado em dealer.py
    # def distribuir_primeiras_cartas(self):
    #     # Método que distribui cartas para os jogadores
    #     cartas_jogadores = []
    #     for i in range(2):
    #         cartas_jogadores.append(choice_card(self.baralho))
    #         self.baralho.remove(cartas_jogadores[i])
    #     return cartas_jogadores 