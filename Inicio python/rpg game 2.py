import random

# Personagem
personagem = {
    "nome": "Carolina",
    "classe": "Mago"
    "vida": 100,
    "ataque": 20,
    "defesa": 10,
    "nivel": 1,
    "xp": 0
}

inimigos = [
    {"nome": "Orc", "vida": 50, "defesa": 5, "xp": 10},
    {"nome": "Dragon", "vida": 30, "defesa": 8, "xp": 20},
    {"nome": "Troll", "vida": 80, "defesa": 3, "xp": 15}
]

# Função de ataque
def atacar(atacante, alvo):

    # Sorteia um número entre 1 e 100
    chance = random.randint(1, 100)

    # 20% de chance de errar
    if chance <= 20:
        print(f"❌ {atacante['nome']} errou o ataque!")
        return

    # Calcula o dano
    dano = max(
        0,
        atacante["ataque"] - alvo["defesa"]
    )

    # Remove vida do alvo
    alvo["vida"] = max(
        0,
        alvo["vida"] - dano
    )

    # Mostra o resultado
    print(f"⚔️ {atacante['nome']} atacou {alvo['nome']}!")
    print(f"💥 Dano causado: {dano}")
    print(f"❤️ Vida restante do {alvo['nome']}: {alvo['vida']}")

# Antes do ataque
print("=== ANTES DO ATAQUE ===")
print(f"{orc['nome']} tem {orc['vida']} de vida")

# Faz o ataque
atacar(personagem, )

# Depois do ataque
print("\n=== DEPOIS DO ATAQUE ===")
print(f"{['nome']} tem {['vida']} de vida")