from jogador import Jogador
from random import randint

class Bot(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
    
    def decidir_jogada(self,aposta_vigente):
        # Método que decide a jogada do bot
        # Sobrecarga de método com a classe Jogador

        aleatorio = randint(0,9)
        # 1 - Cobrir
        if (aleatorio >= 6):
            self.cobrir(aposta_vigente)
        # 2 - Aumentar
        elif (5 >= aleatorio) and (aleatorio >= 3):
            self.aumentar(aposta_vigente)
        # 3 - Desistir
        else:
            self.desistir()
        

    def __str__(self):
        return self.nome
    
    def cobrir(self,aposta_vigente):
        # Método que cobre a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < aposta_vigente:
            self.decidir_jogada(aposta_vigente)
        else:
            for i in range(aposta_vigente - self.pilha._get_numero_fichas_apostadas()):
                self.pilha.apostar_ficha()

    def aumentar(self,aposta_vigente):
        # Método que aumenta a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < (aposta_vigente+1):
            self.decidir_jogada(aposta_vigente)
        else:
            self.cobrir(aposta_vigente)
            diferenca = self.pilha._get_numero_fichas() - (aposta_vigente - self.pilha._get_numero_fichas_apostadas())
            for i in range(randint(1, diferenca)):
                self.pilha.apostar_ficha()

    def desistir(self):
        self.desistiu = True
        pass