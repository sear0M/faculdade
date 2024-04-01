soma = 0
contador = 0

while True:
    valor = int(input("Digite um valor inteiro positivo (ou um numero negativo para encerrar): "))
    
    if valor < 0:
        break
    
    soma += valor
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A media dos valores e: {media}")
else:
    print("Nenhum valor foi inserido.")
    