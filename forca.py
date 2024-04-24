import random

with open("br-sem-acentos.txt", "r") as file:
    palavras = file.readlines()

palavras = [palavra.strip() for palavra in palavras]

palavra = random.choice(palavras)

letras_certas = []
letras_erradas = []

tentativas = 6

print("A palavra tem", len(palavra), "letras.")

while tentativas > 0:
    palavra_atual = ""
    for letra in palavra:
        if letra in letras_certas:
            palavra_atual += letra
        else:
            palavra_atual += "_"
    print("Palavra:", palavra_atual)

    if letras_erradas:
        print("Letras erradas:", " ".join(letras_erradas))

    if "_" not in palavra_atual:
        print("voce ganhou")
        tentativas = 0
    else:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_certas or letra in letras_erradas:
            print("Voce ja escolheu essa letra. Tente novamente.")
            continue

        if letra in palavra:
            letras_certas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra incorreta. Voce tem", tentativas, "tentativas restantes.")

if tentativas == 0:
    print("Voce perdeu, a palavra era:", palavra)
