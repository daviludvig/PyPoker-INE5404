from math import ceil

class Pontuacao():
    def __init__(self):
        self.score = 0
        self.flag = False

    def set_cartas(self, alvo, mesa):
        self.cartas = alvo.rodada.get_cartas() + mesa.get_flop()

    def set_pontuacao(self, alvo, mesa):
        # Metodo que seta o score do jogador
        self.set_cartas(alvo, mesa)
        self.royal_flush()
        self.straigth_flush()
        self.quadra()
        self.full_house()
        self.flush()
        self.straigth()
        self.trinca()
        self.dois_pares()
        self.um_par()

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
                    if not self.flag:
                        self.score = 10
                        self.flag = True
    
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
                        if not self.flag:
                            self.score = 9
                            self.flag = True
        
    def quadra(self):
        # Método que verifica se o jogador tem uma quadra
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 4:
                self.score = 8
                self.flag = True
            
    def full_house(self):
        # Método que verifica se o jogador tem um full house
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 3:
                for valor2 in valores:
                    if valores.count(valor2) >= 2 and valor != valor2:
                        if not self.flag:
                            self.score = 7
                            self.flag = True
            
    def flush(self):
        # Método que verifica se o jogador tem um flush
        naipes = []
        for carta in self.cartas:
            naipes.append(carta.get_naipe())
        aux = ["Paus", "Copas", "Espadas", "Ouro"]
        for naipe in aux:
            if naipes.count(naipe) >= 5:
                if not self.flag:
                    self.score = 6
                    self.flag = True
            
    def straigth(self):
        # Método que verifica se o jogador tem um straigth
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        valores.sort()
        for i in range(len(valores)-4):
            if valores[i] == valores[i+1] - 1 and valores[i+1] == valores[i+2] - 1 and valores[i+2] == valores[i+3] - 1 and valores[i+3] == valores[i+4] - 1:
                if not self.flag:
                    self.score = 5
                    self.flag = True

    def trinca(self):
        # Método que verifica se o jogador tem uma trinca
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 3:
                if not self.flag:
                    self.score = 4
                    self.flag = True
                    break
            
    def dois_pares(self):
        # Metodo que verifica se o jogador tem dois pares
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 2:
                for valor2 in valores:
                    if valores.count(valor2) >= 2 and valor != valor2:
                        if not self.flag:
                            self.score = 3
                            self.flag = True
                            break
                break
    
    def um_par(self):
        # Método que verifica se o jogador tem um par
        valores = []
        for carta in self.cartas:
            valores.append(carta.get_valor())
        for valor in valores:
            if valores.count(valor) >= 2:
                if not self.flag:
                    self.score = 2
                    self.flag = True
                    break
    

    # Nunca vai chegar nesse método
    # def maior_carta(self):
    #     # Método que retorna a maior carta do jogador
    #     valores = []
    #     for carta in self.cartas:
    #         valores.append(carta.get_valor())
    #     valores.sort()
    #     self.score = 1