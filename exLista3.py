n = int(input("Digite a quantidade de numeros: "))
numeros = []
maior_vinte = 0
maior_dez = 0
entre_dez_e_cem = []

for i in range (1, n + 1):
    numero = int(input("Informe numero: "))
    numeros.append(numero)
    if numero > 20:
        maior_vinte += 1
    if numero > 10:
        maior_dez += 1
    if numero >= 10 and numero <= 100:
        entre_dez_e_cem.append(numero)

print("a) maior valor: ", max(numeros))
print("b) menor valor: ", min(numeros))
print("c) soma dos valores: ", sum(numeros))
media = sum(numeros) / n
print("d) media dos valores do vetor: ", media)
print("e) Numero de valores maiores que 20:", maior_vinte)
perc_maior_dez = (maior_dez * 100) / n
print("f) Percentagem (%) dos maiores que 10 na lista:", perc_maior_dez)
if entre_dez_e_cem:
    media10e100 = sum(entre_dez_e_cem) / len(entre_dez_e_cem)
    print("g) Media dos valores entre 10 e 100",media10e100)
else:
    print("g) Nao ha numeros entre 10 e 100 para obter a media")
    

