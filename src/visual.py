from PIL import Image, ImageDraw
import math

class Visual:
    def __init__(self, participantes, jogador):
        self.participantes = participantes
        self.exibir(jogador)
    
    def auxiliar(self, raio, elementos, deslocamento=0, centro = (150, 150)):
        posicoes = []
        angulo_inicial = math.radians(-90 + deslocamento)  # Inclinação de -90 graus com deslocamento
        angulo_total = math.radians(360)
        angulo_por_elemento = angulo_total / elementos
    
        for i in range(elementos):
            angulo = angulo_inicial + i * angulo_por_elemento
            x = int(raio * math.cos(angulo) + centro[0])
            y = int(raio * math.sin(angulo) + centro[1])
            posicoes.append((x, y))
        return posicoes
    
    def exibir(self, jogador):
        largura = 300
        altura = 300
        imagem = Image.new("RGB", (largura, altura), (255, 255, 255))
        desenho = ImageDraw.Draw(imagem)

        elementos = self.participantes
        raio = 100
        deslocamento = 360//len(elementos)
        centro = (130, 140)
        posicoes = self.auxiliar(raio, len(elementos), deslocamento, centro)

        fundo = Image.open("/Users/daviludvig/Documents/UFSC/23.2/Python/10-17/Poker/docs/mesa.jpg")
        imagem.paste(fundo, (35,35))
        for i in range(len(elementos)):
            x, y = posicoes[i]
            # imagem.paste(cadeira, (x - cadeira.width // 2, y - cadeira.height // 2), cadeira)
            elemento = elementos[i].nome
            if elemento == "Dealer":
                desenho.text((x, y), elemento, fill=(255, 0, 0))
            elif elemento == jogador:
                desenho.text((x, y), elemento, fill=(0, 0, 255))
            else:
                desenho.text((x, y), elemento, fill=(0, 0, 0))

        imagem.show()