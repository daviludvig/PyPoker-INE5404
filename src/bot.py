from jogador import Jogador
from random import randint

class Bot(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
    
    def decidir_jogada(self, mesa, aposta_vigente):
        # Método que decide a jogada do bot
        # Sobrecarga de método com a classe Jogador

        aleatorio = randint(0,9)

        # 1 - Cobrir
        if (9 <= aleatorio <= 7):
            return 1
        # 2 - Aumentar
        if (6 <= aleatorio <= 3):
            return 2
        # 3 - Desistir
        if (2 <= aleatorio <= 1):
            return 3
        

    def __str__(self):
        return self.nome
    
    def cobrir(self, aposta_vigente):
        pass

    def aumentar(self, aposta_vigente):
        # Método que aumenta a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < (aposta_vigente+1):
            return False
        else:
            for i in range(aposta_vigente+1):
                self.rodada.apostar_ficha()
        

    def desistir(self):
        self.desistiu = True
        pass