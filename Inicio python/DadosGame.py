import random

print("🎲 Bem-vindo ao Jogo de Dados!")

jogador = random.randint(1, 6)
computador = random.randint(1, 6)

print(f"\nVocê tirou: {jogador}")
print(f"Computador tirou: {computador}")

if jogador > computador:
    print("\n🎉 Você venceu!")
elif computador > jogador:
    print("\n💻 O computador venceu!")
else:
    print("\n🤝 Empate!")