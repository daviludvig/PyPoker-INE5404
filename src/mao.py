class Mao():
    def __init__(self):
       self.cartas = []
    
    def _set_carta(self, carta):
        # Método que seta as cartas do jogador
        self.cartas.append(carta)

    def get_cartas(self):
        # Método que retorna as cartas do jogador
        return self.cartas
    
    def _reset_mao(self):
        # Método que reseta a mão do jogador
        self.cartas = []
        