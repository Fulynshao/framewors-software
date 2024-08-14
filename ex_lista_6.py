while True:
    while True:
        nota1 = float(input("Digite a primeira nota entre 0 e 10: "))
        if 0 <= nota1 <= 10:
            break
        else:
            print("NOTA INVALIDA")
    
    while True:
        nota2 = float(input("Digite a segunda nota entre 0 e 10: "))
        if 0 <= nota2 <= 10:
            break
        else:
            print("NOTA INVALIDA")
    
    media = (nota1 + nota2) / 2
    print(f"Média = {media:.2f}")
    
    repetir = int(input("Deseja calcular novamente? (1-Sim 0-Não): "))
    if repetir == 0:
        break
