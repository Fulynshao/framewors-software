grenais = []

vitoria_inter = 0
vitoria_gremio = 0
empates = 0

while True:
    gols_inter = int(input("Gols do INTER no grenal: "))
    gols_gremio = int(input("Gols do GREMIO no grenal: "))
    grenais.append((gols_inter, gols_gremio))

    if gols_inter == gols_gremio:
        print("EMPATE")
        empates += 1
    elif gols_inter > gols_gremio:
        print("VITORIA DO INTER")
        vitoria_inter += 1
    elif gols_inter < gols_gremio:
        print("VITORIA DO GREMIO")
        vitoria_gremio += 1

    continuar = int(input("Deseja adicionar mais dados de GRENAL? (1-sim; 2-não): "))
    if continuar == 2:
        break

print(f"Grenais analisados: {len(grenais)}")
print(f"Vitórias coloradas: {vitoria_inter}")
print(f"Vitórias gremistas: {vitoria_gremio}")
print(f"Empates: {empates}")

if vitoria_inter > vitoria_gremio:
    print(f"Inter ganhou mais grenais com {vitoria_inter} vitórias a {vitoria_gremio}")
elif vitoria_inter < vitoria_gremio:
    print(f"Gremio ganhou mais grenais com {vitoria_gremio} vitórias a {vitoria_inter}")
else:
    print("Não houve vencedor maior de grenais")
