from PIL import Image, ImageDraw
import math

class Visual:
    def __init__(self, participantes, jogador):
        self.participantes = participantes
        self.exibir(jogador)
    
    def auxiliar(self, raio, elementos):
        posicoes = []
        for i in range(elementos):
            angulo = (2 * math.pi / elementos) * i
            x = int(raio * math.cos(angulo) + raio)
            y = int(raio * math.sin(angulo) + raio)
            posicoes.append((x, y))
        return posicoes
    
    def exibir(self, jogador):
        largura = 300
        altura = 300
        imagem = Image.new("RGB", (largura, altura), (255, 255, 255))
        desenho = ImageDraw.Draw(imagem)

        elementos = self.participantes
        raio = 100
        posicoes = self.auxiliar(raio, len(elementos))

        for i in range(len(elementos)):
            x, y = posicoes[i]
            elemento = elementos[i].nome
            if elemento == "Dealer":
                desenho.text((x, y), elemento, fill=(255, 0, 0))
            elif elemento == jogador:
                desenho.text((x, y), elemento, fill=(100, 255, 0))
            else:
                desenho.text((x, y), elemento, fill=(0, 0, 0))

        imagem.show()


# import math
# import tkinter as tk

# class Visual:
#     def __init__(self, participantes):
#         self.participantes = participantes
#         self.exibir()

#     def auxiliar(self, raio, elementos):
#         posicoes = []
#         for i in range(elementos):
#             angulo = (2 * math.pi / elementos) * i
#             x = raio * math.cos(angulo) + 100  # Ajuste 100 para o centro da janela
#             y = raio * math.sin(angulo) + 100
#             posicoes.append((x, y))
#         return posicoes

#     def exibir(self):
#         elementos = self.participantes
#         janela = tk.Tk()
#         janela.title("Disposição dos participantes")

#         raio = 50
#         numero = len(elementos)
#         posicoes = self.auxiliar(raio, numero)
#         for i in range(len(elementos)):
#             elemento = elementos[i]
#             x, y = posicoes[i]
#             label = tk.Label(janela, text=elemento)
#             label.place(x=x, y=y)

#         janela.geometry("300x200")
#         janela.mainloop()
