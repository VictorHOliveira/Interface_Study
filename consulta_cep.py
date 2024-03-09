import requests
from tkinter import *
from ttkthemes import *

background_color = "#3c3c3c"

def consultar_cep():
    obter_cep = cep.get()
    url = f'https://viacep.com.br/ws/{obter_cep}/json/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        dados_cep = resposta.json()
        
        if 'erro' not in dados_cep:
            lbl_cep.config(text=f"CEP: {dados_cep['cep']}")
            lbl_logradouro.config(text=f"Logradouro: {dados_cep['logradouro']}")
            lbl_complemento.config(text=f"Complemento: {dados_cep.get('complemento', '')}")
            lbl_bairro.config(text=f"Bairro: {dados_cep['bairro']}")
            lbl_cidade.config(text=f"Cidade: {dados_cep['localidade']}")
            lbl_estado.config(text=f"Estado: {dados_cep['uf']}")
        else:
            limpar_rotulos()
            lbl_cep.config(text=f"Erro: {dados_cep['erro']}")

    except requests.exceptions.HTTPError as errh:
        return {'erro': f'HTTP Error: {errh}'}
    except requests.exceptions.ConnectionError as errc:
        return {'erro': f'Error Connecting: {errc}'}
    except requests.exceptions.Timeout as errt:
        return {'erro': f'Timeout Error: {errt}'}
    except requests.exceptions.RequestException as err:
        return {'erro': f'Request Error: {err}'}


def limpar_rotulos():
    # Limpa os rótulos
    lbl_cep.config(text="")
    lbl_logradouro.config(text="")
    lbl_complemento.config(text="")
    lbl_bairro.config(text="")
    lbl_cidade.config(text="")
    lbl_estado.config(text="")

janela = ThemedTk(theme="radiance")
janela.title("Consulta CEP")
janela.geometry("800x600")
janela.configure(bg=background_color)

text_title = Label(janela, text="Digite o CEP que deseja encontrar:", bg=background_color, fg="white", padx=5, pady=5)
text_title.pack()

cep = StringVar()
entry_cep = Entry(janela, textvariable=cep, font=("Arial", 14))
entry_cep.pack(pady=10)

botao = Button(janela, text="Search", command=consultar_cep, bg="#8c8c8c", fg="white")
botao.pack()

lbl_cep = Label(janela, text="", bg=background_color, fg="white", padx=5, pady=5)
lbl_cep.pack()

lbl_logradouro = Label(janela, text="", bg=background_color, fg="white", padx=5, pady=5)
lbl_logradouro.pack()

lbl_complemento = Label(janela, text="", bg=background_color, fg="white", padx=5, pady=5)
lbl_complemento.pack()

lbl_bairro = Label(janela, text="", bg=background_color, fg="white", padx=5, pady=5)
lbl_bairro.pack()

lbl_cidade = Label(janela, text="", bg=background_color, fg="white", padx=5, pady=5)
lbl_cidade.pack()

lbl_estado = Label(janela, text="", bg=background_color, fg="white", padx=5, pady=5)
lbl_estado.pack()

janela.mainloop()