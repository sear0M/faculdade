nota = float(input('digite sua nota: '))

if nota >100:
    print('Nota Invalida')
if nota< 0:
    print(input('Nota invalida'))
    if nota >= 60:
        print('Aprovado')
    else:
        print('Reprovado')