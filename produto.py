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
        return f"Produto: {self.nome} - R${self.preco} - Quantidade: {self.quantidade} - Salvo com sucesso!"
    

