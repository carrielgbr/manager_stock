class user_screen:
    
    def screen_print(self,print_result):
        print("Pesquisar Usuário")
        print("Cadastrar Usuário")

    def search_user(self):
        user_name = input("Digite o nome do usuário que deseja pesquisar: ")
        print(f"Pesquisando usuário: {user_name}")

    def register_user(self):   
        new_user_name = input("Digite o nome do novo usuário: ")
        print(f"Usuário {new_user_name} cadastrado com sucesso!")   