from personagem import Personagem
from dado import Dado

class Aventureiro(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = "aventureiro"
        self.dado = Dado(6)

    def gerar_atributos(self):
        atributos_rolados = []
        for _ in range(6):
            soma_da_rolagem = 0
            for _ in range(3):
                soma_da_rolagem += self.dado.rolar()
            atributos_rolados.append(soma_da_rolagem)
        return atributos_rolados
    
    def mostrar_atributos(self):
        print("\nEstilo: Aventureiro")
        super().mostrar_atributos()
