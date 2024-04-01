n = int(input("Digite a quantidade de valores a serem lidos: "))

for _ in range(n):
    valor = int(input("Digite um valor: "))
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i
    print(f"O fatorial de {valor} é {fatorial}")
