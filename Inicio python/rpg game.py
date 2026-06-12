personagem = {
    "nome": "Aragorn",
    "classe": "Mago",
    "nivel": 5,
    "vida": 100,
    "ataque": 20,
    "defesa": 10
}

inimigos = [
    {"nome": "Orc", "vida": 50},
    {"nome": "dragon", "vida": 30},
    {"nome": "Troll", "vida": 80}

]

print(f"⚔️ Bem-vindo, {personagem['nome']}!")

import random

def atacar(atacante, alvo):
    chance = random.randint(1, 100)

    if chance <= 20:
        print(f"❌ {atacante['nome']} errou o ataque!")
        return

    dano = max(0, atacante["ataque"] - alvo["defesa"])
    alvo["vida"] -= dano

    print(f"⚔️ {atacante['nome']} atacou {alvo['nome']}")
    print(f"💥 Dano: {dano}")

while len(inimigos) > 0:

    print("\n👹 Inimigos:")
    for i, inimigo in enumerate(inimigos, start=1):
        print(f"{i} - {inimigo['nome']} ❤️ {inimigo['vida']}")

    print("\nAções:") # Imprime as opções de ação para o jogador
    print("1 - Atacar")
    print("2 - Curar")

    escolha = input("O que deseja fazer? ") # Solicita ao jogador que escolha uma ação

    if escolha == "1":

        alvo = int(input("Escolha o número do inimigo: ")) - 1 # Solicita ao jogador que escolha um inimigo para atacar   

        if 0 <= alvo < len(inimigos):

            inimigo_escolhido = inimigos[alvo]

            dano_causado = max(
                0,
                personagem["ataque"] - 5
            )

            inimigo_escolhido["vida"] = max(
                0,
                inimigo_escolhido["vida"] - dano_causado
            )

            print(
                f"\n⚔️ Você causou {dano_causado} de dano ao "
                f"{inimigo_escolhido['nome']}!"
            )

            print(
                f"❤️ Vida restante: "
                f"{inimigo_escolhido['vida']}"
            )

            if inimigo_escolhido["vida"] <= 0:
                print(
                    f"💀 {inimigo_escolhido['nome']} foi derrotado!"
                )

                inimigos.remove(inimigo_escolhido)

        else:
            print("❌ Inimigo não existe!")

    elif escolha == "2": # Verifica se o jogador escolheu curar

        personagem["vida"] += 20

        print(
            f"✨ Você se curou!"
        )

        print(
            f"❤️ Vida atual: {personagem['vida']}"
        )

    else:
        print("❌ Opção inválida!")

if len(inimigos) == 0: # Verifica se todos os inimigos foram derrotados
    print("\n🏆 Todos os inimigos foram derrotados!")
    print("🎉 Vitória!")