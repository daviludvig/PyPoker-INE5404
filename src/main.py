from jogador import Jogador
from dealer import Dealer
from baralho import Baralho
from maleta import Maleta

d1 = Dealer("Dealer")
baralho = Baralho()
j1 = Jogador("Jogador 1")
m1 = Maleta()

d1.distribuir_primeiras_cartas(j1.rodada, baralho)
print(len(j1.pilha.fichas))
d1.distribuir_ficha(m1, j1.pilha)

print(len(j1.pilha.fichas))