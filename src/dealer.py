from pessoa import Pessoa

class Dealer(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def distribuir_primeiras_cartas(self, alvo, baralho):
        # Método que distribui uma carta para o jogador
        carta = baralho.get_baralho()[0]
        baralho.get_baralho().remove(carta)
        alvo._set_carta(carta)

    def distribuir_flop(self, mesa, baralho):
        # Método que distribui as cartas comunitárias
        for i in range(3):
            carta = baralho.get_baralho()[0]
            baralho.get_baralho().remove(carta)
            mesa._set_flop(carta)
    
    def distribuir_ficha(self, maleta, alvo):
        # Método que distribui uma ficha para um jogador
        ficha = maleta.get_fichas()[0]
        maleta.get_fichas().remove(ficha)
        alvo._set_ficha(ficha)
        
