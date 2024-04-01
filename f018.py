votos_candidatos = [0, 0, 0, 0]
votos_nulos = 0
votos_em_branco = 0

while True:
    voto = int(input("Digite o codigo do candidato (ou 0 para encerrar): "))
    
    if voto == 0:
        break
    
    if voto >= 1 and voto <= 4:
        votos_candidatos[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    else:
        print("Codigo de voto invalido. Por favor, insira novamente.")

for i in range(4):
    print(f"Total de votos para o candidato {i+1}: {votos_candidatos[i]}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_em_branco}")
