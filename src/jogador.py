from mao import Mao
from stack import Pilha
from pontuacao import Pontuacao

class Jogador():
    def __init__(self, nome):
        self.nome = nome
        self.rodada = Mao()
        self.pilha = Pilha()
        self.pontos = Pontuacao()
        self.desistiu = False

    def limpa_mao(self):
        # Método que limpa a mão do jogador
        self.rodada._reset_mao()

    def small_blind(self, pote):
        # Método que aposta uma ficha
        ficha = self.pilha.fichas[0]
        self.pilha.fichas.pop()

        self.pilha.fichas_apostadas.append(ficha)
        pote.add_fichas(self.pilha.fichas_apostadas)

    def big_blind(self, pote):
        # Método que aposta duas fichas
        ficha1 = self.pilha.fichas[0]
        self.pilha.fichas.pop()

        ficha2 = self.pilha.fichas[0]
        self.pilha.fichas.pop()

        self.pilha.fichas_apostadas.append(ficha1)
        self.pilha.fichas_apostadas.append(ficha2)

        pote.add_fichas(self.pilha.fichas_apostadas)    

    def decidir_jogada(self, mesa):
        # Método que decide a jogada do jogador
        # Método sobrecarregado em Bot
        pass

    def __str__(self):
        return self.nome
    
    def cobrir(self, aposta_vigente):
        # Método que cobre a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < aposta_vigente:
            return False
        else:
            for i in range(aposta_vigente):
                self.rodada.apostar_ficha()
        return True
    
    def aumentar(self, aposta_vigente):
        # Método que aumenta a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < (aposta_vigente+1):
            return False
        else:
            for i in range(aposta_vigente+1):
                self.rodada.apostar_ficha()
        return True
    
    def desistir(self):
        # Método que remove um jogador da partida
        self.desistiu = True
        

    

