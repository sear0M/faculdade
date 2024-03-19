from random import randint
pedra = 0
papel = 1
tesoura = 2
n = randint(0,2)

jogada = int(input('Pedra, Papel ou Tesoura?, sendo respectivamente 0, 1 e 2: '))
print('-' * 23)
if jogada == n:
    print('Empate')
elif jogada == 0 and n == 1:
    print('Papel ganha de pedra')
elif jogada == 0 and n == 2:
    print('Pedra ganha de tesoura')
elif jogada == 1 and n == 0:
    print('Pedra ganha de papel')
elif jogada == 1 and n == 2:
    print('Papel ganha de tesoura')
elif jogada == 2 and n == 0:
    print('Pedra ganha de tesoura')
elif jogada == 2 and n == 1:
    print('Tesoura ganha de papel')
else:
    print('Jogada invalida')
print('-' * 23)
