def coletar_dados():
    sexo = input("Informe o sexo (M/F): ").upper()
    cor_olhos = input("Informe a cor dos olhos (A/V/C): ").upper()
    cor_cabelos = input("Informe a cor dos cabelos (L/C/P): ").upper()
    idade = int(input("Informe a idade: "))
    altura = float(input("Informe a altura (em cm): "))
    peso = float(input("Informe o peso (em kg): "))
    return sexo, cor_olhos, cor_cabelos, idade, altura, peso

def calcular_estatisticas(dados):
    total_pessoas = len(dados)
    total_idade = sum(pessoa[3] for pessoa in dados)
    total_peso = sum(pessoa[4] for pessoa in dados)
    total_altura = sum(pessoa[5] for pessoa in dados)
    total_feminino = sum(1 for pessoa in dados if pessoa[0] == 'F')
    total_verde_louro = sum(1 for pessoa in dados if pessoa[1] == 'V' and pessoa[2] == 'L')

    media_idade = total_idade / total_pessoas
    media_peso = total_peso / total_pessoas
    media_altura = total_altura / total_pessoas
    percentual_feminino = (total_feminino / total_pessoas) * 100
    percentual_masculino = 100 - percentual_feminino

    print(f"Média de idade: {media_idade:.2f} anos")
    print(f"Média de peso: {media_peso:.2f} kg")
    print(f"Média de altura: {media_altura:.2f} cm")
    print(f"Percentual de mulheres: {percentual_feminino:.2f}%")
    print(f"Percentual de homens: {percentual_masculino:.2f}%")
    print(f"Pessoas com olhos verdes e cabelos louros: {total_verde_louro}")

if __name__ == "__main__":
    dados = []
    while True:
        dados.append(coletar_dados())
        continuar = input("Deseja continuar? (S/N): ").upper()
        if continuar == 'N':
            break
    calcular_estatisticas(dados)
