import random

def escolher_palavra():
    palavras = ["python", "programação", "computador", "algoritmo", "desenvolvimento"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")

    while tentativas < tentativas_maximas:
        print("\nPalavra: " + exibir_palavra_oculta(palavra, letras_corretas))

        if "_" not in exibir_palavra_oculta(palavra, letras_corretas):
            print("Parabéns! Você acertou a palavra!")
            break

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
        elif tentativa in palavra:
            print("Letra correta!")
            letras_corretas.append(tentativa)
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas += 1

    if tentativas == tentativas_maximas:
        print("\nVocê perdeu! A palavra correta era: " + palavra)

# Inicia o jogo da forca
jogar_forca()
