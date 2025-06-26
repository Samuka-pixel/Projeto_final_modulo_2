#as imagens utilizadas precisam de ser transferidas para a pasta onde está o código
import tkinter as tk
from tkinter import ttk

# Atualiza na janela o clima na cidade
def atualizar_cidade(clima):
    pass

def grid(janela,clima):
    janela.rowconfigure(0,weight= 1)
    janela.rowconfigure(1, weight=1)
    janela.rowconfigure(2, weight=1)
    janela.rowconfigure(3, weight=1)
    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)
    janela.columnconfigure(2, weight=1)
    janela.columnconfigure(3, weight=1)
    janela.columnconfigure(4, weight=1)
    janela.columnconfigure(5, weight=1)
    #temperatura maxima
    temp_max_txt = f"{clima.temp_max}º"
    temp_max_label=ttk.Label(janela, text=temp_max_txt, background= "pink")
    temp_max_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
    temp_max_label.config(font=("Times New Roman", 25))
    temp_max2_label = ttk.Label(janela, text="Temp. max.", background= "pink")
    temp_max2_label.grid(column=0, row=0, sticky=tk.SE, padx=5, pady=5)
    temp_max2_label.config(font=("Times New Roman", 15))
    #temperatura minima
    temp_min_txt = f"{clima.temp_min}º"
    temp_min_label=ttk.Label(janela, text=temp_min_txt, background= "pink")
    temp_min_label.grid(column=0, row=3, sticky=tk.NE, padx=5, pady=5)
    temp_min_label.config(font=("Times New Roman", 25))
    temp_min2_label = ttk.Label(janela, text="Temp. min.", background= "pink")
    temp_min2_label.grid(column=0, row=2, sticky=tk.SE, padx=5, pady=5)
    temp_min2_label.config(font=("Times New Roman", 15))
    #cidade
    cidade_label = ttk.Label(janela, text=clima.cidade, background= "pink")
    cidade_label.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)
    cidade_label.config(font=("Times New Roman", 25))
    #temperatura atual
    temp_atual_txt = f"{clima.temp_atual}º"
    temp_atual_label = ttk.Label(janela, text=temp_atual_txt, background= "pink")
    temp_atual_label.grid(column=2, row=2, sticky=tk.NE, padx=5, pady=5)
    temp_atual_label.config(font=("Times New Roman", 45))
    temp_atual2_label = ttk.Label(janela, text="Temp. atual", background= "pink")
    temp_atual2_label.grid(column=2, row=1, sticky=tk.SE, padx=5, pady=5)
    temp_atual2_label.config(font=("Times New Roman",15))
    #trocar cidades
    '''
    cidade_button = ttk.Label(janela, text="Trocar")
    cidade_button.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)
    cidade_button.config(font=("Times New Roman", 25))
    '''
    cidade_sel = tk.StringVar()
    cidades_cb = ttk.Combobox(janela, textvariable=cidade_sel)
    cidades_cb['values'] = list_cidades
    cidades_cb['state'] = 'readonly'
    cidades_cb.grid(column=2, row=3, sticky=tk.SW, padx=5, pady=5)
    #cidade_sel.set( "Lisboa" )
    cidades_txt = f"Trocar cidade:"
    cidades_label = ttk.Label(janela, text=cidades_txt, background= "pink")
    cidades_label.grid(column=0, row=3, sticky=tk.SE, padx=5, pady=5)
    cidades_label.config(font=("Times New Roman", 12))

    #estado de tempo
    estd_temp2_label = ttk.Label(janela, text="Estado do tempo", background= "pink")
    estd_temp2_label.grid(column=5, row=1, sticky="nse", padx=5, pady=5)
    estd_temp2_label.config(font=("Times New Roman", 15))

    if clima.estd_temp.lower() == "sol":
        imagem = tk.PhotoImage(file="sol.png").subsample(5, 5)
    elif clima.estd_temp.lower() == "nublado":
        imagem = tk.PhotoImage(file="nublado.png").subsample(5, 5)
    elif clima.estd_temp.lower() == "chuva":
        imagem = tk.PhotoImage(file="chuva.png").subsample(5, 5)
    elif clima.estd_temp.lower() == "neve":
        imagem = tk.PhotoImage(file="neve.png").subsample(2, 2)
    else:
        imagem = tk.PhotoImage(file="desconhecido.png").subsample(3, 3)

    estd_temp_label = tk.Label(
        janela,
        image=imagem,
        compound="left",
        bg="pink"
    )
    estd_temp_label.image = imagem  # manter referência
    estd_temp_label.grid(column=5, row=2, columnspan=2, sticky="NE", padx=5, pady=5)
    estd_temp_label.config(font=("Times New Roman", 25))


