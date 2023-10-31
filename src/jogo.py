from random import choice, randint, shuffle
from time import sleep
from jogador import Jogador
from bot import Bot
from visual import Visual
import os
from random import choice


class Jogo:
    def __init__(self, dealer, maleta, pote, baralho, mesa):
        self.apostas = []
        self.jogadores = []
        self.apostaram = []
        self.desistencias = []

        os.system("clear")
        self.iniciar()
        self.selecao_inicial()
        self.gerar_bots()
        self.gerar_jogador()
        self.set_aposta_jogador()
        self.set_apostas_bots()
        self.set_fichas_jogadores(dealer, maleta)
        self.meio_rodada()
        self.organizar_lugares()
        self.primeira_rodada(dealer, pote, baralho, mesa)
        self.set_cartas_mesa(dealer, mesa, baralho)
        self.loop(mesa, baralho, dealer, pote)

    def iniciar(self):
        # Método que imprime a mensagem de início do jogo
        temporizacao_dinamica = [randint(1, 4) / 100 for i in range(100)]
        with open(
            "/Users/daviludvig/Documents/UFSC/23.2/Python/10-17/Poker/docs/mensagem_inicio.txt",
            "r",
        ) as arquivo:
            for letra in arquivo.read():
                tempo = choice(temporizacao_dinamica)
                print(letra, end="", flush=True)
                sleep(tempo)
            print()
        pass

    def selecao_inicial(self):
        # Método que imprime a mensagem de seleção inicial e pede entradas do usuário
        print(f"\n{'=+'*20}")

        print(
            f"\nAntes de comecar a jogar, o usuário\ndeve definir o número de jogadores.\n"
        )
        self.quantidade_jogadores = int(
            input(">> Digite o número de jogadores (2 - 10): ")
        )

        while (self.quantidade_jogadores < 2) or (self.quantidade_jogadores > 10):
            print("\nNúmero de jogadores inválido. Tente novamente.")
            self.quantidade_jogadores = int(
                input(">> Digite o número de jogadores (2 - 10): ")
            )

    def gerar_jogador(self):
        # Método que gera o jogador
        self.nome_do_jogador = input(">> Digite o seu nome: ").capitalize()
        self.nome_do_jogador = "* " + self.nome_do_jogador
        self.jogador = Jogador(self.nome_do_jogador)
        self.jogadores.append(self.jogador)

    def gerar_bots(self):
        # Método que gera os bots
        with open("/Users/daviludvig/Documents/UFSC/23.2/Python/10-17/Poker/docs/nomes_bots.txt","r") as file:
            temp = file.read()
            temp = temp.split(", ")
            file.close()
        for i in range(self.quantidade_jogadores - 1):
            nome = choice(temp)
            temp.remove(nome)
            self.jogadores.append(Bot(f"{nome}"))

    def set_aposta_jogador(self):
        # Método que define o valor apostado pelo jogador
        self.aposta_jogador = int(input(">> Digite o valor da sua aposta: "))
        while (
            self.aposta_jogador < 200
            or self.aposta_jogador > 2000
            or self.aposta_jogador % 50 != 0
        ):
            print(
                f"\nValor de aposta inválido. Tente novamente (200 < n < 2000) com um número múltiplo de 25."
            )
            self.aposta_jogador = int(input(">> Digite o valor da aposta: "))
        self.apostas.append(self.aposta_jogador)

    def set_apostas_bots(self):
        # Método que define as apostas dos bots
        for i in range(self.quantidade_jogadores - 1):
            aposta_bot = randint(self.aposta_jogador // 2, self.aposta_jogador * 2)
            while aposta_bot < 200 or aposta_bot > 2000 or aposta_bot % 25 != 0:
                aposta_bot = randint(self.aposta_jogador // 2, self.aposta_jogador * 2)
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

    def aumentar_flop(self, dealer, mesa, baralho):
        # Método que aumenta o flop
        dealer.aumentar_flop(mesa, baralho)

    def visual(self, dealer):
        # Método que imprime a disposição dos jogadores
        participantes = self.jogadores.copy()
        participantes.append(dealer)

        visual = Visual(participantes, self.nome_do_jogador)

    def meio_rodada(self):
        aux = input("\n>> Pressione ENTER quando estiver pronto para começar...")
        os.system("clear")

    def mostrar_pote(self, pote):
        # Método que imprime o pote
        print(f"\nPOTE: {pote.get_pote()} = R${pote.get_pote()*25}.00")

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

    def set_pontuacao_jogadores(self, mesa):
        # Método que define a pontuação de cada jogador
        for jogador in self.jogadores:
            jogador.pontos.set_pontuacao(jogador, mesa)

    def tela_de_decisao(self):
        pass

    def decisao_rodada(self, mesa, pote, mostrarFlop = False):
        aposta_vigente = 0
        for jogador in self.jogadores:
            if jogador.pilha._get_numero_fichas_apostadas() != 0:
                aposta_vigente = jogador.pilha._get_numero_fichas_apostadas()

        for jogador in self.jogadores:
            if jogador.nome == self.nome_do_jogador:
                self.tela_de_relatorio(mesa, pote, mostrarFlop = mostrarFlop)
                while not jogador.realizou_jogada:
                    decisao = input(
                        "\n>> Digite 'c' para cobrir, 'a' para aumentar ou 'd' para desistir: "
                    )
                    while decisao not in ["c", "a", "d"]:
                        decisao = input(
                            "\n>> Digite 'c' para cobrir, 'a' para aumentar ou 'd' para desistir: "
                        )
                    if decisao == "c":
                        jogador.realizou_jogada = jogador.cobrir(aposta_vigente, pote)
                    elif decisao == "a":
                        jogador.realizou_jogada = jogador.aumentar(aposta_vigente, pote)
                    elif decisao == "d":
                        jogador.realizou_jogada = jogador.desistir()
            else:
                if not jogador.realizou_jogada:
                    jogador.decidir_jogada(aposta_vigente, pote)
                    jogador.realizou_jogada = True

            if jogador.pilha._get_numero_fichas_apostadas() > aposta_vigente:
                aposta_vigente = jogador.pilha._get_numero_fichas_apostadas()
        self.set_desistencias()

    def mostrar_flop(self, mesa):
        # Método que imprime as cartas comunitárias
        print("\nFLOP:")
        for carta in mesa.get_flop():
            print(f"{carta}")

    def tela_de_relatorio(self, mesa, pote, mostrarFlop = False):
        # Método que imprime o relatório da rodada
        aposta_vigente = 0
        for jogador in self.jogadores:
            if jogador.pilha._get_numero_fichas_apostadas() > aposta_vigente:
                aposta_vigente = jogador.pilha._get_numero_fichas_apostadas()

        for i in range(len(self.jogadores) - 1):
            maior_length = max(
                len(self.jogadores[i].nome), len(self.jogadores[i + 1].nome)
            )
        maior_length += 1
        print(f"\n{'=+'*10}RELATÓRIO{'=+'*10}\n")
        print(f"{abs(((maior_length+3-6)//2))*' '}FICHAS{abs(((maior_length+3-6)//2))*' '}APOSTADAS  RESTANTES")
        for jogador in self.jogadores:
            if not jogador.desistiu:
                print(
                    f"{jogador}{abs((maior_length+1-len(jogador.nome)))*' '}|{jogador.pilha._get_numero_fichas_apostadas():^9}  {jogador.pilha._get_numero_fichas():^9}"
                )
        for jogador in self.jogadores:
            if jogador.desistiu:
                print(f"{jogador}{abs((maior_length+1-len(jogador.nome)))*' '}|{' '*8}FORA")
        self.mostrar_pote(pote)
        print(f"Aposta vigente: {aposta_vigente}")
        for jogador in self.jogadores:
            if jogador.nome == self.nome_do_jogador:
                print(f"\nSUAS CARTAS:")
                for carta in jogador.rodada.get_cartas():
                    print(f"{carta}")
        if mostrarFlop:
            self.mostrar_flop(mesa)

    def desempate(self, melhores, mesa):
        # Metodo que define vencedor(es) por maior carta
        melhores_melhor = []
        max = 0
        for jogador in melhores:
            cartas_alvo = jogador.rodada.get_cartas() + mesa.get_flop()
            for carta in cartas_alvo:
                if carta.get_valor() > max:
                    max = carta.get_valor()
                    melhores_melhor = [jogador]
                elif carta.get_valor() == max and jogador not in melhores_melhor:
                    melhores_melhor.append(jogador)
        return melhores_melhor

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
                self.visual(dealer)
                break
        
        self.jogadores[0].small_blind(pote)
        self.jogadores[1].big_blind(pote)
        self.apostaram.append(self.jogadores[0])
        self.apostaram.append(self.jogadores[1])

        self.set_cartas_inicias(dealer, baralho)
        self.tela_de_relatorio(mesa, pote)

    def loop(self, mesa, baralho, dealer, pote):
        contador = 0
        while True:
            if len(self.desistencias) == len(self.jogadores) - 1:
                for jogador in self.jogadores:
                    if not jogador.desistiu:
                        print(f"\n{jogador.nome} venceu a partida sem mostrar as cartas!")
                        break
                break
            if contador == 0:
                self.meio_rodada()
                self.decisao_rodada(mesa, pote)
                os.system("clear")
                self.tela_de_relatorio(mesa, pote)
                self.meio_rodada()
                self.reiniciar()
                self.decisao_rodada(mesa, pote)
                os.system("clear")
                self.tela_de_relatorio(mesa, pote)
                self.meio_rodada()
                self.reiniciar()

            elif contador <= 3:
                self.decisao_rodada(mesa, pote, mostrarFlop = True)
                os.system("clear")
                self.tela_de_relatorio(mesa, pote, mostrarFlop=True)
                self.meio_rodada()
                if contador != 3:   
                    self.aumentar_flop(dealer, mesa, baralho)

                self.reiniciar()
            else:
                self.mostrar_todas_cartas(mesa, pote)
                self.meio_rodada()
                self.set_pontuacao_jogadores(mesa)
                print()
                melhores = []
                melhores2 = []
                max = 0
                for i in range(len(self.jogadores)):
                    if not self.jogadores[i].desistiu:
                        if self.jogadores[i].pontos.score == max:
                            max = self.jogadores[i].pontos.score
                            melhores.append(self.jogadores[i])
                        elif self.jogadores[i].pontos.score > max:
                            max = self.jogadores[i].pontos.score
                            melhores = []
                            melhores.append(self.jogadores[i])
                if len(melhores) == 1:
                    print(f"{'=+'*10}VENCEDOR{'=+'*10}\n")
                    print(f"{melhores[0].nome} venceu a partida e levou {pote.get_pote()} fichas.")
                else:
                    melhores2 = self.desempate(melhores, mesa)
                    if len(melhores2) == 1:
                        print(f"{'=+'*10}VENCEDOR{'=+'*10}\n")
                        print(f"{melhores2[0].nome} venceu a partida e levou {pote.get_pote()} fichas.")
                    else:
                        print(f"{'=+'*10}VENCEDORES{'=+'*10}\n")
                        for jogador in melhores2:
                            print(f"{jogador.nome} levou {pote.get_pote()//len(melhores2)} fichas.")
                self.registrar(melhores, mesa, melhores2)
                break
            contador += 1

    def reiniciar(self):
        for jogador in self.jogadores:
            if not jogador.desistiu:
                jogador.realizou_jogada = False

    def mostrar_todas_cartas(self, mesa, pote):
        print(f"{'=+'*10}CARTAS{'=+'*10}\n")
        self.mostrar_pote(pote)
        print()
        jogadores_ativos = [jogador for jogador in self.jogadores if not jogador.desistiu]


        if len(jogadores_ativos) % 2 != 0:
            aux = len(jogadores_ativos) -1
        else:
            aux = len(jogadores_ativos)

        for i in range(0, aux, 2):
            if not jogadores_ativos[i].desistiu and not jogadores_ativos[i+1].desistiu:
                tamanho = len(jogadores_ativos[i].nome)
                print(f"{jogadores_ativos[i].nome}: {(25 - tamanho)*' '} {jogadores_ativos[i+1].nome}: ")
                for j in range(2):
                    print(f"{jogadores_ativos[i].rodada.get_cartas()[j]} {(26-len(str(jogadores_ativos[i].rodada.get_cartas()[j])))*' '} {jogadores_ativos[i+1].rodada.get_cartas()[j]}")
                print()
        if len(jogadores_ativos) % 2 != 0 and not jogadores_ativos[-1].desistiu:
            print(f"{jogadores_ativos[-1].nome}: ")
            for carta in jogadores_ativos[-1].rodada.get_cartas():
                print(f"{carta}")
            print()
        print("FLOP:")
        for carta in mesa.get_flop():
            print(f"{carta}")

    def registrar(self, vencedores, mesa, melhores2):
        # Método que registra os vencedores da partida
        melhores_maos = ["Par", "Dois pares", "Trinca", "Straight", "Flush", "Full house", "Quadra", "Straight flush", "Royal flush"]
        
        with open("/Users/daviludvig/Documents/UFSC/23.2/Python/10-17/Poker/docs/vencedores.txt", "w") as arquivo:
            for vencedor in vencedores:
                arquivo.write(f"{vencedor.nome} - {melhores_maos[vencedor.pontos.score - 2]}")
                if vencedor in melhores2:
                    arquivo.write(" *\n")
                else:
                    arquivo.write("\n")
                for carta in vencedor.rodada.get_cartas():
                    arquivo.write(f"{carta}\n")
                arquivo.write("\n")
            arquivo.write(f"FLOP:\n")            
            for carta in mesa.get_flop():
                arquivo.write(f"{carta}\n")
            arquivo.close()