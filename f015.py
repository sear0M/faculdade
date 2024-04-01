soma_salarios = 0
soma_filhos = 0
contador_pessoas = 0
contador_salario_ate_1000 = 0
maior_salario = float('-inf')

while True:
    salario = float(input("Digite o salário (ou um número negativo para encerrar): "))
    
    if salario < 0:
        break
    
    soma_salarios += salario
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario <= 1000:
        contador_salario_ate_1000 += 1
    
    num_filhos = int(input("Digite o número de filhos: "))
    
    soma_filhos += num_filhos
    
    contador_pessoas += 1

media_salarios = soma_salarios / contador_pessoas if contador_pessoas > 0 else 0

media_filhos = soma_filhos / contador_pessoas if contador_pessoas > 0 else 0

percentual_salario_ate_1000 = (contador_salario_ate_1000 / contador_pessoas) * 100 if contador_pessoas > 0 else 0

print(f"Media do salario da populacao: {media_salarios}")
print(f"Media do numero de filhos: {media_filhos}")
print(f"Maior salario: {maior_salario}")
print(f"Percentual de pessoas com salario atr R$1000,00: {percentual_salario_ate_1000}%")
