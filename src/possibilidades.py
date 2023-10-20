from math import ceil

class Possibilidades():
    def __init__(self, alvo, mesa):
        self.score = 0
        self.checagem = False
        self.cartas = alvo.rodada.get_cartas() + mesa.get_flop()

    def checar_possibilidades(self):
        # Metodo que seta o score do jogador
        pass

    def royal_flush(self):
        # Método que verifica se o jogador tem um royal flush
        naipes = []
        for carta in self.cartas:
            naipes.append(carta.get_naipe())
        aux = ["Paus", "Copas", "Espadas", "Ouro"]
        for naipe in aux:
            if naipes.count(naipe) >= 5:
                valores = []
                for carta in self.cartas:
                    if carta.get_naipe() == naipe:
                        valores.append(carta.get_valor())
                if "Ás" in valores and "Rei" in valores and "Dama" in valores and "Valete" in valores and "10" in valores:
                    self.score = 10
    
    def straigth_flush(self):
        # Método que verifica se o jogador tem um straigth flush
        naipes = []
        for carta in self.cartas:
            naipes.append(carta.get_naipe())
        aux = ["Paus", "Copas", "Espadas", "Ouro"]
        for naipe in aux:
            if naipes.count(naipe) >= 5:
                valores = []
                for carta in self.cartas:
                    if carta.get_naipe() == naipe:
                        valores.append(carta.get_valor())
                valores.sort()
                for i in range(len(valores)-4):
                    if sum(valores)/len(valores) == int(valores[ceil(len(valores)/2)]):
                        self.score = 9
    
    def quadra(self):
        # Método que verifica se o jogador tem uma quadra
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 4:
                self.score = 8
            
    def full_house(self):
        # Método que verifica se o jogador tem um full house
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 3:
                for valor2 in valores:
                    if valores.count(valor2) >= 2 and valor != valor2:
                        self.score = 7
            
    def flush(self):
        # Método que verifica se o jogador tem um flush
        naipes = []
        for carta in self.cartas:
            naipes.append(carta.get_naipe())
        aux = ["Paus", "Copas", "Espadas", "Ouro"]
        for naipe in aux:
            if naipes.count(naipe) >= 5:
                self.score = 6
            
    def straigth(self):
        # Método que verifica se o jogador tem um straigth
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        valores.sort()
        for i in range(len(valores)-4):
            if valores[i] == valores[i+1] - 1 and valores[i+1] == valores[i+2] - 1 and valores[i+2] == valores[i+3] - 1 and valores[i+3] == valores[i+4] - 1:
                self.score = 5

    def trinca(self):
        # Método que verifica se o jogador tem uma trinca
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 3:
                self.score = 4
            
    def dois_pares(self):
        # Metodo que verifica se o jogador tem dois pares
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 2:
                for valor2 in valores:
                    if valores.count(valor2) >= 2 and valor != valor2:
                        self.score = 3
    
    def um_par(self):
        # Método que verifica se o jogador tem um par
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 2:
                self.score = 2
    

    # Nunca vai chegar nesse método
    # def maior_carta(self):
    #     # Método que retorna a maior carta do jogador
    #     valores = []
    #     for carta in self.cartas:
    #         valores.append(carta.get_valor())
    #     valores.sort()
    #     self.score = 1