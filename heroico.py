from personagem import Personagem
from dado import Dado

class Heroico(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = "heroico"
        self.dado = Dado(6)
    
    def gerar_atributos(self):
        atributos_rolados = []
        for _ in range(6):
            rolagens_individuais = []
            for _ in range(4):
                rolagens_individuais.append(self.dado.rolar())
            
            rolagens_individuais.remove(min(rolagens_individuais))
            soma_final = sum(rolagens_individuais)
            atributos_rolados.append(soma_final)
        return atributos_rolados
    
    def mostrar_atributos(self):
        print("\nEstilo: Heroico")
        super().mostrar_atributos()
