class Pote:
    def __init__(self):
        self.fichas = []
    
    def add_fichas(self, ficha):
        # Método que adiciona fichas ao pote
        self.fichas.append(ficha)

    def get_numero_fichas(self):
        # Método que retorna o número de fichas do pote
        return len(self.fichas)