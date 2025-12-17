class screen_produto:
    def tela_produto(self):
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE PRODUTOS")
        print("=" * 40)

    def menu_produto(self):
        acoes = ['Adicionar Produto', 'Remover Produto', 'Ver Produtos' ,'Voltar']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")

    def tela_produto(self):
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE PRODUTOS")
        print("=" * 40)
        print()
        import time
        time.sleep(1)

        while True:

            self.menu_produto()
            enter_produto = input(">> ")
            enter_produto = enter_produto.lower()

            if enter_produto == 'ver produtos':
                print(enter_produto, 'ver produtos')
            elif enter_produto == 'voltar':
                return
            elif enter_produto == 'adicionar produto':
                print(enter_produto, 'adicionar produto')
            elif enter_produto == 'remover produto':
                print(enter_produto, 'remover produto')

            else:
                print("Ação inválida, tente novamente.")
            # Additional functionality for 'Adicionar Produto' and 'Remover Produto' can be added here  

    def adicionar_produto():
        produtos = []
        nome = input("Insira o nome do produto: ")
        preco = float(input("Insira o preço do produto: R$ "))
        quantidade = int(input("Insira a quantidade em estoque: "))

    # Adiciona o produto à lista
        produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        })

        print(f"{nome} cadastrado com sucesso!")