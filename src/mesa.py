class Mesa():
    def __init__(self):
        self.flop = []

    def _set_flop(self, carta):
        # Método que seta as cartas comunitárias
        self.flop.append(carta)

    def get_flop(self):
        # Método que retorna as cartas comunitárias
        return self.flop

    def set_lista_jogadores(self, jogadores):
        # Método que seta a lista de jogadores
        self.jogadores = jogadores
    
    def get_lista_jogadores(self):
        # Método que retorna a lista de jogadores
        return self.jogadores