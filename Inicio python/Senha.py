import random
import string

print("🔐 GERADOR DE SENHAS")

print("""
1 - Senha simples
2 - Senha forte
3 - Senha muito forte
""")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    tamanho = 8

elif opcao == 2:
    tamanho = 12

elif opcao == 3:
    tamanho = 16

else:
    print("Opção inválida!")
    exit()

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print(f"\n✅ Senha gerada: {senha}")