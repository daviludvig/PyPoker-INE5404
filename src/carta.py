class Carta():
    def __init__(self, naipe, valor, cor):
        self.naipe = naipe
        self.valor = valor
        self.cor = cor

    def __str__(self):
        return f"{self.valor} de {self.naipe} ({self.cor})"