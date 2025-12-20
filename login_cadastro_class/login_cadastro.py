import time
import variaveis_global
import db

class Cadastro_logic:

    def login_tela(self):
        print()
        print(f"{variaveis_global.bcolors.OKBLUE}=" * 40)
        print("\tTela de Login")
        print(f"=" * 40, f"{variaveis_global.bcolors.ENDC}")
        print()

    def cadastro_tela(self):
        print()
        print(f"{variaveis_global.bcolors.OKBLUE}=" * 40)
        print("\tTela de Cadastro de Usuário")
        print(f"=" * 40, f"{variaveis_global.bcolors.ENDC}")
        print()

    # Tela de Login
    def login(self):

        if variaveis_global.usuario_logado_index != -1:
            return variaveis_global.usuario_logado_index

        if len(db.usuarios) <= 0:
            print(f"{variaveis_global.bcolors.WARNING}Não há nenhum usuário cadastrado no sistema.{variaveis_global.bcolors.ENDC}")
            print(f"{variaveis_global.bcolors.WARNING}Por favor, cadastre um novo para acessar o sistema.{variaveis_global.bcolors.ENDC}")
            print()
            time.sleep(0.10)
            return -1

        self.login_tela()

        while True:
            input_usuario = input("Usuario: ")
            if input_usuario == variaveis_global.voltar_flair:
                return -1
            input_senha = input("Senha: ")
            if input_senha == variaveis_global.voltar_flair:
                return -1

            index = self.usuario_auth(input_usuario, input_senha)
            if index != -1:
                return index
            else:
                print(f"{variaveis_global.bcolors.FAIL}Login e/ou senha incorreto!{variaveis_global.bcolors.ENDC}")
                print()

    # Mover essa função para outro arquivo.
    def cadastro(self):

        usuario = {}
        cad_usuario = ""
        cad_senha = ""

        self.cadastro_tela()

        while True:
            cad_usuario = input("Insira seu usuario: ")
            cad_usuario = cad_usuario.strip()
            if cad_usuario == variaveis_global.voltar_flair:
                return
            elif not self.nome_de_usuario_check(cad_usuario):
                continue
            elif self.usuario_existe(cad_usuario) != -1:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Já existe um usuário com esse nome de usuário.{variaveis_global.bcolors.ENDC}")
                print()
                continue

            while True:
                cad_senha = input("Insira a senha: ")
                if cad_senha == variaveis_global.voltar_flair:
                    return
                if not self.senha_check(cad_senha):
                    continue
                cad_senha_nov = input("Insira a senha novamente: ")
                if cad_senha == variaveis_global.voltar_flair:
                    return
                if cad_senha_nov == cad_senha:
                    break
                else:
                    print(f"{variaveis_global.bcolors.FAIL}Erro: As senhas não coincidem, tente novamente.{variaveis_global.bcolors.ENDC}")
                    print()
            break

        usuario["usuario"] = cad_usuario
        usuario["senha"] = cad_senha

        db.usuarios.append(usuario.copy())
        usuario.clear()

        print(f"{variaveis_global.bcolors.OKGREEN}Sucesso: Usuário cadastrado{variaveis_global.bcolors.ENDC}")
        print()
        time.sleep(1.5)

    def add_admin(self):
        db.usuarios.append({"usuario": variaveis_global.admin_usuario, "senha": variaveis_global.admin_senha})

    def usuario_existe(self, usr):

        for index, usuario in enumerate(db.usuarios):
            if usuario["usuario"] == usr:
                return index
        return -1

    def usuario_auth(self, usr, senha):

        for index, usuario in enumerate(db.usuarios):
            if usuario["usuario"] == usr and usuario["senha"] == senha:
                return index
        return -1

    def editar_nome_de_usuario(self, index: int, new_usr_name: str):
        try:
            if not self.nome_de_usuario_check(new_usr_name):
                return False
            db.usuarios[index]["usuario"] = new_usr_name
        except:
            print(f"{variaveis_global.bcolors.FAIL}Erro: Ocorreu um problema ao editar o nome de usuário. Por favor, entre em contato com os administradores para reportar o Bug.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        return True

    def editar_senha_de_usuario(self, index: int, old_usr_pass: str, new_usr_pass: str):

        if not old_usr_pass == db.usuarios[index]["senha"]:
            print(f"{variaveis_global.bcolors.FAIL}Senha incorreta.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        try:
            if not self.senha_check(new_usr_pass):
                return False
            db.usuarios[index]["senha"] = new_usr_pass
        except:
            print(f"{variaveis_global.bcolors.FAIL}Ocorreu um problema ao editar a senha de usuário. Por favor, entre em contato com os administradores para reportar o Bug.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        return True

    def nome_de_usuario_check(self, nome_de_usuario: str):

        if nome_de_usuario.isnumeric():
            print(f"{variaveis_global.bcolors.FAIL}Erro: Usuario não deve conter apenas números.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        elif nome_de_usuario.isspace():
            print(f"{variaveis_global.bcolors.FAIL}Erro: Usuario não deve conter apenas espaços.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        elif not ((len(nome_de_usuario) > 3) and (len(nome_de_usuario) <= 64)):
            print(f"{variaveis_global.bcolors.FAIL}Erro: Usuário deve conter, pelo menos, entre 4 à 64 caracteres.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        return True

    def senha_check(self, senha: str):

        if " " in senha:
            print(f"{variaveis_global.bcolors.FAIL}Erro: Não deve conter espaço em senha.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        elif not ((len(senha) > 5) and (len(senha) <= 64)):
            print(f"{variaveis_global.bcolors.FAIL}Erro: senha deve conter, pelo menos, entre 6 à 64 caracteres.{variaveis_global.bcolors.ENDC}")
            print()
            return False
        return True

    # Função que pega argumento como index ou nome de usuario, e retorna index correspondente do usuario
    def selecione_usuario(self, argumento: str):
        if argumento.isnumeric():
            argumento = int(argumento)
            if (argumento >= 0) and (argumento < len(db.usuarios)):
                return argumento
            else:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Selecione um index entre '0' até \'{len(db.usuarios)}\'.{variaveis_global.bcolors.ENDC}")
                print()
        elif argumento.isalnum():
            argumento_temp = argumento
            argumento = int(self.usuario_existe(argumento))
            if argumento != -1:
                return argumento
            else:
                print(f"{variaveis_global.bcolors.FAIL}Erro: Não foi encontrado o usuario \'{argumento_temp}\'.{variaveis_global.bcolors.ENDC}")
                print()
        return -1

    def deletar_usuario(self, index: int):
        try:
            db.usuarios.pop(index)
        except:
            return False
        return True

    def usuario_e_adm(self, index: int):

        if index == 0 and db.usuarios[index]["usuario"] == variaveis_global.admin_usuario:
            return True
        else:
            return False