import requests
from tkinter import *
from ttkthemes import *

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
janela.title("Study Creation Interface!")
janela.configure(bg="#3c3c3c")

text_title = Label(janela, text="Digite o CEP que deseja encontrar:", padx=10, pady=10)
text_title.grid(column=0, row=0)

cep = StringVar()
entry_cep = Entry(janela, textvariable=cep)
entry_cep.grid(column=0, row=1)

botao = Button(janela, text="Search", command=consultar_cep, bg="#4CAF50", fg="white")
botao.grid(column=0, row=3)

lbl_cep = Label(janela, text="", bg="#3c3c3c", fg="white", padx=5, pady=5)
lbl_cep.grid(column=0, row=4)

lbl_logradouro = Label(janela, text="", bg="#3c3c3c", fg="white", padx=5, pady=5)
lbl_logradouro.grid(column=0, row=5)

lbl_complemento = Label(janela, text="", bg="#3c3c3c", fg="white", padx=5, pady=5)
lbl_complemento.grid(column=0, row=6)

lbl_bairro = Label(janela, text="", bg="#3c3c3c", fg="white", padx=5, pady=5)
lbl_bairro.grid(column=0, row=7)

lbl_cidade = Label(janela, text="", bg="#3c3c3c", fg="white", padx=5, pady=5)
lbl_cidade.grid(column=0, row=8)

lbl_estado = Label(janela, text="", bg="#3c3c3c", fg="white", padx=5, pady=5)
lbl_estado.grid(column=0, row=9)

janela.mainloop()