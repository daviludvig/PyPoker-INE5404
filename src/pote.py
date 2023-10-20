class Pote:
    def __init__(self):
        self.fichas = []
    
    def add_fichas(self, fichas):
        # Método que adiciona fichas ao pote
        for ficha in fichas:
            self.fichas.append(ficha)