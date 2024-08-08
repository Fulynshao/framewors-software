n = int(input("Digite o limite: "))
soma = 0
produto = 1

for i in range (1, n + 1):
    if i % 2 == 0:
        soma = soma + i
    else:
        produto = produto * i

print("Soma dos valores pares até o limite:",soma)
print("Produto dos valores ímpares até o limite:",produto)