num1 = int(input('Digite um Numero: '))
num2 = int(input('digite outro numero: '))

if num1 >10 or num1 < 0:
    print('numero invalido')
elif num2 >10 or num2 < 0:
    print('numero invalido')
elif num1 + num2 < 8:
    print((num1 * num2) / 2)
elif num1 + num2 == 8:
    print(num1 * num2)
elif num1 + num2 >8:
    if num1>num2:
        print(num1/num2)
    else:
        print(num2/num1)
