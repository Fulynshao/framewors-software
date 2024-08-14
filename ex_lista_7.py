dados = []

while True:
    time = int(input("Clube (1-Gremio; 2-Inter; 3-Outros): "))
    if(time == 0):
        break
    cidade = int(input("Cidade (0-Porto Alegre; 1-Outra): "))
    dados.append((time, cidade))

total_gremio = 0
total_inter = 0
total_outros_times = 0
total_poa = 0
total_outras_cidades = 0
poa_outros_times = 0

for time, cidade in dados:
    if time == 1:
        total_gremio += 1
    elif time == 2:
        total_inter += 1
    elif time == 3:
        total_outros_times += 1

    if cidade == 0:
        total_poa += 1
    elif cidade == 1:
        total_outras_cidades += 1

    if cidade == 0 and time == 3:
        poa_outros_times += 1

print(f"Total de torcedores do Grêmio: {total_gremio}")
print(f"Total de torcedores do Inter: {total_inter}")
print(f"Total de torcedores de outros times: {total_outros_times}")
print(f"Porto-alegrenses que torcem para outros times: {poa_outros_times}")
print(f"Pessoas entrevistadas: {len(dados)}")

