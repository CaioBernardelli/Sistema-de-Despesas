import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def carregar_despesas():
    if os.path.exists("despesas.json"):
        with open("despesas.json", "r") as file:
            return json.load(file)
    else:
        return []

def salvar_despesas(despesas):
    with open("despesas.json", "w") as file:
        json.dump(despesas, file, indent=2)

def adicionar_despesa(valor, categoria):
    global despesas
    despesas = carregar_despesas()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nova_despesa = {"valor": valor, "categoria": categoria, "data": data}
    despesas.append(nova_despesa)
    salvar_despesas(despesas)


def exibir_relatorio():
    relatorio.config(state=tk.NORMAL)  # Habilita a edição do widget Text
    relatorio.delete("1.0", tk.END)   # Limpa o conteúdo atual do widget Text

    if despesas:
        for despesa in despesas:
            relatorio.insert(tk.END, f"{despesa['data']} - {despesa['categoria']}: R$ {despesa['valor']}\n")
    else:
        relatorio.insert(tk.END, "Nenhuma despesa registrada.")

    relatorio.config(state=tk.DISABLED)  # Desabilita a edição do widget Tex
    
"""  
def exibir_categorias():
    relatorio.config(state=tk.NORMAL)  # Habilita a edição do widget Text
    relatorio.delete("1.0", tk.END)  
    categorias_pre_definidas = ["Alimentação", "Transporte", "Moradia", "Lazer", "Saúde", "Educação", "Outros"]
    for categoria in categorias_pre_definidas:
        relatorio.insert(tk.END, f"{categoria}\n")
    relatorio.config(state=tk.DISABLED)
"""

def exibir_categorias():
    relatorio.config(state=tk.NORMAL)  # Habilita a edição do widget Text
    relatorio.delete("1.0", tk.END)  
    categorias_pre_definidas = ["Alimentação", "Transporte", "Moradia", "Lazer", "Saúde", "Educação", "Outros"]
    for index, categoria in enumerate(categorias_pre_definidas, start=1):
        relatorio.insert(tk.END, f"{index}: {categoria}\n")
    relatorio.config(state=tk.DISABLED)


def adicionar_despesa_click():
    try:
        global despesas
        result_message.set("")  # Limpa a mensagem de erro
        valor = float(valor_entry.get())
        categoria = categoria_entry.get()
        adicionar_despesa(valor, categoria)
        result_message.set(f" Despesa  adicionada com sucesso ,Categoria {categoria} e Valor{valor} .")
        message_label.configure(foreground="black")
    except ValueError:
        result_message.set("Erro de Valor: Por favor, insira um valor válido.")
        message_label.configure(foreground="red")


def limpar_text():
    relatorio.config(state=tk.NORMAL)  # Habilita a edição do widget Text
    relatorio.delete("1.0", tk.END)   # Limpa o conteúdo do widget Text
    relatorio.config(state=tk.DISABLED)




def main():
    global despesas
    despesas = carregar_despesas()
    

    while True:
        print("\n===== Rastreador de Despesas =====")
        print("1. Adicionar Despesa")
        print("2. Exibir Relatório")
        print("3. Sair")

        escolha = input("Escolha uma opção (1/2/3): ")

        if escolha == "1":
            adicionar_despesa()
        elif escolha == "2":
            exibir_relatorio()
        elif escolha == "3":
            print("Saindo do Rastreador de Despesas. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


janela = tk.Tk()
janela.title("Rastreador de Despesas")

frame = ttk.Frame(janela, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

valor_label = ttk.Label(frame, text="Valor:")
valor_entry = ttk.Entry(frame)
categoria_label = ttk.Label(frame, text="Categoria:")
categoria_entry = ttk.Entry(frame)
adicionar_button = ttk.Button(frame, text="Adicionar Despesa", command=adicionar_despesa_click)
relatorio_label = ttk.Label(frame, text="Informações:")
relatorio = tk.Text(frame, height=10, width=40, wrap=tk.WORD, state=tk.DISABLED)

categoria_button = ttk.Button(frame, text="Categorias", command=exibir_categorias)
categoria_button.grid(row=5, column=0, columnspan=1, pady=10)

limpa_button = ttk.Button(frame, text="Limpar", command=limpar_text)
limpa_button.grid(row=5, column=2, columnspan=2, pady=(10))


result_message = tk.StringVar()
message_label = ttk.Label(frame, textvariable=result_message, foreground="black")
message_label.grid(column=1, row=3, sticky=(tk.W, tk.E))


valor_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
valor_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
categoria_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
categoria_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
adicionar_button.grid(row=2, column=0, columnspan=2, pady=10)
relatorio_label.grid(row=3, column=0, pady=5, sticky=tk.W)
relatorio.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

#  botão "Relatório"
relatorio_button = ttk.Button(frame, text="Relatório", command=exibir_relatorio)
relatorio_button.grid(row=5, column=0, columnspan=4, pady=10)

# Carregar despesas
despesas = carregar_despesas()

# Iniciar loop de eventos
janela.mainloop()