from random import choice, randint, shuffle
import sys
from time import sleep
from jogador import Jogador

class Jogo():
    def __init__(self, dealer, maleta, pote):
        self.apostas = []
        self.jogadores = []
        self.desistencias = []
        self.iniciar()
        self.selecao_inicial()
        self.gerar_bots()
        self.gerar_jogador()
        self.set_aposta_jogador()
        self.set_apostas_bots()
        self.set_fichas_jogadores(dealer, maleta)
        self.organizar_lugares()
        self.primeira_rodada(pote)

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

    def gerar_jogador(self):
        # Método que gera o jogador
        self.nome_do_jogador = input(">> Digite o seu nome: ")
        self.jogador = Jogador(self.nome_do_jogador)
        self.jogadores.append(self.jogador)
    
    def gerar_bots(self):
        # Método que gera os bots
        for i in range(self.quantidade_jogadores - 1):
            self.jogadores.append(Jogador(f"Bot {i+1}"))

    def set_aposta_jogador(self):
        # Método que define o valor apostado pelo jogador
        self.aposta_jogador = int(input(">> Digite o valor da sua aposta: "))
        while self.aposta_jogador < 200 or self.aposta_jogador > 2000 or self.aposta_jogador % 50 != 0:
            print(f"\nValor de aposta inválido. Tente novamente (200 < n < 2000) com um número múltiplo de 50.")
            self.aposta_jogador = int(input(">> Digite o valor da aposta: "))
        self.apostas.append(self.aposta_jogador)

    def set_apostas_bots(self):
        # Método que define as apostas dos bots
        for i in range(self.quantidade_jogadores - 1):
            aposta_bot = randint(self.aposta_jogador//2, self.aposta_jogador*2)
            while aposta_bot < 200 or aposta_bot > 2000 or aposta_bot % 50 != 0:
                aposta_bot = randint(self.aposta_jogador//2, self.aposta_jogador*2)
            self.apostas.append(aposta_bot)
    
    def set_fichas_jogadores(self, dealer, maleta):
        # Método que distribui 10 fichas para cada jogador
        for i in range((len(self.jogadores)-1)):
            fichas = self.apostas[i] // 50
            for j in range(fichas):
                dealer.distribuir_ficha(maleta, self.jogadores[i].pilha)

    def set_cartas_inicias(self, dealer):
        # Método que distribui as cartas iniciais para cada jogador
        for i in range(len(self.jogadores)):
            for j in range(2):
                dealer.distribuir_carta(self.jogadores[i].mao)

    def organizar_lugares(self):
        # Método que organiza os lugares dos jogadores
            shuffle(self.jogadores)
    
    def desistir(self, jogador):
        # Método que remove um jogador da partida
        self.desistencias.append(jogador)

    def tela_de_decisao(self):
        pass

    def tela_de_relatorio_fichas(self):
        # Método que imprime o relatório da rodada

        for i in range(len(self.jogadores)-1):
            maior_length = max(len(self.jogadores[i].nome), len(self.jogadores[i+1].nome))

        print(maior_length, type(maior_length))
        print(f"\n{'=+'*10}RELATÓRIO DE FICHAS{'=+'*10}\n")
        print(f"{(maior_length+2)*' '}APOSTADAS  RESTANTES")
        for jogador in self.jogadores:
            print(f"{jogador}{(len(jogador.nome)-maior_length+1)*' '}|{jogador.pilha._get_numero_fichas_apostadas():^9}  {jogador.pilha._get_numero_fichas():^9}")

        # for jogador in self.jogadores:
        #     if not jogador.nome == self.nome_do_jogador:
        #         if jogador.nome in self.desistencias:
        #             print(f"{jogador.nome}: FORA.")
        #         else:
        #             print(f"{jogador.nome}: {jogador.pilha._get_numero_fichas_apostadas()} fichas apostadas ({jogador.pilha._get_numero_fichas()} restantes).")

    def primeira_rodada(self, pote):
        # Método que realiza a primeira rodada de apostas

        aux = input("\n>> Pressione ENTER quando estiver pronto para começar...")
        print(f"\n{'=+'*10}PRIMEIRA RODADA{'=+'*10}\n")
        flag = False
        for i in range(len(self.jogadores)):
            if self.jogadores[i].nome == self.nome_do_jogador:
                if i < 2:
                    flag = True
                    print(f"-> Nesta rodada você apostou.")
                    break
                else:
                    jogador_index = i
                    break

        if not flag:
            self.jogadores[0].small_blind(pote)
            self.jogadores[1].big_blind(pote)
            self.tela_de_relatorio_fichas()

        

