from random import choice, randint
from time import sleep
from maleta import Maleta

class Jogo():
    def __init__(self):
        self.apostas = []
        self.iniciar()
        self.selecao_inicial()
        pass

    def iniciar(self):
        # Método que imprime a mensagem de início do jogo
        temporizacao_dinamica = [randint(1,4) / 100 for i in range(100)]
        with open("/Users/daviludvig/Documents/UFSC/23.2/Python/10-17/Poker/docs/mensagem_inicio.txt", "r") as arquivo:
            for letra in arquivo.read():
                tempo = choice(temporizacao_dinamica)
                print(letra, end="", flush=True)
                #sleep(tempo)
            print()
        pass
    
    def selecao_inicial(self):
        # Método que imprime a mensagem de seleção inicial e pede entradas do usuário
        print(f"\n{'=+'*20}")

        print(f"\nAntes de comecar a jogar, o usuário\ndeve definir o número de jogadores.\n")
        self.quantidade_jogadores = int(input(">> Digite o número de jogadores (2 - 10): "))

        while (self.quantidade_jogadores < 2) or (self.quantidade_jogadores > 10):
            print("\nNúmero de jogadores inválido. Tente novamente.")
            self.quantidade_jogadores = int(input(">> Digite o número de jogadores (2 - 10): "))

    def set_aposta_jogador(self):
        # Método que define o valor apostado pelo jogador
        self.aposta_jogador = int(input(">> Digite o valor da sua aposta: "))
        while self.aposta_jogador < 200 or self.aposta_jogador > 2000:
            print("Valor de aposta inválido. Tente novamente (200 < n < 2000).")
            self.aposta_jogador = int(input(">> Digite o valor da aposta: "))
        self.apostas.append(self.aposta_jogador)

    def set_apostas_bots(self):
        # Método que define as apostas dos bots
        for i in range(self.quantidade_jogadores - 1):
            aposta_bot = randint(200, 2000)
            while aposta_bot < 200 or aposta_bot > 2000:
                aposta_bot = randint(200, 2000)
            self.apostas.append(aposta_bot)

    def set_maleta(self):
        # Método que define as fichas
        self.fichas = Maleta().preencher(self.quantidade_jogadores)
        
    def set_fichas(self, dealer, jogadores):
        # Método que distribui 10 fichas para cada jogador
        for jogador in jogadores:
            continue
