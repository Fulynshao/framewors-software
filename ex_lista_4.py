dados = []

while True:
    sexo = input("Informe o sexo (M/F): ").upper()
    cor_olhos = input("Informe a cor dos olhos (A/V/C): ").upper()
    cor_cabelos = input("Informe a cor dos cabelos (L/C/P): ").upper()
    idade = int(input("Informe a idade: "))
    altura = float(input("Informe a altura (em cm): "))
    peso = float(input("Informe o peso (em kg): "))
    
    dados.append((sexo, cor_olhos, cor_cabelos, idade, altura, peso))
    
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar == 'N':
        break

total_pessoas = len(dados)
total_idade = 0
total_peso = 0
total_altura = 0
total_feminino = 0
total_verde_louro = 0

for pessoa in dados:
    sexo, cor_olhos, cor_cabelos, idade, altura, peso = pessoa
    total_idade += idade
    total_peso += peso
    total_altura += altura
    if sexo == 'F':
        total_feminino += 1
    if cor_olhos == 'V' and cor_cabelos == 'L':
        total_verde_louro += 1

if total_pessoas > 0:
    media_idade = total_idade / total_pessoas
    media_peso = total_peso / total_pessoas
    media_altura = total_altura / total_pessoas
    percentual_feminino = (total_feminino / total_pessoas) * 100
    percentual_masculino = 100 - percentual_feminino
else:
    media_idade = media_peso = media_altura = percentual_feminino = percentual_masculino = 0

# Exibição dos resultados
print(f"Média de idade: {media_idade:.2f} anos")
print(f"Média de peso: {media_peso:.2f} kg")
print(f"Média de altura: {media_altura:.2f} cm")
print(f"Percentual de mulheres: {percentual_feminino:.2f}%")
print(f"Percentual de homens: {percentual_masculino:.2f}%")
print(f"Pessoas com olhos verdes e cabelos louros: {total_verde_louro}")
