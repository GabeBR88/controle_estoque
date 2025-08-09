from utils import carregar_json, salvar_json
from pathlib import Path
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
        texto = ""
        for prod in dados:
            texto += f"Produto: {prod['nome']}\n"
            texto += f"Preço: R${prod['preco']}\n"
            texto += f"Quantidade: {prod['quantidade']}\n\n"
        return texto


    def atualizar_estoque(self, produto, novo_preco, nova_quantidade):
        dados = carregar_json(str(path))
        for prod in dados:
            if prod['nome'] == produto:
                prod['preco'] = novo_preco
                prod['quantidade'] = nova_quantidade
                break
        salvar_json(str(path), dados)


