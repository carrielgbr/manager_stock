import time
from home_produto.screen_produto import screen_produto

produto_screen = screen_produto()

class screen_estoque:
    def __init__(self, produtos):
        self.produtos = produtos.produto_screen  # Recebe a lista de produtos existente

    def tela_estoque(self):
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE ESTOQUE")
        print("=" * 40)
        time.sleep(1)
        teste = input("Enter...")
        for produto in self.produtos:
                print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Fornecedor: {produto['fornecedor']}, descrição: {produto['descrição']}")
