numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

if numero < 0:
    print("Erro: Não é possível calcular o fatorial de um número negativo.")
else:
    fatorial = 1
    # Calcula o fatorial do número
    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é: {fatorial}")
