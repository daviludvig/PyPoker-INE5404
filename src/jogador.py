from rodada import Rodada

class Jogador():
    def __init__(self, nome, baralho, quantidade_cartas):
        self.nome = nome

        rodadaAtual = Rodada(baralho, quantidade_cartas)

        self.cartas = rodadaAtual.get_cartas_rodada()