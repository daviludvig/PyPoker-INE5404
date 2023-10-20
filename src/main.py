from pote import Pote
from dealer import Dealer
from baralho import Baralho
from maleta import Maleta
from jogo import Jogo

d1 = Dealer("Dealer")
baralho = Baralho()
m1 = Maleta()
p1 = Pote()

jogo = Jogo(d1, m1, p1, baralho)

