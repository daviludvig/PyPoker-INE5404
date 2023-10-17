from jogador import Jogador
from baralho import Baralho

baralho = Baralho()

j1 = Jogador("Jogador 1", baralho, 5)

for i in j1.cartas:
    print(i)
