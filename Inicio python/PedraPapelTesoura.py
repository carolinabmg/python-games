import random

def jogar_rodada():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    
    jogador = input("Escolha pedra, papel ou tesoura: ").lower().strip()
    
    if jogador not in opcoes:
        print("❌ Opção inválida!")
        return None
    
    print(f"Você: {jogador} | Computador: {computador}")
    
    vence = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}
    
    if jogador == computador:
        return "empate"
    elif vence[jogador] == computador:
        return "vitória"
    else:
        return "derrota"

# Loop com pontuação
pontos = {"você": 0, "computador": 0}

while True:
    resultado = jogar_rodada()
    
    if resultado == "vitória":
        pontos["você"] += 1
        print("🎉 Você ganhou!\n")
    elif resultado == "derrota":
        pontos["computador"] += 1
        print("💻 Computador ganhou!\n")
    elif resultado == "empate":
        print("🤝 Empate!\n")
    
    print(f"Placar: Você {pontos['você']} x {pontos['computador']} Computador")
    
    if input("Jogar novamente? (s/n): ").lower() != "s":
        print(f"\n📊 Placar final: {pontos}\n👋 Tchau!")
        break
