ano = int(input('digite o ano do carro: '))
peso = float(input('digite o seu peso: '))

print(f'-' * 18)

if ano <=1970:
    if peso < 1200:
        print('classe 1 - 16,50')
    elif peso <=1700:
        print('classe 2 - 25,50')
    elif peso >1700:
        print('classe 3 - 46,50')
elif ano <=1979:
    if peso <1200:
        print('classe 4 - 27,00')
    elif peso <=1700:
        print('classe 5 - 30,50')
    elif peso >1700:
        print('classe 6 - 52,50')
elif ano >=1980:
    if peso <1600:
        print('classe 7 - 19,50')
    else:
        print('classe 8 - 55,50')

print(f'-' * 18)