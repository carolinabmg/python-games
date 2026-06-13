import random

opcoes = ["pedra", "papel", "tesoura"]

computador = random.choice(opcoes) #random.choice() é uma função da biblioteca random que seleciona aleatoriamente um elemento de uma sequência (como uma lista). Neste caso, ela escolhe aleatoriamente entre "pedra", "papel" e "tesoura" para o computador.

jogador = input("Escolha pedra, papel ou tesoura: ").lower() #.lower() para garantir que a entrada do usuário seja tratada como minúscula, independentemente de como ele digite.

print(f"Você escolheu: {jogador}")
print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):  
    print("Você ganhou!")
else:    print("Computador ganhou!")

while True:
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()

    if jogar_novamente == "s":
        computador = random.choice(opcoes)
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        print(f"Você escolheu: {jogador}")
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
        else:
            print("Computador ganhou!")

    elif jogar_novamente == "n":
        print("👋 Obrigado por jogar!")
        break

    else:
        print("❌ Digite apenas s ou n.")