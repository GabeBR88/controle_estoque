class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    
    def to_dict(self):
        return {
            "nome" : self.nome,
            "preco" : self.preco,
            "quantidade" : self.quantidade
        }
    

    def __str__(self):
        return f"Nome: {self.nome} - Preço: R${self.preco:.2f} - Quantidade: {self.quantidade}"
    

