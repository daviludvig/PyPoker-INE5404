from pessoa import Pessoa
from baralho import Baralho
from random import choice as choice_card

class Dealer(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def distribuir_primeiras_cartas(self, alvo, baralho):
        # Método que distribui as duas primeiras cartas para os jogadores
        cartas_jogadores = []
        for i in range(2):
            cartas_jogadores.append(choice_card(baralho.get_baralho()))
            baralho.get_baralho().remove(cartas_jogadores[i])
        alvo._set_cartas(cartas_jogadores)
    
    def distribuir_comunitarias(self, mesa, baralho):
        # Método que distribui as cartas comunitárias
        cartas_comunitarias = []
        for i in range(5):
            cartas_comunitarias.append(choice_card(baralho.get_baralho()))
            baralho.get_baralho().remove(cartas_comunitarias[i])
        mesa._set_comunitarias(cartas_comunitarias)
    
    
