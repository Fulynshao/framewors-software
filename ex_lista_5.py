senha = int(input())
contador = 0
senha_certa = 2014

while(True):
    if (senha != senha_certa):
        contador += 1
        print("SENHA INVALIDA")
        senha = int(input())
        
    else:
        print("ACESSO PERMITIDO")
        print("Senha digitada " + str(contador) + " vezes.")
        break