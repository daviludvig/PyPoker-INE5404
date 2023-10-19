from random import randint

class Ficha:
    def __init__(self):
        self.set_cor()

    def set_cor(self):
        if randint(0,9)%2 == 0:
            self.cor = "Vermelha"
        else:
            self.cor = "Preta"

    def __str__(self):
        return f"Ficha {self.cor}"
        
    def gerar_ficha(self):
        # Método que gera uma fichas
        return Ficha()