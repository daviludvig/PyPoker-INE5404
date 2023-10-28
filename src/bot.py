from jogador import Jogador
from random import randint

class Bot(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
    
    def decidir_jogada(self,aposta_vigente, pote):
        # Método que decide a jogada do bot
        # Sobrecarga de método com a classe Jogador

        aleatorio = randint(0,9)
        # 1 - Cobrir
        if (aleatorio >= 4):
            self.cobrir(aposta_vigente, pote)
        # 2 - Aumentar
        elif (3 >= aleatorio) and (aleatorio >= 1):
            self.aumentar(aposta_vigente, pote)
        # 3 - Desistir
        else:
            self.desistir()
        

    def __str__(self):
        return self.nome
    
    def cobrir(self, aposta_vigente, pote):
        if aposta_vigente - self.pilha._get_numero_fichas_apostadas() > self.pilha._get_numero_fichas():
            for i in range(self.pilha._get_numero_fichas()):
                self.pilha.apostar_ficha(pote)
        else:
            for i in range(aposta_vigente - self.pilha._get_numero_fichas_apostadas()):
                self.pilha.apostar_ficha(pote)
        

    def aumentar(self,aposta_vigente,pote):
        # Método que aumenta a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < (aposta_vigente+1):
            self.decidir_jogada(aposta_vigente, pote)
        else:
            self.cobrir(aposta_vigente, pote)
            diferenca = self.pilha._get_numero_fichas() - (aposta_vigente - self.pilha._get_numero_fichas_apostadas())
            diferenca = diferenca//2
            for i in range(randint(1, diferenca)):
                if self.pilha._get_numero_fichas == 0:
                    break
                self.pilha.apostar_ficha(pote)

    def desistir(self):
        self.desistiu = True
        pass