# src/produto.py

class Produto:
    """
    Representa um produto no inventário.
    """
    def __init__(self, nome, codigo, quantidade, preco):
        """
        Inicializa uma nova instância de Produto.
        """
        self.nome = nome
        self.codigo = codigo
        self.quantidade = int(quantidade)  # Garante que seja um número inteiro
        self.preco = float(preco)  # Garante que seja um número decimal

    def para_csv(self):
        """
        Retorna os dados do produto como uma string formatada para CSV.
        """
        return f"{self.nome},{self.codigo},{self.quantidade},{self.preco}"