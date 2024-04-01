n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 <= n2:
    inicio = n1
    fim = n2
else:
    inicio = n2
    fim = n1

print("Intervalo fechado entre", inicio, "e", fim, ":")
for numero in range(inicio, fim + 1):
    print(numero, end=" ")
