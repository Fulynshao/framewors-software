notas = []

while(True):
    nota1 = float(input())
    if(nota1 < 0 or nota1 > 10):
        print("NOTA INVALIDA")
    else:
        notas.append(nota1)
    nota2 = float(input())
    if(nota2 < 0 or nota2 > 10):
        print("NOTA INVALIDA")
    else:
        notas.append(nota2)
