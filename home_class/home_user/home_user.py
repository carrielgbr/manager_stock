
import db
import variaveis_global
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
        if not db.usuarios:  # Verifica se a lista de usuários está vazia
            print("Nenhum usuário cadastrado.")
        else:
            print("Usuários cadastrados:")
            for index, usuario in enumerate(db.usuarios):
                print(f"{index} -\t{usuario['usuario']}")  # Mostra somente o usuario
        # Opção para voltar ao menu
        input("\nPressione Enter para voltar ao menu...")

    def editar_usuario(self):

        usrs_class = Cadastro_logic()
        selecionado = -1
        nome_de_usuario = ""

        print("\n--- Editar Usuário ---")
        if not db.usuarios:
            print("Nenhum usuário cadastrado para editar.")
            return
        if db.usuarios :  # Verifica se há usuários cadastrados
            while True:
                print()
                print("Usuarios:")
                for index, usuario in enumerate(db.usuarios):
                    print(f"{index} -\t{usuario['usuario']}")
                try:
                    selecionado = input("Selecione o Index do usuario para editar: ")
                    if selecionado == variaveis_global.voltar_flair:
                        return
                    if selecionado.isalpha():
                        selecionado_temp = selecionado
                        selecionado = int(usrs_class.usuario_existe(selecionado))
                        if selecionado != -1:
                            break
                        else:
                            print(f"Não foi encontrado o usuario \'{selecionado_temp}\'.")
                    elif selecionado.isnumeric():
                        selecionado = int(selecionado)
                        if (selecionado >= 0) and (selecionado < len(db.usuarios)):
                            break
                        else:
                            print(f"Selecione um index entre '0' até \'{len(db.usuarios)}\'.")
                except:
                    print("Digite o \'index\' ou o \'nome de usuario\' para editar.")

            nome_de_usuario = db.usuarios[selecionado]["usuario"]
            while True:
                print()
                print(f"Usuario \'{nome_de_usuario}\' selecionado.")
                print("0 - Editar usuário")
                print("1 - Editar senha")
                print("2 - voltar")
                acao = input("Selecione o Index: ")
                if acao in ["2", variaveis_global.voltar_flair]:
                    return
                elif acao == "0":
                    novo_nome_de_usuario = input(f"Novo nome de usuário para \'{nome_de_usuario}\': ")
                    novo_nome_de_usuario.strip()
                    if usrs_class.usuario_existe(novo_nome_de_usuario) == -1:
                        if not usrs_class.editar_nome_de_usuario(selecionado, novo_nome_de_usuario):
                            print(f"Não foi possível editar o nome de usuario do \'{nome_de_usuario}\'.")
                        else:
                            print(f"Sucesso: usuario \'{nome_de_usuario}\' foi alterado para \'{novo_nome_de_usuario}\'.")
                            nome_de_usuario = novo_nome_de_usuario
                    else:
                        print(f"O usuário \'{novo_nome_de_usuario}\' já existe.")
                    continue
                elif acao == "1":
                    auth_senha = input(f"Digite a senha atual: ")
                    if usrs_class.usuario_auth(nome_de_usuario, auth_senha) == -1:
                        print("Senha incorreta.")
                        continue
                    nova_senha = input(f"Digite a nova senha: ")
                    if not usrs_class.editar_senha_de_usuario(selecionado, auth_senha, nova_senha):
                        continue
                    print(f"Sucesso: a senha do usuário \'{nome_de_usuario}\' foi alterado.")
                else:
                    continue


    def deletar_usuario(self):
        print("\n--- Deletar Usuário ---")
        nome = input("Nome do usuário a deletar: ")
        print(f"Usuário {nome} deletado com sucesso!")