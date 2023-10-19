class Ficha:
    def __init__(self, valor):
        self.valor = valor
        self.set_cor()

    def set_cor(self):
        if self.valor == 1:
            self.cor = "branca"
        elif self.valor == 5:
            self.cor = "vermelha"
        elif self.valor == 10:
            self.cor = "azul"
        elif self.valor == 50:
            self.cor = "verde"
        elif self.valor == 100:
            self.cor = "preta"
        else:
            self.cor = "laranja"

    def __str__(self):
        return f"Ficha de {self.valor} ({self.cor})"
        