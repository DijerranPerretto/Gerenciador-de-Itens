import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os itens e suas localizações
itens = {}

# Função para armazenar itens em um ficheiro
def armazenar_itens_em_ficheiro():
    with open("itens_cadastrados.txt", "w") as file:
        for nome, localizacao in itens.items():
            file.write(f"{nome},{localizacao}\n")
    print("Itens armazenados com sucesso no ficheiro 'itens_cadastrados.txt'")

# Função para cadastrar item e armazenar no ficheiro
def cadastrar_item():
    nome = entry_nome.get().strip()
    localizacao = entry_localizacao.get().strip()

    if not nome or not localizacao:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    # Verifica se o item já existe com o mesmo nome e localização
    if nome in itens and itens[nome] == localizacao:
        messagebox.showwarning("Aviso", f"O item '{nome}' já está cadastrado com essa localização.")
    else:
        itens[nome] = localizacao
        messagebox.showinfo("Sucesso", f"Item '{nome}' cadastrado com sucesso!")
        # Após o cadastro, armazena os itens no ficheiro
        armazenar_itens_em_ficheiro()
        entry_nome.delete(0, tk.END)
        entry_localizacao.delete(0, tk.END)


# Função para excluir um item pelo nome
def excluir_item(nome):
    if nome in itens:
        del itens[nome]
        print(f"Item '{nome}' foi excluído com sucesso.")
    else:
        print(f"O item '{nome}' não foi encontrado.")

# Função para procurar item
def procurar_item():
    nome = entry_nome_procurar.get().strip()

    if nome in itens:
        messagebox.showinfo("Item Encontrado", f"O item '{nome}' está localizado em: {itens[nome]}")
    else:
        messagebox.showwarning("Não encontrado", f"O item '{nome}' não foi encontrado.")

# Função para listar itens em ordem alfabética
def listar_itens():
    if itens:
        lista_ordenada = "\n".join(f"{nome}: {itens[nome]}" for nome in sorted(itens))
        messagebox.showinfo("Itens Cadastrados", f"Itens cadastrados:\n{lista_ordenada}")
    else:
        messagebox.showinfo("Nenhum Item", "Não há itens cadastrados.")

# Janela principal
janela = tk.Tk()
janela.title("Gerenciador de Itens")
janela.geometry("500x500")

# Frame para Cadastrar item
frame_cadastro = tk.Frame(janela)
frame_cadastro.pack(pady=10)

label_titulo = tk.Label(frame_cadastro, text="Cadastrar Item", font=("Arial", 14))
label_titulo.grid(row=0, columnspan=2)

label_nome = tk.Label(frame_cadastro, text="Nome do Item:")
label_nome.grid(row=1, column=0, padx=5, pady=5)

entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

label_localizacao = tk.Label(frame_cadastro, text="Localização:")
label_localizacao.grid(row=2, column=0, padx=5, pady=5)

entry_localizacao = tk.Entry(frame_cadastro)
entry_localizacao.grid(row=2, column=1, padx=5, pady=5)

btn_cadastrar = tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar_item)
btn_cadastrar.grid(row=3, columnspan=2, pady=10)

# Frame para Procurar item
frame_procurar = tk.Frame(janela)
frame_procurar.pack(pady=10)

label_procurar = tk.Label(frame_procurar, text="Procurar Item", font=("Arial", 14))
label_procurar.grid(row=0, columnspan=2)

label_nome_procurar = tk.Label(frame_procurar, text="Nome do Item:")
label_nome_procurar.grid(row=1, column=0, padx=5, pady=5)

entry_nome_procurar = tk.Entry(frame_procurar)
entry_nome_procurar.grid(row=1, column=1, padx=5, pady=5)

btn_procurar = tk.Button(frame_procurar, text="Procurar", command=procurar_item)
btn_procurar.grid(row=2, columnspan=2, pady=10)

# Frame para Listar itens
frame_listar = tk.Frame(janela)
frame_listar.pack(pady=10)

btn_listar = tk.Button(frame_listar, text="Listar Itens (Alfabética)", command=listar_itens)
btn_listar.pack()

# Frame para Excluir item
frame_excluir = tk.Frame(janela)
frame_excluir.pack(pady=10)

label_excluir = tk.Label(frame_excluir, text="Excluir Item", font=("Arial", 14))
label_excluir.grid(row=0, columnspan=2)

label_nome_excluir = tk.Label(frame_excluir, text="Nome do Item:")
label_nome_excluir.grid(row=1, column=0, padx=5, pady=5)

entry_nome_excluir = tk.Entry(frame_excluir)
entry_nome_excluir.grid(row=1, column=1, padx=5, pady=5)

def excluir_item_ui():
    nome = entry_nome_excluir.get().strip()
    if nome in itens:
        excluir_item(nome)
        messagebox.showinfo("Sucesso", f"O item '{nome}' foi excluído.")
        entry_nome_excluir.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", f"O item '{nome}' não foi encontrado.")

btn_excluir = tk.Button(frame_excluir, text="Excluir", command=excluir_item_ui)
btn_excluir.grid(row=2, columnspan=2, pady=10)

# Iniciar a janela
janela.mainloop()
