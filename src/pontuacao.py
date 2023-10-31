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

    def verificar_combinacao(self, valores, quantidades):
        for valor in valores:
            if valores.count(valor) >= quantidades:
                self.score = quantidades
                return True
        return False

    def royal_flush(self):
        # Método que verifica se o jogador tem um royal flush
        naipes = set([carta.get_naipe() for carta in self.cartas])
        if len(naipes) < 5:
            return
        valores = set([carta.get_valor() for carta in self.cartas])
        if "Ás" in valores and "Rei" in valores and "Dama" in valores and "Valete" in valores and "10" in valores:
            self.score = 10
            self.flag = True

    
    def straigth_flush(self):
        # Método que verifica se o jogador tem um straigth flush
        naipes = set([carta.get_naipe() for carta in self.cartas])
        if len(naipes) < 5:
            return False
        valores = set([carta.get_valor() for carta in self.cartas])
        valores = sorted(valores, key=lambda x: ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás"].index(x))
        for i in range(len(valores) - 4):
            if valores[i:i+5] == valores[i] + 5:
                if not self.flag:
                    self.score = 9
                    self.flag = True
        
    def quadra(self):
        # Método que verifica se o jogador tem uma quadra
        if not self.flag:
            self.score = 8
            self.flag = self.verificar_combinacao([carta.get_valor() for carta in self.cartas], 4)
            
    def full_house(self):
        # Método que verifica se o jogador tem um full house
        valores = [carta.get_valor() for carta in self.cartas]
        if self.verificar_combinacao(valores, 3):
            if self.verificar_combinacao(valores, 2):
                if not self.flag:
                    self.score = 7
                    self.flag = True
            
    def flush(self):
        # Método que verifica se o jogador tem um flush
        naipes = [carta.get_naipe() for carta in self.cartas]
        if not self.flag:
            self.flag = self.verificar_combinacao(naipes, 5)
            self.score = 6
            
    def straigth(self):
        # Método que verifica se o jogador tem um straigth
        valores = set([carta.get_valor() for carta in self.cartas])
        valores = sorted(valores, key=lambda x: ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás"].index(x))
        for i in range(len(valores) - 4):
            if valores[i:i+5] == valores[i] + 5:
                if not self.flag:
                    self.score = 5
                    self.flag = True


    def trinca(self):
        # Método que verifica se o jogador tem uma trinca
        if not self.flag:
            self.score = 4
            self.flag = self.verificar_combinacao([carta.get_valor() for carta in self.cartas], 3)
            
    def dois_pares(self):
        # Metodo que verifica se o jogador tem dois pares
        if not self.flag:
            valores = [carta.get_valor() for carta in self.cartas]
            if self.verificar_combinacao(valores, 2):
                if self.verificar_combinacao(valores, 2):
                    self.score = 3
                    self.flag = True
    
    def um_par(self):
        # Método que verifica se o jogador tem um par
        if not self.flag:
            self.flag = self.verificar_combinacao([carta.get_valor() for carta in self.cartas], 2)
            self.score = 2
    

    # Nunca vai chegar nesse método
    # def maior_carta(self):
    #     # Método que retorna a maior carta do jogador
    #     valores = []
    #     for carta in self.cartas:
    #         valores.append(carta.get_valor())
    #     valores.sort()
    #     self.score = 1