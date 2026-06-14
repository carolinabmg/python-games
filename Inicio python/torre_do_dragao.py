
import random

print("🧙‍♂️ A Torre do Dragão 🐉")
print("-" * 30)

vida = 100
pocoes = 3
nivel = 1

while vida > 0 and nivel <= 5:
    print(f"\n🌟 Fase {nivel}")
    inimigo = random.randint(15, 35)

    print(f"🐲 Um monstro apareceu com {inimigo} de vida!")

    while inimigo > 0 and vida > 0:
        print(f"\n❤️ Sua vida: {vida}")
        print(f"🧪 Poções: {pocoes}")
        print(f"🐲 Vida do monstro: {inimigo}")

        print("\n1 - Atacar")
        print("2 - Usar Poção")

        escolha = input("Escolha: ")

        if escolha == "1":
            dano = random.randint(10, 25)
            inimigo -= dano
            print(f"⚔️ Você causou {dano} de dano!")

        elif escolha == "2":
            if pocoes > 0:
                cura = random.randint(20, 35)
                vida += cura
                pocoes -= 1
                print(f"✨ Você recuperou {cura} de vida!")
            else:
                print("❌ Você não possui poções!")

        if inimigo > 0:
            ataque = random.randint(5, 20)
            vida -= ataque
            print(f"💥 O monstro atacou e causou {ataque} de dano!")

    if vida > 0:
        print(f"🏆 Você venceu a fase {nivel}!")
        nivel += 1

if vida <= 0:
    print("\n💀 GAME OVER!")
else:
    print("\n👑 PARABÉNS! Você derrotou todos os monstros da torre!")
