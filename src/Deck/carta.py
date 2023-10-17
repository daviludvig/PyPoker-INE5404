class Carta():
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.naipe}"