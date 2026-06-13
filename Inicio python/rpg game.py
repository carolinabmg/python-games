import random

personagem = {
    "nome": "Carolina",
    "classe": "Mago",
    "nivel": 5,
    "vida": 100,
    "ataque": 20,
    "defesa": 10
}

inimigos = [
    {"nome": "Orc", "vida": 50, "defesa": 5},
    {"nome": "Dragon", "vida": 30, "defesa": 8},
    {"nome": "Troll", "vida": 80, "defesa": 3}
]

print(f"⚔️ Bem-vindo, {personagem['nome']}!")

def atacar(atacante, alvo):
    chance = random.randint(1, 100)

    if chance <= 20:
        print(f"❌ {atacante['nome']} errou o ataque!")
        return

    dano = max(0, atacante["ataque"] - alvo["defesa"])

    alvo["vida"] = max(0, alvo["vida"] - dano)

    print(f"\n⚔️ {atacante['nome']} atacou {alvo['nome']}!")
    print(f"💥 Dano causado: {dano}")
    print(f"❤️ Vida restante: {alvo['vida']}")

while len(inimigos) > 0:

    print("\n👹 Inimigos:")
    for i, inimigo in enumerate(inimigos, start=1):
        print(f"{i} - {inimigo['nome']} ❤️ {inimigo['vida']}")

    print("\nAções:")
    print("1 - Atacar")
    print("2 - Curar")

    escolha = input("O que deseja fazer? ")

    if escolha == "1":

        alvo = int(input("Escolha o número do inimigo: ")) - 1

        if 0 <= alvo < len(inimigos):

            inimigo_escolhido = inimigos[alvo]

            atacar(personagem, inimigo_escolhido)

            if inimigo_escolhido["vida"] <= 0:
                print(f"💀 {inimigo_escolhido['nome']} foi derrotado!")
                inimigos.remove(inimigo_escolhido)

        else:
            print("❌ Inimigo não existe!")

    elif escolha == "2":

        personagem["vida"] += 20

        print("✨ Você se curou!")
        print(f"❤️ Vida atual: {personagem['vida']}")

    else:
        print("❌ Opção inválida!")

print("\n🏆 Todos os inimigos foram derrotados!")
print("🎉 Vitória!")