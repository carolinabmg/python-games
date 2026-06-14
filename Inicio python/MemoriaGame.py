import tkinter as tk
from tkinter import messagebox
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

# =====================
# JANELA
# =====================

janela = tk.Tk()
janela.title("🃏 Jogo da Memória")
janela.geometry("500x650")
janela.resizable(False, False)

# =====================
# LABELS
# =====================

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
# RECORDE
# =====================

def carregar_recorde():
    if os.path.exists("recorde.txt"):
        with open("recorde.txt", "r") as arquivo:
            try:
                return int(arquivo.read())
            except:
                return 9999
    return 9999


def salvar_recorde(valor):
    with open("recorde.txt", "w") as arquivo:
        arquivo.write(str(valor))


# =====================
# ATUALIZAR TELA
# =====================

def atualizar_labels():
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
            text=f"⏱️ Tempo: {minutos:02}:{segundos:02}"
        )

        janela.after(
            1000,
            atualizar_tempo
        )


# =====================
# VERIFICAR PAR
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
# CLIQUE NAS CARTAS
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
# VITÓRIA
# =====================

def venceu():
    tempo = int(
        time.time() - inicio
    )

    minutos = tempo // 60
    segundos = tempo % 60

    recorde = carregar_recorde()

    mensagem = (
        f"🎉 PARABÉNS!\n\n"
        f"⭐ Pontos: {pontos}\n"
        f"🎯 Tentativas: {tentativas}\n"
        f"⏱️ Tempo: {minutos:02}:{segundos:02}"
    )

    if tentativas < recorde:
        salvar_recorde(tentativas)
        mensagem += "\n\n🏆 NOVO RECORDE!"

    messagebox.showinfo(
        "Vitória",
        mensagem
    )


# =====================
# REINICIAR
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

    cartas = EMOJIS.copy()
    random.shuffle(cartas)

    vidas = VIDAS_INICIAIS
    pontos = 0
    tentativas = 0
    pares_encontrados = 0

    primeira = None
    segunda = None

    atualizar_labels()

    for botao in botoes:
        botao.config(
            text="❓",
            state="normal"
        )

    inicio = time.time()
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
        command=lambda i=i: clicar(i)
    )

    botao.grid(
        row=i // 4,
        column=i % 4,
        padx=5,
        pady=5
    )

    botoes.append(botao)

# =====================
# BOTÃO NOVO JOGO
# =====================

tk.Button(
    janela,
    text="🔄 Novo Jogo",
    font=("Arial", 14),
    command=reiniciar
).pack(pady=15)

# =====================
# INICIAR
# =====================

reiniciar()

janela.mainloop()