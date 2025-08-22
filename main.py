from personagem import Personagem 
from classico import Classico
from aventureiro import Aventureiro
from heroico import Heroico
from auxiliares import Auxiliares


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
        atributos_finais = Auxiliares.permitir_distribuicao(valores_gerados)
        
    if len(atributos_finais) != 6:
        print("\nOcorreu um erro na geração dos atributos.")
        return

    for nome_atributo, valor_atributo in zip(Personagem.atributos_nomes,atributos_finais):
        setattr(personagem, nome_atributo, valor_atributo )

    personagem.mostrar_atributos() 


if __name__ == "__main__":
    main()