def centralizar(janela, largura=500, altura=330):
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


class CidadeClima:
    def __init__(self, cidade, temp_max, temp_min, temp_atual, estd_temp):
        self.cidade = cidade
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.temp_atual = temp_atual
        self.estd_temp = estd_temp
list_cidades=("Lisboa", "Porto", "Setúbal", "Beja", "Évora", "Faro", "Leiria", "Coimbra", "Aveiro", "Santarém",
              "Castelo Branco", "Viseu", "Guarda", "Bragança","Braga", "Viana do Castelo", "Vila Real","Paris",
              "Londres", "Berlim", "Madrid", "Roma", "Bruxelas", "Amesterdão", "Viena", "Praga", "Varsóvia",
              "Oslo", "Estocolmo", "Helsínquia", "Copenhaga", "Dublin", "Atenas", "Bucareste", "Sófia", "Belgrado",
              "Budapeste", "Bratislava", "Zagreb", "Sarajevo", "Skopje", "Podgorica", "Tirana", "Moscovo", "Kiev",
              "Minsk", "Washington", "Ottawa", "Cidade do México", "Brasília", "Buenos Aires", "Santiago", "Bogotá",
              "Lima", "Quito", "Caracas", "Montevideu", "Asunción", "La Paz", "Sucre", "Havana", "Santo Domingo",
              "San Juan", "Kingston", "Nassau", "Port-au-Prince", "Panamá", "San José", "Tegucigalpa", "Manágua",
              "Cidade da Guatemala", "Belmopan", "Port of Spain", "Paramaribo", "Georgetown", "Londres (Belize)",
              "Abuja", "Pretória", "Cidade do Cabo", "Bloemfontein", "Luanda", "Maputo", "Harare", "Nairobi",
              "Adis Abeba", "Dacar", "Bamaco", "Acra", "Lomé", "Abidjan", "Yaoundé", "Kinshasa", "Brazzaville",
              "Cairo", "Trípoli", "Tunes", "Rabat", "Argel", "Riade", "Doha", "Manama", "Abu Dhabi", "Mascate",
              "Sana", "Teerão", "Bagdad", "Damasco", "Amã", "Beirute", "Jerusalém", "Ancara", "Tóquio", "Pequim",
              "Seul", "Pyongyang", "Banguecoque", "Hanói", "Phnom Penh", "Vientiane", "Kuala Lumpur", "Jacarta",
              "Singapura", "Dili", "Camberra", "Wellington", "Port Moresby", "Suva", "Apia", "Nukuʻalofa", "Honiara",
              "Yaren", "Palikir", "Majuro", "Funafuti", "Tarawa", "Nouméa", "Nuuk")

janela = tk.Tk()
janela.title("Metereologia")
janela.configure(bg="pink")
#janela.
centralizar(janela)
climaLx = CidadeClima("Lisboa", 30, 25, 26, "Sol")
grid(janela, climaLx)

'''

climaPt = CidadeClima(25, 20, 21, "Porto", "Nublado")

print(climaLx.temp_atual)
print(climaPt.temp_atual)
'''

janela.mainloop()