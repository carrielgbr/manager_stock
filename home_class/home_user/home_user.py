
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
        print()
        print(f"{variaveis_global.bcolors.OKBLUE}=" * 40)
        print("TELA DE GERENCIAMENTO DE USUÁRIOS")
        print(f"=" * 40, f"{variaveis_global.bcolors.ENDC}")

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
                print(f"{variaveis_global.bcolors.FAIL}Opção inválida!{variaveis_global.bcolors.ENDC}")
                print()
    
    def listar_usuarios(self):
        print(f"\n{variaveis_global.bcolors.OKBLUE}--- Listar Usuários ---{variaveis_global.bcolors.ENDC}")
        if not db.usuarios:  # Verifica se a lista de usuários está vazia
            print(f"{variaveis_global.bcolors.WARNING}Nenhum usuário cadastrado.{variaveis_global.bcolors.ENDC}")
            print()
        else:
            print("Usuários cadastrados:")
            for index, usuario in enumerate(db.usuarios):
                print(f"{index} -\t{usuario['usuario']}")  # Mostra somente o usuario
        # Opção para voltar ao menu
        input("\nPressione Enter para voltar ao menu...")
        print()

    def editar_usuario(self):

        usrs_class = Cadastro_logic()
        selecionado = -1
        nome_de_usuario = ""

        print(f"\n{variaveis_global.bcolors.OKBLUE}--- Editar Usuário ---{variaveis_global.bcolors.ENDC}")
        if not db.usuarios:
            print(f"{variaveis_global.bcolors.WARNING}Nenhum usuário cadastrado para editar.{variaveis_global.bcolors.ENDC}")
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
                    selecionado = usrs_class.selecione_usuario(selecionado)
                    if selecionado != -1:
                        break
                except:
                    print(f"{variaveis_global.bcolors.WARNING}Digite o \'index\' ou o \'nome de usuario\' para editar.{variaveis_global.bcolors.ENDC}")
                    print()

            if usrs_class.usuario_e_adm(selecionado):
                print(f"{variaveis_global.bcolors.FAIL}Erro: Não é possivel editar a conta do Administrador{variaveis_global.bcolors.ENDC}.")
                print()
                return

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
                            print(f"{variaveis_global.bcolors.FAIL}Não foi possível editar o nome de usuario do \'{nome_de_usuario}\'{variaveis_global.bcolors.ENDC}.")
                            print()
                        else:
                            print(f"{variaveis_global.bcolors.OKGREEN}Sucesso: usuario \'{nome_de_usuario}\' foi alterado para \'{novo_nome_de_usuario}\'.{variaveis_global.bcolors.ENDC}")
                            print()
                            nome_de_usuario = novo_nome_de_usuario
                    else:
                        print(f"{variaveis_global.bcolors.FAIL}O usuário \'{novo_nome_de_usuario}\' já existe.{variaveis_global.bcolors.ENDC}")
                        print()
                    continue
                elif acao == "1":
                    auth_senha = input(f"Digite a senha atual: ")
                    if usrs_class.usuario_auth(nome_de_usuario, auth_senha) == -1:
                        print(f"{variaveis_global.bcolors.FAIL}Senha incorreta.{variaveis_global.bcolors.ENDC}")
                        print()
                        continue
                    nova_senha = input(f"Digite a nova senha: ")
                    nova_senha_dnv = input(f"Digite a nova senha novamente:")
                    if nova_senha != nova_senha_dnv:
                        print(f"{variaveis_global.bcolors.FAIL}As duas senhas não são iguais.{variaveis_global.bcolors.ENDC}")
                        print()
                        continue
                    if not usrs_class.editar_senha_de_usuario(selecionado, auth_senha, nova_senha):
                        continue
                    print(f"{variaveis_global.bcolors.OKGREEN}Sucesso: a senha do usuário \'{nome_de_usuario}\' foi alterado.{variaveis_global.bcolors.ENDC}")
                    print()
                else:
                    continue


    def deletar_usuario(self):

        usrs_class = Cadastro_logic()

        print(f"\n{variaveis_global.bcolors.OKBLUE}--- Deletar Usuário ---{variaveis_global.bcolors.ENDC}")
        if not db.usuarios:
            print(f"{variaveis_global.bcolors.WARNING}Nenhum usuário cadastrado para deletar.{variaveis_global.bcolors.ENDC}")
            print()
            return
        if db.usuarios :  # Verifica se há usuários cadastrados
            while True:
                print()
                print("Usuarios:")
                for index, usuario in enumerate(db.usuarios):
                    print(f"{index} -\t{usuario['usuario']}")
                try:
                    usuario_deletar = input("Nome de usuário a deletar: ")
                    if usuario_deletar == variaveis_global.voltar_flair:
                        return
                    usuario_deletar = usrs_class.selecione_usuario(usuario_deletar)
                    if usuario_deletar != -1:
                        break
                except:
                    print(f"{variaveis_global.bcolors.WARNING}Digite o \'index\' ou o \'nome de usuario\' para excluir.{variaveis_global.bcolors.ENDC}")
                    print()

        if usrs_class.usuario_e_adm(usuario_deletar):
            print(f"{variaveis_global.bcolors.FAIL}Não é possivel excluir a conta do administrador.{variaveis_global.bcolors.ENDC}")
            print()
            return

        username = db.usuarios[usuario_deletar]["usuario"]

        while True:
            continuar = input(f"Deseja excluir o usuário \'{username}\' [s/n]? ")
            continuar = continuar.strip().lower()

            if continuar != 's':
                return
            else:
                break

        if usrs_class.deletar_usuario(usuario_deletar):
            print(f"{variaveis_global.bcolors.OKGREEN}Usuário \'{username}\' deletado com sucesso!{variaveis_global.bcolors.ENDC}")
            print()
        else:
            print(f"{variaveis_global.bcolors.FAIL}Não foi possível deletar o usuário \'{username}\'.{variaveis_global.bcolors.ENDC}")
            print()
