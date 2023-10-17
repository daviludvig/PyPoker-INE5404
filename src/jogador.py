from rodada import Rodada

class Jogador():
    def __init__(self, nome, baralho, quantidade):
        self.nome = nome

        rodadaAtual = Rodada(baralho, quantidade)

        self.cartas = rodadaAtual.get_cartas_rodada()