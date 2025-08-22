from personagem import Personagem 
from classico import Classico
from aventureiro import Aventureiro
from heroico import Heroico


def permitir_distribuicao(valores_rolados):
    print(f"\nRolagens disponíveis: {sorted(valores_rolados)}")
    print("Agora, distribua esses valores entre os 6 atributos.")

    valores_disponiveis = sorted(valores_rolados)
    atributos_finais = []
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    for nome in nomes_atributos:
        while True:
            try:
                valor_str = input(f"Digite o valor para {nome} (disponíveis: {valores_disponiveis}): ")
                valor_int = int(valor_str)
                if valor_int in valores_disponiveis:
                    atributos_finais.append(valor_int)
                    valores_disponiveis.remove(valor_int)
                    break
                else:
                    print("Valor inválido ou já utilizado. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
    return atributos_finais

def main():
    print("--- Gerador de Atributos de Personagem ---")
    estilo = input("Escolha o estilo de geração (classico, aventureiro, heroico): ").strip().lower()

    personagem = None

    if estilo == "classico":
        personagem = Classico()
    elif estilo == "aventureiro":
        personagem = Aventureiro()
    elif estilo == "heroico":
        personagem = Heroico()
    else:
        print("Estilo inválido.")
        return

    valores_gerados = personagem.gerar_atributos()
    
    atributos_finais = []
    if estilo == "classico":
        atributos_finais = valores_gerados
    else:
        atributos_finais = permitir_distribuicao(valores_gerados)
        
    if len(atributos_finais) != 6:
        print("\nOcorreu um erro na geração dos atributos.")
        return

    for nome_atributo, valor_atributo in zip(Personagem.atributos_nomes,atributos_finais):
        setattr(personagem, nome_atributo, valor_atributo )

    personagem.mostrar_atributos() 


if __name__ == "__main__":
    main()
