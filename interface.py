import customtkinter as ctk
import tkinter.messagebox as msgbox
from estoque import *
from produto import * 
import csv
import tkinter.filedialog as fd

# Janela
def rodar_app():
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
    tabs.add("Sobre")

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


    # Conteúdo da aba "Sobre"
    texto_sobre = (
        "📦 Sistema Controle de Estoque v1.0\n\n"
        "Desenvolvido por: Gabriel Brito\n"
        "Versão: 1.0\n"
        "Data: Agosto/2025\n\n"
        "Este sistema permite gerenciar o estoque de produtos\n"
        "de forma simples e eficiente, com interface moderna.\n\n"
        "Tecnologias usadas:\n"
        "- Python\n"
        "- CustomTkinter\n"
        "- JSON para armazenamento"
    )

    label_sobre = ctk.CTkLabel(tabs.tab("Sobre"), text=texto_sobre, justify="left", font=ctk.CTkFont(size=14))
    label_sobre.pack(padx=20, pady=20, anchor="center")


    # Conteúdo aba "Acessar Estoque"
    def listar_produtos():
        estoque = Estoque()
        texto_produtos = estoque.listar_todos()

        caixa_lista.delete("1.0", "end")  # limpa o conteúdo anterior
        caixa_lista.insert("end", texto_produtos)  # insere o novo conteúdo

        
    # Área de texto para mostrar os produtos
    caixa_lista = ctk.CTkTextbox(master=tabs.tab("Acessar Estoque"), width=400, height=300)
    caixa_lista.grid(row=1, column=0, padx=10, pady=5)

    # Botão de acesso a listar produtos
    button_listar = ctk.CTkButton(master=tabs.tab("Acessar Estoque"), command=listar_produtos, text="Listar Produtos")
    button_listar.grid(row=0, column=0, padx=10, pady=5)


    # Área Editar produto

    def abrir_nova():
        nova = ctk.CTkToplevel(janela)
        nova.title("Editar Produto")
        nova.geometry("300x200")
        nova.lift()  # Traz para frente
        nova.attributes('-topmost', True)  # Mantém por cima
        nova.after(100, lambda: nova.attributes('-topmost', False))  # Remove o "sempre por cima"

        nova.lift()
        nova.attributes('-topmost', True)
        nova.after(100, lambda: nova.attributes('-topmost', False))

        # Campos da nova janela
        label_produto = ctk.CTkLabel(nova, text="Produto")
        label_produto.grid(row=0, column=0, padx=10, pady=5)
        entry_produto = ctk.CTkEntry(nova, placeholder_text="Digite o Produto")
        entry_produto.grid(row=0, column=1, padx=10, pady=5)

        label_preco = ctk.CTkLabel(nova, text="Novo Preço (R$)")
        label_preco.grid(row=1, column=0, padx=10, pady=5)
        entry_preco = ctk.CTkEntry(nova, placeholder_text="0.00")
        entry_preco.grid(row=1, column=1, padx=10, pady=5)

        label_qtd = ctk.CTkLabel(nova, text="Nova Quantidade")
        label_qtd.grid(row=2, column=0, padx=10, pady=5)
        entry_qtd = ctk.CTkEntry(nova, placeholder_text="0")
        entry_qtd.grid(row=2, column=1, padx=10, pady=5)


        def salvar_alteracao():
            produto = entry_produto.get().title().strip()
            try:
                novo_preco = float(entry_preco.get())
                nova_qtd = int(entry_qtd.get())
            except ValueError:
                msgbox.showerror("Erro", "Preço ou quantidade inválidos!")
                return

            estoque = Estoque()

            # Carregar dados para verificar se o produto existe
            dados = carregar_json(str(path))
            encontrado = False
            for prod in dados:
                if prod['nome'] == produto:
                    encontrado = True
                    break

            if not encontrado:
                msgbox.showerror("Produto não encontrado", f"O produto '{produto}' não está no estoque.")
                return

            # Atualizar o estoque
            estoque.atualizar_estoque(produto, novo_preco, nova_qtd)
            msgbox.showinfo("Sucesso", f"Produto '{produto}' atualizado com sucesso!")
            nova.destroy()

        botao_salvar = ctk.CTkButton(nova, text="Salvar", command=salvar_alteracao)
        botao_salvar.grid(row=3, column=0, columnspan=2, pady=10)

    button_editar = ctk.CTkButton(master=tabs.tab("Acessar Estoque"), command=abrir_nova, text="Editar Produto")
    button_editar.grid(row=0, column=1, padx=10, pady=5)


    # Exportar CSV
    def exportar_csv():
        # Abre janela para escolher local e nome do arquivo
        caminho = fd.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivos CSV", "*.csv")],
            initialfile="estoque_produto.csv",
            title="Salvar arquivo CSV"
        )

        if not caminho:  # Se o usuário cancelar
            return

        dados = carregar_json(str(path))
        if not dados:
            msgbox.showerror("Erro", "Estoque vazio, nada para exportar!")
            return

        # Escreve CSV no caminho escolhido
        with open(caminho, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Preço", "Quantidade"])
            for prod in dados:
                writer.writerow([prod["nome"], prod["preco"], prod["quantidade"]])

        msgbox.showinfo("Sucesso", f"Arquivo '{caminho}' exportado com sucesso!")
    
    # Botão Exportar CSV
    button_exportar = ctk.CTkButton(master=tabs.tab("Acessar Estoque"), command=exportar_csv, text="Exportar (CSV)")
    button_exportar.grid(row=0, column=2, padx=10, pady=5)


    janela.mainloop()

