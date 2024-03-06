cod = int(input('digite o código: '))

if cod == 1:
    print('CD-ROM (700MB)') 
elif cod == 2:
    print('DVD-ROM (4.7GB)')
elif cod == 3:
    print('DVD-9 (8.54 GB)')
elif cod == 4:
    print('Blu-Ray (25 GB)')
else:
    print('codigo invalido')