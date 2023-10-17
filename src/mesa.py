class Mesa():
    def __init__(self):
        self.cartas_comunitarias = []
        self.cartas_exibidas = []
        pass
    
    def _set_comunitarias(self, cartas):
        # Método que seta as cartas comunitárias
        self.cartas_comunitarias = self.cartas_comunitarias.extend(cartas)

    def get_comunitarias(self):
        # Método que retorna as cartas comunitárias
        return self.cartas_comunitarias

    def _set_comuni_exibidas(self, cartas):
        # Método que seta as cartas comunitárias exibidas
        self.exibidas = self.exibidas.extend(cartas)
