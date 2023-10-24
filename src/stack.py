class Pilha:
    def __init__(self):
        self.fichas = []
        self.fichas_apostadas = []
    
    def _set_ficha(self, ficha):
        # Método que seta uma ficha para o jogador
        self.fichas.append(ficha)
    
    def _get_numero_fichas(self):
        # Método que retorna o número de fichas do jogador
        return len(self.fichas)

    def _get_numero_fichas_apostadas(self):
        # Método que retorna o número de fichas apostadas pelo jogador
        return len(self.fichas_apostadas)
    
    def apostar_ficha(self):
        # Método que aposta uma ficha
        ficha = self.fichas[0]
        self.fichas.pop()

        self.fichas_apostadas.append(ficha)