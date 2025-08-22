from personagem import Personagem
from dado import Dado


class Classico(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = "classico"
        self.dado = Dado(6)

    def mostrar_atributos(self):
        print("\nEstilo: Clássico")
        super().mostrar_atributos()
