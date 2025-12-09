class home_user_teste:
    
    def __init__(self, home_screen=None):
        self.home_screen = home_screen
    
    def fun_user(self):
        """Função para gerenciar usuários"""
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE USUÁRIOS")
        print("=" * 40)
        
        while True:
            print("\n1 - Adicionar Usuário")
            print("2 - Listar Usuários")
            print("3 - Editar Usuário")
            print("4 - Deletar Usuário")
            print("5 - Voltar")
            
            opcao = input("\nEscolha uma opção: >> ").lower()
            
            if opcao == '1' or opcao == 'adicionar':
                self.adicionar_usuario()
            elif opcao == '2' or opcao == 'listar':
                self.listar_usuarios()
            elif opcao == '3' or opcao == 'editar':
                self.editar_usuario()
            elif opcao == '4' or opcao == 'deletar':
                self.deletar_usuario()
            elif opcao == '5' or opcao == 'voltar':
                return
            else:
                print("Opção inválida!")
    
    def adicionar_usuario(self):
        print("\n--- Adicionar Usuário ---")
        nome = input("Nome: ")
        email = input("Email: ")
        print(f"Usuário {nome} ({email}) adicionado com sucesso!")
    
    def listar_usuarios(self):
        print("\n--- Listar Usuários ---")
        print("Usuários cadastrados no sistema...")
    
    def editar_usuario(self):
        print("\n--- Editar Usuário ---")
        nome = input("Nome do usuário a editar: ")
        print(f"Editando {nome}...")
    
    def deletar_usuario(self):
        print("\n--- Deletar Usuário ---")
        nome = input("Nome do usuário a deletar: ")
        print(f"Usuário {nome} deletado com sucesso!")