from random import choice, randint
from time import sleep

class Jogo():
    def __init__(self):
        self.iniciar()
        self.selecao_inicial()
        pass

    def iniciar(self):
        # Método que imprime a mensagem de início do jogo
        temporizacao_dinamica = [randint(1,6) / 100 for i in range(100)]
        with open("/Users/daviludvig/Documents/UFSC/23.2/Python/10-17/Poker/docs/mensagem_inicio.txt", "r") as arquivo:
            for letra in arquivo.read():
                tempo = choice(temporizacao_dinamica)
                print(letra, end="", flush=True)
                sleep(tempo)
            print()
        pass
    

    def selecao_inicial(self):
        
        pass


j1 = Jogo()