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

            if enter_produto == 'ver produtos' or enter_produto == '2':
                enter_produto = self.ver_produtos()
            elif enter_produto == 'adicionar produto' or enter_produto == '0':
                enter_produto = self.adicionar_produto()
            elif enter_produto == 'remover produto' or enter_produto == '1':
                enter_produto = self.remover_produto()
            else:
                print("Ação inválida, tente novamente.")

    def adicionar_produto(self):
        produtos = []

        nome = input("Insira o nome do produto: ")
        preco = float(input("Insira o preço do produto: R$ "))
        quantidade = int(input("Insira a quantidade em estoque: "))

        produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        })

        print(f"{nome} cadastrado com sucesso!")

    def remover_produto(self, produtos):
        nome = input("Insira o nome do produto a ser removido: ")
        for produto in produtos:
            if produto["nome"] == nome:
                produtos.remove(produto)
                print(f"{nome} removido com sucesso!")
                return
            else:
                print(f"Produto {nome} não encontrado.")

    def ver_produtos(self, produtos):
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        print("Produtos cadastrados:")
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
