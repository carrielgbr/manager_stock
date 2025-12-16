import sys
from login_cadastro_class.login_cadastro import Cadastro_logic

cadastro_login = Cadastro_logic()

class home_user_teste:
    
    def __init__(self, home_screen=None):
        self.home_screen = home_screen
    
    def tela_manager_home(self):
        acoes = ['LISTAR', 'EDITAR', 'DELETAR', 'VOLTAR']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")

    def fun_user(self):
        """Função para gerenciar usuários"""
        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE USUÁRIOS")
        print("=" * 40)
        
        while True:

            self.tela_manager_home()
            
            opcao = input("\nEscolha uma opção: >> ").lower()
            if opcao in ['0', 'listar']:
                self.listar_usuarios()
            elif opcao in ['1', 'editar']:
                self.editar_usuario()
            elif opcao in ['2', 'deletar']:
                self.deletar_usuario()
            elif opcao in ['3', 'voltar']:
                return
            else:
                print("Opção inválida!")
    
    def listar_usuarios(self):
         print("\n--- Listar Usuários ---")
    if not cadastro_login.usuarios:  # Verifica se a lista de usuários está vazia
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in cadastro_login.usuarios:
            print(f"- {usuario['email']}")  # Mostra somente o email

    # Opção para voltar ao menu
    input("\nPressione Enter para voltar ao menu...")

    def editar_usuario(self):
        print("\n--- Editar Usuário ---")
        nome = input("Nome do usuário a editar: ")
        print(f"Editando {nome}...")
    
    def deletar_usuario(self):
        print("\n--- Deletar Usuário ---")
        nome = input("Nome do usuário a deletar: ")
        print(f"Usuário {nome} deletado com sucesso!")