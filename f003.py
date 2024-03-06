salario = float(input('Digite seu Salario: '))
anos = int(input('Quantos anos na empresa: '))

if anos == 1:
    print(f'seu salario sera {salario * 1.1}')
if anos >= 2:
    print(f'seu salario sera {salario * 1.2}')
else:
    print(salario)