class Carta():
    def __init__(self, naipe, valor, cor):
        self.naipe = naipe
        self.valor = valor
        self.cor = cor

    def __str__(self):
        return f"{self.valor} de {self.naipe} ({self.cor})"
    
    def get_valor(self):
        # Método que retorna o valor da carta
        if self.valor == "Ás":
            return 1
        elif self.valor == "Valete":
            return 11
        elif self.valor == "Dama":
            return 12
        elif self.valor == "Rei":
            return 13
        else:
            return int(self.valor)
        
    def get_naipe(self):
        # Método que retorna o naipe da carta
        return self.naipe
    