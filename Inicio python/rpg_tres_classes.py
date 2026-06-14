
import random

print("🧙 RPG DAS TRÊS CLASSES 🏰")
print("=" * 35)

nome = input("Digite o nome do herói: ")

print("\nEscolha sua classe:")
print("1 - 🧙 Mago")
print("2 - ⚔️ Guerreiro")
print("3 - 🏹 Arqueiro")

classe = input("Escolha: ")

if classe == "1":
    classe_nome = "Mago"
    vida = 80
    ataque = 30
elif classe == "2":
    classe_nome = "Guerreiro"
    vida = 120
    ataque = 20
else:
    classe_nome = "Arqueiro"
    vida = 100
    ataque = 25

xp = 0
nivel = 1

print(f"\n🌟 {nome}, o {classe_nome}, inicia sua jornada!")

while vida > 0 and nivel <= 5:

    monstro_vida = random.randint(40, 80)
    print(f"\n🐲 Um monstro apareceu! Vida: {monstro_vida}")

    while monstro_vida > 0 and vida > 0:

        print(f"\n👤 {nome} | Classe: {classe_nome}")
        print(f"❤️ Vida: {vida}")
        print(f"⭐ Nível: {nivel}")
        print(f"✨ XP: {xp}")
        print(f"🐲 Vida do monstro: {monstro_vida}")

        input("\nPressione ENTER para atacar...")

        dano = random.randint(
            ataque - 5,
            ataque + 10
        )

        monstro_vida -= dano

        print(f"⚔️ Você causou {dano} de dano!")

        if monstro_vida > 0:
            dano_monstro = random.randint(8, 18)
            vida -= dano_monstro
            print(
                f"💥 O monstro causou "
                f"{dano_monstro} de dano!"
            )

    if vida > 0:
        ganho = 50
        xp += ganho

        print(
            f"\n🏆 Monstro derrotado!"
            f"\n✨ +{ganho} XP"
        )

        if xp >= nivel * 50:
            nivel += 1
            vida += 20

            print(
                f"🌟 LEVEL UP!"
                f"\nNovo nível: {nivel}"
            )
            print(
                f"❤️ Vida restaurada +20"
            )

if vida <= 0:
    print("\n💀 GAME OVER!")
else:
    print(
        f"\n👑 PARABÉNS, {nome}!"
        f"\nVocê terminou a aventura!"
    )
