import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 20)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 20.")

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()