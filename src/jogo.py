from random import choice, randint
from time import sleep
from math import floor
from baralho import Baralho

class Jogo():
    def __init__(self):
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


    def definir_dealer(self):
        # Método que define o dealer de acordo com as regras do texas hold'em
        baralho = Baralho()
        baralho.embaralhar()

        