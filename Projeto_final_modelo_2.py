import tkinter as tk
from tkinter import ttk, messagebox
import requests
print(requests.__version__)
# --- Chave da API ---
API_KEY = "6e175c0971b04da5a27132533252506"

# --- Função para obter dados da API ---
def obter_dados_clima(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&lang=pt"
    try:
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            return None
    except:
        return None

# --- Classe de clima ---
class CidadeClima:
    def __init__(self, cidade, temp_max, temp_min, temp_atual, estd_temp):
        self.cidade = cidade
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.temp_atual = temp_atual
        self.estd_temp = estd_temp

# --- Lista de cidades ---
list_cidades = ( "Lisboa", "Porto", "Setúbal", "Beja", "Évora", "Faro", "Leiria", "Coimbra", "Aveiro", "Santarém",
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
              "Yaren", "Palikir", "Majuro", "Funafuti", "Tarawa", "Nouméa", "Nuuk"
)

# --- Layout da Interface ---
def grid(janela, clima):
    for i in range(4):
        janela.rowconfigure(i, weight=1)
    for i in range(6):
        janela.columnconfigure(i, weight=1)

    ttk.Label(janela, text=f"{clima.temp_max}º", background="pink", font=("Times New Roman", 25)).grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
    ttk.Label(janela, text="Temp. max.", background="pink", font=("Times New Roman", 15)).grid(column=0, row=0, sticky=tk.SE, padx=5, pady=5)

    ttk.Label(janela, text=f"{clima.temp_min}º", background="pink", font=("Times New Roman", 25)).grid(column=0, row=3, sticky=tk.NE, padx=5, pady=5)
    ttk.Label(janela, text="Temp. min.", background="pink", font=("Times New Roman", 15)).grid(column=0, row=2, sticky=tk.SE, padx=5, pady=5)

    ttk.Label(janela, text=clima.cidade, background="pink", font=("Times New Roman", 25)).grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)
    ttk.Label(janela, text=f"{clima.temp_atual}º", background="pink", font=("Times New Roman", 45)).grid(column=2, row=2, sticky=tk.NE, padx=5, pady=5)
    ttk.Label(janela, text="Temp. atual", background="pink", font=("Times New Roman", 15)).grid(column=2, row=1, sticky=tk.SE, padx=5, pady=5)

    cidade_sel = tk.StringVar()
    cidades_cb = ttk.Combobox(janela, textvariable=cidade_sel, values=list_cidades, state='readonly')
    cidades_cb.grid(column=2, row=3, sticky=tk.SW, padx=5, pady=5)

    ttk.Label(janela, text="Trocar cidade:", background="pink", font=("Times New Roman", 12)).grid(column=0, row=3, sticky=tk.SE, padx=5, pady=5)

    ttk.Label(janela, text="Estado do tempo", background="pink", font=("Times New Roman", 15)).grid(column=5, row=1, sticky="nse", padx=5, pady=5)

    estado = clima.estd_temp.lower()

    # Podes trocar os ficheiros por imagens reais se existirem
    if "sol" in estado:
        imagem = tk.PhotoImage(file="sol.png").subsample(5, 5)
    elif "nublado" in estado:
        imagem = tk.PhotoImage(file="nublado.png").subsample(5, 5)
    elif "chuva" in estado:
        imagem = tk.PhotoImage(file="chuva.png").subsample(5, 5)
    elif "neve" in estado:
        imagem = tk.PhotoImage(file="neve.png").subsample(2, 2)
    else:
        imagem = tk.PhotoImage(file="desconhecido.png").subsample(3, 3)

    estd_temp_label = tk.Label(janela, image=imagem, compound="left", bg="pink")
    estd_temp_label.image = imagem
    estd_temp_label.grid(column=5, row=2, columnspan=2, sticky="NE", padx=5, pady=5)
    estd_temp_label.config(font=("Times New Roman", 25))

# --- Centralizar Janela ---
def centralizar(janela, largura=500, altura=330):
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# --- Mostrar Clima Simples ---
def mostrar_clima_simples():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Atenção", "Digite o nome de uma cidade.")
        return

    dados = obter_dados_clima(cidade)
    if dados:
        nome = dados['location']['name']
        clima = dados['current']['condition']['text']
        temperatura = dados['current']['temp_c']
        sensacao = dados['current']['feelslike_c']
        umidade = dados['current']['humidity']

        resultado = (
            f"Cidade: {nome}\n"
            f"Clima: {clima.capitalize()}\n"
            f"Temperatura: {temperatura}°C\n"
            f"Sensação térmica: {sensacao}°C\n"
            f"Umidade: {umidade}%"
        )
        label_resultado.config(text=resultado)
    else:
        messagebox.showerror("Erro", "Não foi possível obter os dados do clima.")

# --- Criar Janela ---
janela = tk.Tk()
janela.title("Meteorologia")
janela.configure(bg="pink")
centralizar(janela)

# Clima de exemplo inicial
clima_exemplo = CidadeClima("Lisboa", 30, 20, 25, "Sol")
grid(janela, clima_exemplo)

# Entrada e botão
entrada_cidade = tk.Entry(janela)
entrada_cidade.grid(row=4, column=2, padx=5, pady=5)

botao_teste = tk.Button(janela, text="Ver clima detalhado", command=mostrar_clima_simples)
botao_teste.grid(row=4, column=3, padx=5, pady=5)

label_resultado = tk.Label(janela, text="", bg="pink")
label_resultado.grid(row=5, column=0, columnspan=6)

janela.mainloop()
