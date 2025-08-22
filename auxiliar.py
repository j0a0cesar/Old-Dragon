class Auxiliar:

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
