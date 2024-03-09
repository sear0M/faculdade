nota = int(input('digite sua nota: '))

if nota <= 5:
    print('conceito D')
elif nota == 5 or nota == 6:
    print('conceito C')
elif nota == 7 or nota == 8:
    print('conceito B')
elif nota == 9 or nota == 10:
    print('conceito A')
else:
    print('nota invalida')