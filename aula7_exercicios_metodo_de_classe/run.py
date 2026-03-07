class Loja:

    taxa = 1.15

    def __init__(self, valor_produto_bruto:float):
        self.valor_produto_bruto = valor_produto_bruto
    
    def consultar_valor_do_produto(self):
        valor_final = self.valor_produto_bruto * self.taxa
        print(f'O valor do produto é: {valor_final}')

    @classmethod
    def editar_taxa_do_produto(cls,valor:float):
        cls.taxa = valor

roupa = Loja(10)
roupa2 = Loja(10)
roupa.consultar_valor_do_produto()
roupa.editar_taxa_do_produto(2)
roupa.consultar_valor_do_produto()
roupa2.consultar_valor_do_produto() #Observa aqui que alterou o valor da taxa também para roupa 2, apesar do método ter sido chamado somente para roupa1. Pq é uma alteração de método de classe.