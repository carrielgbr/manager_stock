import db
import variaveis_global
import time

class screen_produto:

    def __init__(self):
        self.produtos = []  # Inicializa a lista de produtos

    def tela_produto(self):
        print(f"{variaveis_global.bcolors.OKBLUE}=" * 40)
        print("TELA DE GERENCIAMENTO DE PRODUTOS")
        print(f"=" * 40, f"{variaveis_global.bcolors.ENDC}")
        print()

    def menu_produto(self):
        acoes = ['Adicionar Produto', 'Remover Produto', 'Editar Produto', 'Ver Produtos' ,'Voltar']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")

    def tela_produto_home(self):
        self.tela_produto()

        while True:

            self.menu_produto()
            enter_produto = input(">>: ")
            enter_produto = enter_produto.lower()

            if enter_produto in ["0", "adicionar"]:
                self.adicionar_produto(self)
            elif enter_produto in ["1", "remover"]:
                self.remover_produto()
            elif enter_produto in ["2", "editar"]:
                print("editar")
            elif enter_produto in ["3", "ver"]:
                self.ver_produtos()
            elif enter_produto in ["4", "voltar"]:
                return
            else:
                print(f"{variaveis_global.bcolors.FAIL}Ação inválida, tente novamente.{variaveis_global.bcolors.ENDC}")
                print()

            
    def adicionar_produto(self, produtos):

        while True:
            nome = input("Insira o nome do produto [voltar]: ")
            nome = nome.strip()

            if nome == variaveis_global.voltar_flair:
                return

            if len(nome) == 0:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Nome do produto não deve ser vazio!{variaveis_global.bcolors.ENDC}")
                print()
                continue

            if self.produto_existe(nome) != -1:
                print(f"{variaveis_global.bcolors.FAIL}Produto já está cadastrado no sistema.{variaveis_global.bcolors.ENDC}")
                print()
                continue
            break

        while True:
            try:
                preco = float(input("Insira o preço do produto: R$ "))
                break
            except:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Preço deve ser um valor numérico.{variaveis_global.bcolors.ENDC}")
                print()

        while True:
            try:
                quantidade = int(input("Insira a quantidade em estoque: "))
                break
            except:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Quantidade deve ser um valor numérico.{variaveis_global.bcolors.ENDC}")
                print()

        while True:
            fornecedor = input("Insira o nome do fornecedor: ")
            fornecedor = fornecedor.strip()

            if len(fornecedor) == 0:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Nome do fornecedor não deve ser vazio!{variaveis_global.bcolors.ENDC}")
                print()
                continue
            break

        while True:
            descricao = input("Insira a descrição do produto: ")
            descricao = descricao.strip()

            if len(descricao) == 0:
                print(f"{variaveis_global.bcolors.FAIL}Erro: A descrição não deve ser vazia!{variaveis_global.bcolors.ENDC}")
                print()
                continue
            break

        db.produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "fornecedor": fornecedor,
            "descricao": descricao
        })

        print(f"{variaveis_global.bcolors.OKGREEN}{nome} cadastrado com sucesso!{variaveis_global.bcolors.ENDC}")
        print()

    def remover_produto(self):
        if not db.produtos:
            print(f"{variaveis_global.bcolors.WARNING}Nenhum produto cadastrado.{variaveis_global.bcolors.ENDC}")
            print()
            return

        self.lista_produtos()
        produto_remover = input("Insira o nome ou index do produto a ser removido: ")
        produto_remover = self.selecione_produto(produto_remover)

        if produto_remover == -1:
            return

        nome_produto = db.produtos[produto_remover]["nome"]

        continuar = input(f"Você tem certeza que deseja remover o produto \'{nome_produto}\'?[s/n] ")
        if continuar.lower() != 's':
            return

        try:
            db.produtos.pop(produto_remover)
        except:
            print(f"{variaveis_global.bcolors.FAIL}Ocorreu um erro ao tentar excluir o produto \'{nome_produto}\'. Por favor, entre em contato com os administradores para reportar o Bug.{variaveis_global.bcolors.ENDC}")
            print()


    def ver_produtos(self):
        self.lista_produtos()
        continuar = input("Aperte Enter para continuar...")
        print()

    def produto_existe(self, nome: str):
        for index, produto in enumerate(db.produtos):
            if produto["nome"] == nome:
                return index
        return -1


    def lista_produtos(self):
        if not db.produtos:
            print(f"{variaveis_global.bcolors.WARNING}Nenhum produto cadastrado.{variaveis_global.bcolors.ENDC}")
            print()
            return

        print(f"{variaveis_global.bcolors.OKBLUE}--- Produtos cadastrados ---{variaveis_global.bcolors.ENDC}")
        for index, produto in enumerate(db.produtos):
            print(f"{index}:\tNome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Fornecedor: {produto['fornecedor']}, Descrição: {produto['descricao']}")
        print()

    def selecione_produto(self, argumento: str):
        if argumento.isnumeric():
            argumento = int(argumento)
            if (argumento >= 0) and (argumento < len(db.produtos)):
                return argumento
            else:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Selecione um index entre '0' até \'{len(db.produtos)}\'.{variaveis_global.bcolors.ENDC}")
                print()
        elif argumento.isalnum():
            argumento_temp = argumento
            argumento = int(self.produto_existe(argumento))
            if argumento != -1:
                return argumento
            else:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Não foi encontrado o produto \'{argumento_temp}\'.{variaveis_global.bcolors.ENDC}")
                print()
        return -1