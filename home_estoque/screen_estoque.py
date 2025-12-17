import time

class screen_estoque:
    def tela_estoque(self):
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE ESTOQUE")
        print("=" * 40)


    def menu_estoque(self):
        acoes = ['Adicionar Produto', 'Remover Produto', 'Ver Estoque' ,'Voltar']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")

    def tela_estoque(self):
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE ESTOQUE")
        print("=" * 40)
        print()
        time.sleep(1)

        while True:

            self.menu_estoque()
            enter_estoque = input(">> ")
            enter_estoque = enter_estoque.lower()

            if enter_estoque == 'ver estoque':
                print(enter_estoque, 'ver estoque')
            elif enter_estoque == 'voltar':
                return
            
    def ver_estoque(self):
        print(enter_estoque, 'ver estoque')