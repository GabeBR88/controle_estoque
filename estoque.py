from utils import carregar_json, salvar_json
from pathlib import Path
import json
from produto import Produto

path = Path(r"E:\Workspace\Um treino por dia\AGOSTO\Projeto1\controle_estoque\data\estoque.json")

class Estoque:
    def __init__(self):
        self.lista_produtos = []


    def adicionar_produto(self, produto: Produto):
        dados = carregar_json(str(path)) 
        dados.append(produto.to_dict())
        salvar_json(str(path), dados)


    def remover_produto(self, produto):
        dados = carregar_json(str(path))
        for prod in dados:
            if prod['nome'] == produto:
                dados.remove(prod)
                break
        salvar_json(str(path), dados)


    def buscar_produto(self, produto):
        dados = carregar_json(str(path))
        for prod in dados:
            if prod['nome'] == produto:
                print(f"Produto: {prod['nome']}")
                print(f"Preço: R${prod['preco']}")
                print(f"Quantidade: {prod['quantidade']}")
                break
        else:
            print("Produto informado, não localizado em estoque!")


    def listar_todos(self):
        dados = carregar_json(str(path))
        for prod in dados:
            print(f"Produto: {prod['nome']}")
            print(f"Preço: R${prod['preco']}")
            print(f"Quantidade: {prod['quantidade']}\n")


    def atualizar_estoque(self, produto):
        dados = carregar_json(str(path))
        for prod in dados:
            if prod['nome'] == produto:
                novo_preco = float(input("Novo preço: R$"))
                nova_quantidade = int(input("Nova quantidade: "))
                prod['preco'] = novo_preco
                prod['quantidade'] = nova_quantidade
                break
        salvar_json(str(path), dados)


