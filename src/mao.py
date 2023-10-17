from baralho import Baralho

class Mao():
    def __init__(self, baralho, quantidade):
       self.cartas = []
    
    def _set_cartas(self, cartas):
        # Método que seta as cartas do jogador
        self.cartas = self.cartas.extend(cartas)

    def get_cartas(self):
        # Método que retorna as cartas do jogador
        return self.cartas