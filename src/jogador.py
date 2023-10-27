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
        self.realizou_jogada = False

    def limpa_mao(self):
        # Método que limpa a mão do jogador
        self.rodada._reset_mao()

    def small_blind(self, pote):
        # Método que aposta uma ficha
        self.pilha.apostar_ficha(pote)
        self.realizou_jogada = True

    def big_blind(self, pote):
        # Método que aposta duas fichas
        for i in range(2):
            self.pilha.apostar_ficha(pote)
        self.realizou_jogada = True  

    def decidir_jogada(self, mesa):
        # Método que decide a jogada do jogador
        # Método sobrecarregado em Bot
        pass

    def __str__(self):
        return self.nome
    
    def cobrir(self, aposta_vigente, pote):
        # Método que cobre a aposta vigente
        # if len(self.pilha.fichas) == 0: #or len(self.pilha.fichas) < aposta_vigente:
        #     return False
        # else:
        for i in range(aposta_vigente - self.pilha._get_numero_fichas_apostadas()):
            if self.pilha._get_numero_fichas == 0:
                break
            self.pilha.apostar_ficha(pote)
        return True
    
    def aumentar(self, aposta_vigente, pote):
        # Método que aumenta a aposta vigente
        if len(self.pilha.fichas) == 0 or len(self.pilha.fichas) < (aposta_vigente+1 - self.pilha._get_numero_fichas_apostadas()):
            return False
        else:
            aumento = int(input(f">> Digite o valor do aumento (1 / {self.pilha._get_numero_fichas() - (aposta_vigente - self.pilha._get_numero_fichas_apostadas())}): "))
            while aumento < 1 or (aumento > self.pilha._get_numero_fichas() - (aposta_vigente - self.pilha._get_numero_fichas_apostadas())):
                aumento = int(input(f">> Digite o valor do aumento (1 / {self.pilha._get_numero_fichas() - (aposta_vigente - self.pilha._get_numero_fichas_apostadas())}): "))

            for i in range(aposta_vigente+aumento):
                if self.pilha._get_numero_fichas == 0:
                    break
                self.pilha.apostar_ficha(pote)
        return True
    
    def desistir(self):
        # Método que remove um jogador da partida
        self.desistiu = True
        return True
        

    

