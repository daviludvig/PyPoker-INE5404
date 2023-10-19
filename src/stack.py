class Pilha:
    def __init__(self):
        self.fichas = []
    
    def _set_ficha(self, ficha):
        # Método que seta uma ficha para o jogador
        self.fichas.append(ficha)
    
    def __str__(self):
        