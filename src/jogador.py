from mao import Mao
from pessoa import Pessoa
from stack import Pilha

class Jogador(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.rodada = Mao()
        self.pilha = Pilha()

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

    def decidir_jogada(self):
        # Método que decide a jogada do jogador
        pass

    def __str__(self):
        return self.nome
    
    def cobrir(self):
        # Método que cobre a aposta vigente
        pass


