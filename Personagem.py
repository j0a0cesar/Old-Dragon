from dado import Dado
class Personagem:

    atributos_nomes =["forca", "destreza", "constituicao", "inteligecia","sabedoria","carisma"]

    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        
    dado =  Dado(6)

    def mostrar_atributos(self):
        print("\n--- Atributos Finais do Personagem ---")
        print(f"Força:         {self.forca}")
        print(f"Destreza:      {self.destreza}")
        print(f"Constituição:  {self.constituicao}")
        print(f"Inteligência:  {self.inteligencia}")
        print(f"Sabedoria:     {self.sabedoria}")
        print(f"Carisma:       {self.carisma}")

    def gerar_atributos(self):
        atributos = []
        for _ in range(6):
            soma_da_rolagem = 0
            for _ in range(3):
                soma_da_rolagem += self.dado.rolar()
            atributos.append(soma_da_rolagem)
        return atributos    
