from jogador import Jogador
from dealer import Dealer
from baralho import Baralho

d1 = Dealer("Dealer")
baralho = Baralho()
j1 = Jogador("Jogador 1")

d1.distribuir_primeiras_cartas(j1.rodada, baralho)

