from pote import Pote
from dealer import Dealer
from baralho import Baralho
from maleta import Maleta
from jogo import Jogo
from mesa import Mesa

d1 = Dealer("Dealer")
baralho = Baralho()
baralho.embaralhar()
m1 = Maleta()
p1 = Pote()
mesa = Mesa()

jogo = Jogo(d1, m1, p1, baralho, mesa)

