import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time
import os

# =====================
# CONFIGURAÇÕES
# =====================

EMOJIS = [
    "🐱", "🐱",
    "🐶", "🐶",
    "🐸", "🐸",
    "🦊", "🦊",
    "🐼", "🐼",
    "🐵", "🐵",
    "🦄", "🦄",
    "🐧", "🐧"
]

VIDAS_INICIAIS = 5

# =====================
# VARIÁVEIS
# =====================

cartas = []
botoes = []

primeira = None
segunda = None
travado = False

vidas = VIDAS_INICIAIS
pontos = 0
tentativas = 0
pares_encontrados = 0
inicio = 0

nome_jogador = "Aventureiro"

# =====================
# JANELA
# =====================

janela = tk.Tk()
janela.title("🃏 Jogo da Memória Deluxe")
janela.geometry("500x700")
janela.resizable(False, False)

# =====================
# LABELS
# =====================

label_jogador = tk.Label(
    janela,
    text="👤 Jogador:",
    font=("Arial", 14)
)
label_jogador.pack()

label_vidas = tk.Label(
    janela,
    text="❤️ Vidas: 5",
    font=("Arial", 14)
)
label_vidas.pack()

label_pontos = tk.Label(
    janela,
    text="⭐ Pontos: 0",
    font=("Arial", 14)
)
label_pontos.pack()

label_tentativas = tk.Label(
    janela,
    text="🎯 Tentativas: 0",
    font=("Arial", 14)
)
label_tentativas.pack()

label_tempo = tk.Label(
    janela,
    text="⏱️ Tempo: 00:00",
    font=("Arial", 14)
)
label_tempo.pack()

# =====================
# TABULEIRO
# =====================

frame = tk.Frame(janela)
frame.pack(pady=20)

# =====================
# FUNÇÕES DO RANKING
# =====================

def carregar_ranking():
    ranking = []

    if os.path.exists("ranking.txt"):
        with open(
            "ranking.txt",
            "r",
            encoding="utf-8"
        ) as arquivo:

            for linha in arquivo:
                try:
                    nome, tent, tempo = linha.strip().split(",")

                    ranking.append(
                        (
                            nome,
                            int(tent),
                            int(tempo)
                        )
                    )
                except:
                    pass

    return ranking


