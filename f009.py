nota = int(input('digite sua nota: '))

if nota >= 0 and nota <5:
    print('conceito D')
elif nota == 5 and nota == 6:
    print('conceito C')
elif nota == 7 and nota == 8:
    print('conceito B')
elif nota == 9 and nota == 10:
    print('conceito A')
else:
    print('nota invalida')