import customtkinter as ctk
import tkinter.messagebox as msgbox
from estoque import *
from produto import * 

# Janela
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.title("Sistema Controle de Estoque")
janela.geometry("854x480")


# Limite de redimensionamento
janela.maxsize(width=854, height=480)
janela.minsize(width=854, height=480)


# Abas (TABS)
tabs = ctk.CTkTabview(janela, width=0, corner_radius=30)
tabs.pack()

tabs.add("Cadastrar Produtos")
tabs.add("Acessar Estoque")


# Aba de cadastro
aba_cadastrar = tabs.tab("Cadastrar Produtos")


# Frame para organizar tudo com grid
label_titul = ctk.CTkLabel(master=tabs.tab("Cadastrar Produtos"), text="PREENCHA OS DADOS ABAIXO", font=("bold", 15)).pack()
form_frame = ctk.CTkFrame(master=aba_cadastrar, fg_color="transparent")
form_frame.pack(pady=30)



def coletar_produto():
    """Função responsável por coletar os dados dos produtos e enviar usando a classe Estoque"""
    produto_nome = entry_produto.get().title().strip()
    
    try:
        # Captura e conversão
        produto_preco = float(entry_preco.get().strip())  
        produto_quantidade = int(entry_quantidade.get().strip())  

        if not produto_nome or not produto_preco or not produto_quantidade:
            mensagem_falha_label.configure(text="Favor preencher todos os campos!")
        else:
            produto = Produto(produto_nome, produto_preco, produto_quantidade)
            estoque = Estoque()
            estoque.adicionar_produto(produto)

            # Limpar os campos
            for campo in (entry_produto, entry_preco, entry_quantidade):
                campo.delete(0, ctk.END)

            # Mostrar mensagem de sucesso
            mensagem_sucesso_label.configure(text="- Último produto cadastrado -\n" + str(produto))
            mensagem_falha_label.configure(text="")  # Limpa mensagem anterior

    except ValueError:
        mensagem_falha_label.configure(text="Erro: Preço deve ser número com ponto e quantidade número inteiro.")
        mensagem_sucesso_label.configure(text="")  # Limpa mensagem anterior


mensagem_sucesso_label = ctk.CTkLabel(master=aba_cadastrar, text="", text_color="green")
mensagem_sucesso_label.pack(pady=10)

mensagem_falha_label = ctk.CTkLabel(master=aba_cadastrar, text="", text_color="red")
mensagem_falha_label.pack(pady=10)


# === Linha 1: Produto ===
label_produto = ctk.CTkLabel(master=form_frame, text="Produto", width=100, anchor="w")
label_produto.grid(row=0, column=0, padx=10, pady=5)

entry_produto = ctk.CTkEntry(master=form_frame, placeholder_text="Digite o Produto", width=250)
entry_produto.grid(row=0, column=1, padx=10, pady=5)

# === Linha 2: Preço ===
label_preco = ctk.CTkLabel(master=form_frame, text="Preço", width=100, anchor="w")
label_preco.grid(row=1, column=0, padx=10, pady=5)

entry_preco = ctk.CTkEntry(master=form_frame, placeholder_text="Digite o Preço", width=250)
entry_preco.grid(row=1, column=1, padx=10, pady=5)

# === Linha 3: Quantidade ===
label_quantidade = ctk.CTkLabel(master=form_frame, text="Quantidade", width=100, anchor="w")
label_quantidade.grid(row=2, column=0, padx=10, pady=5)

entry_quantidade = ctk.CTkEntry(master=form_frame, placeholder_text="Digite a Quantidade", width=250)
entry_quantidade.grid(row=2, column=1, padx=10, pady=5)


# Button
button_enviar = ctk.CTkButton(master=tabs.tab("Cadastrar Produtos"), command=coletar_produto, text="Salvar").pack()




janela.mainloop()

