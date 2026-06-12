import random

opcoes = ["pedra", "papel", "tesoura"]

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
else:    print("Computador ganhou!")