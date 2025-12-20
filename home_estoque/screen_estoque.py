import time
from home_produto.screen_produto import screen_produto

produto_screen = screen_produto()

class screen_estoque:
    def __init__(self, obj_produto):
        # Recebe o objeto que contém a lista de produtos
        self.obj_produto = obj_produto 

    def tela_estoque(self):
        print("=" * 40)
        print("TELA DE ESTOQUE")
        print("=" * 40)
        
        # Acessa a lista que está dentro do outro objeto
        lista_para_exibir = self.obj_produto.produtos
        
        if not lista_para_exibir:
            print("Nenhum produto cadastrado no estoque.")
        else:
            print("Produtos cadastrados:")
            for produto in lista_para_exibir:
                print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")