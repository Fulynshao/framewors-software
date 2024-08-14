x = int(input("Entre com o primeiro valor do intervalo: "))
y = int(input("Entre com o segundo valor do intervalo: "))
soma = 0

for i in range (x, y + 1):
    print(i)
    if i % 2 == 0:
        soma = soma + i

print("Soma dos num. pares no intervalo", soma)