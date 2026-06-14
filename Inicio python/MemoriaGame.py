
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time
import os

EMOJIS = ["🐱","🐱","🐶","🐶","🐸","🐸","🦊","🦊",
          "🐼","🐼","🐵","🐵","🦄","🦄","🐧","🐧"]

VIDAS_INICIAIS = 100
MAX_TENTATIVAS = 100

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

janela = tk.Tk()
janela.title("🃏 Jogo da Memória Deluxe")
janela.geometry("520x720")
janela.resizable(False, False)

label_jogador = tk.Label(janela, text="👤 Jogador:", font=("Arial", 14))
label_jogador.pack()

label_vidas = tk.Label(janela, text="❤️ Vidas: 100", font=("Arial", 14))
label_vidas.pack()

label_pontos = tk.Label(janela, text="⭐ Pontos: 0", font=("Arial", 14))
label_pontos.pack()

label_tentativas = tk.Label(janela, text="🎯 Tentativas: 0/100", font=("Arial", 14))
label_tentativas.pack() 

label_tempo = tk.Label(janela, text="⏱️ Tempo: 00:00", font=("Arial", 14))
label_tempo.pack()

frame = tk.Frame(janela)
frame.pack(pady=20)


def carregar_ranking():
    ranking = []
    if os.path.exists("ranking.txt"):
        with open("ranking.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                try:
                    nome, tent, tempo = linha.strip().split(",")
                    ranking.append((nome, int(tent), int(tempo)))
                except:
                    pass
    return ranking


def salvar_ranking(nome, tent, tempo):
    ranking = carregar_ranking()
    ranking.append((nome, tent, tempo))
    ranking.sort(key=lambda x: (x[1], x[2]))
    ranking = ranking[:10]

    with open("ranking.txt", "w", encoding="utf-8") as arq:
        for n, t, tm in ranking:
            arq.write(f"{n},{t},{tm}\n")


def mostrar_ranking():
    ranking = carregar_ranking()

    if not ranking:
        messagebox.showinfo("Ranking", "Ainda não há jogadores no ranking.")
        return

    texto = "🏆 TOP 10 AVENTUREIROS\n\n"

    for pos, (nome, tent, tempo) in enumerate(ranking, start=1):
        minutos = tempo // 60
        segundos = tempo % 60

        medalha = "🏅"
        if pos == 1:
            medalha = "🥇"
        elif pos == 2:
            medalha = "🥈"
        elif pos == 3:
            medalha = "🥉"

        texto += (
            f"{medalha} {nome} - "
            f"{tent} tentativas - "
            f"{minutos:02}:{segundos:02}\n"
        )

    messagebox.showinfo("Ranking", texto)


def atualizar_labels():
    label_jogador.config(text=f"👤 Jogador: {nome_jogador}")
    label_vidas.config(text=f"❤️ Vidas: {vidas}")
    label_pontos.config(text=f"⭐ Pontos: {pontos}")
    label_tentativas.config(
        text=f"🎯 Tentativas: {tentativas}/{MAX_TENTATIVAS}"
    )


def atualizar_tempo():
    if pares_encontrados < 8:
        seg = int(time.time() - inicio)
        minutos = seg // 60
        segundos = seg % 60
        label_tempo.config(
            text=f"⏱️ Tempo: {minutos:02}:{segundos:02}"
        )
        janela.after(1000, atualizar_tempo)


def venceu():
    tempo = int(time.time() - inicio)
    salvar_ranking(nome_jogador, tentativas, tempo)

    minutos = tempo // 60
    segundos = tempo % 60

    messagebox.showinfo(
        "Vitória",
        f"🎉 Parabéns, {nome_jogador}!\n\n"
        f"⭐ Pontos: {pontos}\n"
        f"🎯 Tentativas: {tentativas}\n"
        f"⏱️ Tempo: {minutos:02}:{segundos:02}"
    )


def verificar():
    global primeira, segunda, travado
    global vidas, pontos, tentativas, pares_encontrados

    i = primeira
    j = segunda

    tentativas += 1

    if cartas[i] == cartas[j]:
        botoes[i].config(text=cartas[i], state="disabled")
        botoes[j].config(text=cartas[j], state="disabled")
        pontos += 100
        pares_encontrados += 1
    else:
        vidas -= 1
        pontos = max(0, pontos - 20)
        botoes[i].config(text="❓")
        botoes[j].config(text="❓")

    atualizar_labels()

    primeira = None
    segunda = None
    travado = False

    if tentativas >= MAX_TENTATIVAS and pares_encontrados < 8:
        messagebox.showinfo(
            "Fim de Jogo",
            f"💀 {nome_jogador}, você usou as "
            f"{MAX_TENTATIVAS} tentativas!"
        )
        reiniciar()
        return

    if vidas <= 0:
        messagebox.showinfo("Game Over", "💀 Você perdeu todas as vidas!")
        reiniciar()
        return

    if pares_encontrados == 8:
        venceu()


def clicar(indice):
    global primeira, segunda, travado

    if travado:
        return

    if botoes[indice]["state"] == "disabled":
        return

    if indice == primeira:
        return

    botoes[indice].config(text=cartas[indice])

    if primeira is None:
        primeira = indice
    else:
        segunda = indice
        travado = True
        janela.after(700, verificar)


def reiniciar():
    global cartas, vidas, pontos
    global tentativas, pares_encontrados
    global primeira, segunda
    global inicio, nome_jogador

    nome = simpledialog.askstring(
        "Jogador",
        "Digite seu nome:"
    )

    if nome:
        nome_jogador = nome

    cartas = EMOJIS.copy()
    random.shuffle(cartas)

    vidas = VIDAS_INICIAIS
    pontos = 0
    tentativas = 0
    pares_encontrados = 0
    primeira = None
    segunda = None

    for botao in botoes:
        botao.config(text="❓", state="normal")

    inicio = time.time()
    atualizar_labels()
    atualizar_tempo()


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

reiniciar()
janela.mainloop()
