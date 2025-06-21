import tkinter as tk

def centralizar(janela, largura=400, altura=300):
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Programa principal
janela = tk.Tk()
janela.title("Metereologia")
centralizar(janela)
def estado_do_tempo:
    if sol:
        image:#uma imagem de sol
        bg.color: #amarelo

    elif nublado:
        image:  # uma imagem de nuvens
        bg.color:  # branco

janela.mainloop()