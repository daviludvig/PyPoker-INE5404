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
    
    def apostar_ficha(self, pote):
        # Método que aposta uma ficha
        ficha = self.fichas[0]
        pote.add_fichas(ficha)
        self.fichas.pop()

        self.fichas_apostadas.append(ficha)

    def get_todas_fichas(self):
        # Método que retorna todas as fichas do jogador
        todas = len(self.fichas) + len(self.fichas_apostadas)
        return todas
    
    def get_diferenca_fichas(self):
        # Método que retorna a diferença entre as fichas do jogador
        diferenca = len(self.fichas) - len(self.fichas_apostadas)
        return diferenca