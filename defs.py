from tkinter import messagebox


def mostrar_clima():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Atenção", "Digite o nome de uma cidade.")
        return

    dados = obter_dados_clima(cidade)

    if dados:
        nome = dados['name']
        clima = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        sensacao = dados['main']['feels_like']
        umidade = dados['main']['humidity']

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
