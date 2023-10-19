class Mesa():
    def __init__(self):
        self.cartas_comunitarias = []
        self.cartas_exibidas = []
    
    def _set_comunitaria(self, carta):
        # Método que seta as cartas comunitárias
        self.cartas_comunitarias.append(carta)

    def get_comunitarias(self):
        # Método que retorna as cartas comunitárias
        return self.cartas_comunitarias

    def _set_exibir_comunitaria(self, carta):
        # Método que seta as cartas comunitárias exibidas
        self.cartas_exibidas.append(carta)

    def set_lista_jogadores(self, jogadores):
        # Método que seta a lista de jogadores
        self.jogadores = jogadores
    
    def get_lista_jogadores(self):
        # Método que retorna a lista de jogadores
        return self.jogadores