def salvar_ranking(nome, tentativas, tempo):
    ranking = carregar_ranking()

    ranking.append(
        (
            nome,
            tentativas,
            tempo
        )
    )

    ranking.sort(
        key=lambda jogador:
        (jogador[1], jogador[2])
    )

    ranking = ranking[:10]

    with open(
        "ranking.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        for jogador in ranking:
            arquivo.write(
                f"{jogador[0]},"
                f"{jogador[1]},"
                f"{jogador[2]}\n"
            )


def mostrar_ranking():
    ranking = carregar_ranking()

    if not ranking:
        messagebox.showinfo(
            "Ranking",
            "Ainda não há jogadores no ranking."
        )
        return

    texto = "🏆 TOP 10 AVENTUREIROS\n\n"

    for posicao, jogador in enumerate(
            ranking,
            start=1):

        nome = jogador[0]
        tent = jogador[1]
        tempo = jogador[2]

        minutos = tempo // 60
        segundos = tempo % 60

        if posicao == 1:
            medalha = "🥇"
        elif posicao == 2:
            medalha = "🥈"
        elif posicao == 3:
            medalha = "🥉"
        else:
            medalha = "🏅"

        texto += (
            f"{medalha} "
            f"{nome} - "
            f"{tent} tentativas - "
            f"{minutos:02}:{segundos:02}\n"
        )

    messagebox.showinfo(
        "Ranking",
        texto
    )

# =====================
# LABELS
# =====================

def atualizar_labels():
    label_jogador.config(
        text=f"👤 Jogador: {nome_jogador}"
    )

    label_vidas.config(
        text=f"❤️ Vidas: {vidas}"
    )

    label_pontos.config(
        text=f"⭐ Pontos: {pontos}"
    )

    label_tentativas.config(
        text=f"🎯 Tentativas: {tentativas}"
    )

# =====================
# CRONÔMETRO
# =====================

def atualizar_tempo():
    if pares_encontrados < 8:

        segundos = int(
            time.time() - inicio
        )

        minutos = segundos // 60
        segundos = segundos % 60

        label_tempo.config(
            text=f"⏱️ Tempo: "
                 f"{minutos:02}:{segundos:02}"
        )

        janela.after(
            1000,
            atualizar_tempo
        )

# =====================
# VITÓRIA
# =====================

def venceu():
    tempo = int(
        time.time() - inicio
    )

    salvar_ranking(
        nome_jogador,
        tentativas,
        tempo
    )

    minutos = tempo // 60
    segundos = tempo % 60

    messagebox.showinfo(
        "Vitória",
        f"🎉 Parabéns, {nome_jogador}!\n\n"
        f"⭐ Pontos: {pontos}\n"
        f"🎯 Tentativas: {tentativas}\n"
        f"⏱️ Tempo: "
        f"{minutos:02}:{segundos:02}"
    )

# =====================
# VERIFICAR CARTAS
# =====================

def verificar():
    global primeira
    global segunda
    global travado
    global vidas
    global pontos
    global tentativas
    global pares_encontrados

    i = primeira
    j = segunda

    tentativas += 1

    if cartas[i] == cartas[j]:

        botoes[i].config(
            state="disabled"
        )

        botoes[j].config(
            state="disabled"
        )

        pontos += 100
        pares_encontrados += 1

    else:

        vidas -= 1

        pontos = max(
            0,
            pontos - 20
        )

        botoes[i].config(
            text="❓"
        )

        botoes[j].config(
            text="❓"
        )

    atualizar_labels()

    primeira = None
    segunda = None
    travado = False

    if vidas == 0:
        messagebox.showinfo(
            "Game Over",
            "💀 Você perdeu!"
        )
        reiniciar()

    if pares_encontrados == 8:
        venceu()

# =====================
# CLIQUE
# =====================

def clicar(indice):
    global primeira
    global segunda
    global travado

    if travado:
        return

    if botoes[indice]["state"] == "disabled":
        return

    if indice == primeira:
        return

    botoes[indice].config(
        text=cartas[indice]
    )

    if primeira is None:
        primeira = indice
    else:
        segunda = indice
        travado = True

        janela.after(
            700,
            verificar
        )

# =====================
# NOVO JOGO
# =====================

def reiniciar():
    global cartas
    global vidas
    global pontos
    global tentativas
    global pares_encontrados
    global primeira
    global segunda
    global inicio
    global nome_jogador

    nome = simpledialog.askstring(
        "Jogador",
        "Digite seu nome:"
    )

    if nome:
        nome_jogador = nome
    else:
        nome_jogador = "Aventureiro"

    cartas = EMOJIS.copy()
    random.shuffle(cartas)

    vidas = VIDAS_INICIAIS
    pontos = 0
    tentativas = 0
    pares_encontrados = 0

    primeira = None
    segunda = None

    for botao in botoes:
        botao.config(
            text="❓",
            state="normal"
        )

    inicio = time.time()

    atualizar_labels()
    atualizar_tempo()

# =====================
# CRIAR BOTÕES
# =====================

for i in range(16):

    botao = tk.Button(
        frame,
        text="❓",
        width=5,
        height=2,
        font=("Arial", 20),
        command=lambda i=i:
        clicar(i)
    )

    botao.grid(
        row=i // 4,
        column=i % 4,
        padx=5,
        pady=5
    )

    botoes.append(botao)

# =====================
# BOTÕES EXTRAS
# =====================

tk.Button(
    janela,
    text="🔄 Novo Jogo",
    font=("Arial", 14),
    command=reiniciar
).pack(pady=5)

tk.Button(
    janela,
    text="🏆 Ranking Top 10",
    font=("Arial", 14),
    command=mostrar_ranking
).pack(pady=5)

# =====================
# INICIAR
# =====================

reiniciar()

janela.mainloop()