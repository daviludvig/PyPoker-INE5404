from jogador import Jogador
from dealer import Dealer
from baralho import Baralho
from maleta import Maleta
from jogo import Jogo

d1 = Dealer("Dealer")
baralho = Baralho()
j1 = Jogador("Jogador 1")
m1 = Maleta()

jogo = Jogo(d1, m1)
