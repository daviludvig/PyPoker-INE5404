from random import choice, randint, shuffle
import sys
from time import sleep
from jogador import Jogador
from bot import Bot
from visual import Visual
import os

class Jogo():
    def __init__(self, dealer, maleta, pote, baralho, mesa):
        self.apostas = []
        self.jogadores = []
        self.apostaram = []
        self.desistencias = []

        self.iniciar()
        self.selecao_inicial()
        self.gerar_bots()
        self.gerar_jogador()
        self.set_aposta_jogador()
        self.set_apostas_bots()
        self.set_fichas_jogadores(dealer, maleta)
        self.meio_rodada()
        self.organizar_lugares()
        # self.visual(dealer)
        self.primeira_rodada(dealer, pote, baralho, mesa)
        self.set_cartas_mesa(dealer, mesa, baralho)
        self.set_pontuacao_jogadores(mesa)
        self.tela_de_relatorio(mesa)
        self.loop(mesa)
        

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
        self.nome_do_jogador = input(">> Digite o seu nome: ").capitalize()
        self.jogador = Jogador(self.nome_do_jogador)
        self.jogadores.append(self.jogador)
    
    def gerar_bots(self):
        # Método que gera os bots
        for i in range(self.quantidade_jogadores - 1):
            self.jogadores.append(Bot(f"Bot {i+1}"))

    def set_aposta_jogador(self):
        # Método que define o valor apostado pelo jogador
        self.aposta_jogador = int(input(">> Digite o valor da sua aposta: "))
        while self.aposta_jogador < 200 or self.aposta_jogador > 2000 or self.aposta_jogador % 50 != 0:
            print(f"\nValor de aposta inválido. Tente novamente (200 < n < 2000) com um número múltiplo de 25.")
            self.aposta_jogador = int(input(">> Digite o valor da aposta: "))
        self.apostas.append(self.aposta_jogador)

    def set_apostas_bots(self):
        # Método que define as apostas dos bots
        for i in range(self.quantidade_jogadores - 1):
            aposta_bot = randint(self.aposta_jogador//2, self.aposta_jogador*2)
            while aposta_bot < 200 or aposta_bot > 2000 or aposta_bot % 25 != 0:
                aposta_bot = randint(self.aposta_jogador//2, self.aposta_jogador*2)
            self.apostas.append(aposta_bot)
    
    def set_fichas_jogadores(self, dealer, maleta):
        # Método que distribui 10 fichas para cada jogador
        for i in range((len(self.jogadores))):
            fichas = self.apostas[i] // 25
            for j in range(fichas):
                dealer.distribuir_ficha(maleta, self.jogadores[i].pilha)

    def set_cartas_inicias(self, dealer, baralho):
        # Método que distribui as cartas iniciais para cada jogador
        for i in range(len(self.jogadores)):
            for j in range(2):
                dealer.distribuir_primeiras_cartas(self.jogadores[i].rodada, baralho)

    def set_cartas_mesa(self, dealer, mesa, baralho):
        # Método que distribui as cartas da mesa
        dealer.distribuir_flop(mesa, baralho)

    def organizar_lugares(self):
        # Método que organiza os lugares dos jogadores
            shuffle(self.jogadores)
    
    def visual(self, dealer):
        # Método que imprime a disposição dos jogadores
        participantes = self.jogadores.copy()
        participantes.append(dealer)

        visual = Visual(participantes, self.nome_do_jogador)

    def meio_rodada(self):
        aux = input("\n>> Pressione ENTER quando estiver pronto para começar...")
        os.system('clear')

    def check(self, decisao, apostaram):
        # Método que realiza as apostas de uma rodada
        for jogador in self.jogadores:
            if jogador not in apostaram and decisao:
                jogador.cobrir()
                apostaram.append(jogador)

    def set_desistencias(self):
        # Método que remove um jogador da partida
        self.desistencias = []
        for jogador in self.jogadores:
            if jogador.desistiu:
                self.desistencias.append(jogador)
                # print(f"\n{self.desistencias[0].nome} desistiu da partida.")

    def set_pontuacao_jogadores(self, mesa):
        # Método que define a pontuação de cada jogador
        for jogador in self.jogadores:
            jogador.pontos.set_pontuacao(jogador, mesa)

    def tela_de_decisao(self):
        pass

    def decisao_rodada(self):
        aposta_vigente = 0
        for jogador in self.jogadores:
            if jogador.pilha._get_numero_fichas_apostadas() != 0:
                aposta_vigente = jogador.pilha._get_numero_fichas_apostadas()

        for jogador in self.jogadores:
            if jogador.nome == self.nome_do_jogador:
                self.mini_relatorio()
                while not jogador.realizou_jogada:
                    decisao = input("\n>> Digite 'c' para cobrir, 'a' para aumentar ou 'd' para desistir: ")
                    while decisao not in ['c', 'a', 'd']:
                        decisao = input("\n>> Digite 'c' para cobrir, 'a' para aumentar ou 'd' para desistir: ")
                    if decisao == 'c':
                        jogador.realizou_jogada = jogador.cobrir(aposta_vigente)
                    elif decisao == 'a':
                        jogador.realizou_jogada = jogador.aumentar(aposta_vigente)
                    elif decisao == 'd':
                        jogador.realizou_jogada = jogador.desistir()
            else:
                if not jogador.realizou_jogada:
                    jogador.decidir_jogada(aposta_vigente)
                    jogador.realizou_jogada = True

            if jogador.pilha._get_numero_fichas_apostadas() > aposta_vigente:
                aposta_vigente = jogador.pilha._get_numero_fichas_apostadas()
        self.set_desistencias()

    def mostrar_flop(self, mesa):
        # Método que imprime as cartas comunitárias
        print("\nFLOP:")
        for carta in mesa.get_flop():
            print(f"{carta}")

    def mini_relatorio(self):
        print(f"\n{'=+'*10}ASSISTENTE{'=+'*10}\n")
        for i in range(len(self.jogadores)-1):
            if self.jogadores[i+1].nome == self.nome_do_jogador or self.jogadores[i].nome == self.nome_do_jogador:
                continue
            maior_length = max(len(self.jogadores[i].nome), len(self.jogadores[i+1].nome))

        print(f"FICHAS{(7-maior_length)*' '}APOSTADAS  RESTANTES")
        for jogador in self.jogadores:
            if jogador.nome == self.nome_do_jogador:
                break
            else:
                if not jogador.desistiu:
                    print(f"{jogador}{(maior_length+2-len(jogador.nome))*' '}|{jogador.pilha._get_numero_fichas_apostadas():^9}  {jogador.pilha._get_numero_fichas():^9}")
        # for jogador in self.jogadores:
        #     if jogador.desistiu:
        #         print(f"{jogador}{(maior_length+2-len(jogador.nome))*' '}|{' '*8}FORA")
        for jogador in self.jogadores:
            if jogador.nome == self.nome_do_jogador:
                print(f"\nSUAS FICHAS:")
                print(f"{jogador}{(maior_length+2-len(jogador.nome))*' '}|{jogador.pilha._get_numero_fichas_apostadas():^9}  {jogador.pilha._get_numero_fichas():^9}")


    def tela_de_relatorio(self, mesa):
        # Método que imprime o relatório da rodada

        for i in range(len(self.jogadores)-1):
            maior_length = max(len(self.jogadores[i].nome), len(self.jogadores[i+1].nome))

        print(f"\n{'=+'*10}RELATÓRIO{'=+'*10}\n")
        print(f"FICHAS{(7-maior_length)*' '}APOSTADAS  RESTANTES")
        for jogador in self.jogadores:
            if not jogador.desistiu:
                print(f"{jogador}{(maior_length+2-len(jogador.nome))*' '}|{jogador.pilha._get_numero_fichas_apostadas():^9}  {jogador.pilha._get_numero_fichas():^9}")
        for jogador in self.jogadores:
            if jogador.desistiu:
                print(f"{jogador}{(maior_length+2-len(jogador.nome))*' '}|{' '*8}FORA")
        for jogador in self.jogadores:
            if jogador.nome == self.nome_do_jogador:
                print(f"\nSUAS CARTAS:")
                for carta in jogador.rodada.get_cartas():
                    print(f"{carta}")
        self.mostrar_flop(mesa)


    def primeira_rodada(self, dealer, pote, baralho, mesa):
        # Método que realiza a primeira rodada de apostas
        flag = False

        while True:
            for i in range(len(self.jogadores)):
                if self.jogadores[i].nome == self.nome_do_jogador:
                    if i < 2:
                        self.organizar_lugares()
                        break
                    else:
                        flag = True
                        break
            if flag:
                break


        self.jogadores[0].small_blind(pote)
        self.jogadores[1].big_blind(pote)
        self.apostaram.append(self.jogadores[0])
        self.apostaram.append(self.jogadores[1])

        if not flag:
            self.decisao_rodada()
        self.set_cartas_inicias(dealer, baralho)
    
    def loop(self, mesa):
        while True:
            self.meio_rodada()
            if len(self.desistencias) == len(self.jogadores) - 1:
                print(f"\n{self.desistencias[0].nome} venceu a partida!")
                break
            for jogador in self.jogadores:
                if jogador.desistiu:
                    continue
                else:
                    jogador.realizou_jogada = False
            self.decisao_rodada()
            self.tela_de_relatorio(mesa)
           

