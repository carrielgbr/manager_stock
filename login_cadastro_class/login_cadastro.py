import time
import variaveis_global
import db

class Cadastro_logic:

    def login_tela(self):
        print()
        print("*" * 40)
        print("\tTela de Login")
        print("*" * 40)
        print()

    # Tela de Login
    def login(self):

        if variaveis_global.usuario_logado_index != -1:
            return variaveis_global.usuario_logado_index

        if len(db.usuarios) <= 0:
            print("Não há nenhum usuário cadastrado no sistema.")
            print("Por favor, cadastre-se para acessar o sistema.")
            time.sleep(0.10)
            return -1

        while True:
            self.login_tela()
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
                print("Login e/ou senha incorreto!")

    # Mover essa função para outro arquivo.
    def cadastro(self):

        usuario = {}
        cad_usuario = ""
        cad_senha = ""

        while True:
            print()
            cad_usuario = input("Insira seu usuario: ")
            cad_usuario = cad_usuario.strip()
            if cad_usuario == variaveis_global.voltar_flair:
                return
            elif not self.nome_de_usuario_check(cad_usuario):
                continue
            elif self.usuario_existe(cad_usuario) != -1:
                print("Já existe um usuário com esse nome de usuário.")
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
                    print("As senhas não coincidem, tente novamente.")
            break

        usuario["usuario"] = cad_usuario
        usuario["senha"] = cad_senha

        db.usuarios.append(usuario.copy())
        usuario.clear()

        print("CADASTRADO COM SUCESSO;")
        time.sleep(1.5)

    def add_admin(self):
        db.usuarios.append({"usuario": "admin", "senha": "admin123"})

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
            print("Ocorreu um problema ao editar o nome de usuário. Por favor, entre em contato com os administradores para reportar o Bug.")
            return False
        return True

    def editar_senha_de_usuario(self, index: int, old_usr_pass: str, new_usr_pass: str):

        if not old_usr_pass == db.usuarios[index]["senha"]:
            print("Senha incorreta.")
            return False
        try:
            if not self.senha_check(new_usr_pass):
                return False
            db.usuarios[index]["senha"] = new_usr_pass
        except:
            print("Ocorreu um problema ao editar a senha de usuário. Por favor, entre em contato com os administradores para reportar o Bug.")
            return False
        return True

    def nome_de_usuario_check(self, nome_de_usuario: str):

        if nome_de_usuario.isnumeric():
            print("Erro: Usuario não deve conter apenas números.")
            return False
        elif nome_de_usuario.isspace():
            print("Erro: Usuario não deve conter apenas espaços.")
            return False
        elif not ((len(nome_de_usuario) > 3) and (len(nome_de_usuario) <= 64)):
            print("Erro: Usuário deve conter, pelo menos, entre 4 à 64 caracteres")
            return False
        return True

    def senha_check(self, senha: str):

        if " " in senha:
            print("Erro: Não deve conter espaço em senha.")
            return False
        elif not ((len(senha) > 5) and (len(senha) <= 64)):
            print("Erro: senha deve conter, pelo menos, entre 6 à 64 caracteres")
            return False
        return True

    # Função que pega argumento como index ou nome de usuario, e retorna index correspondente do usuario
    def selecione_usuario(self, argumento: str):
        if argumento.isnumeric():
            argumento = int(argumento)
            if (argumento >= 0) and (argumento < len(db.usuarios)):
                return argumento
            else:
                print(f"Selecione um index entre '0' até \'{len(db.usuarios)}\'.")
        elif argumento.isalnum():
            argumento_temp = argumento
            argumento = int(self.usuario_existe(argumento))
            if argumento != -1:
                return argumento
            else:
                print(f"Não foi encontrado o usuario \'{argumento_temp}\'.")
        return -1

    def deletar_usuario(self, index: int):
        try:
            db.usuarios.pop(index)
        except:
            return False
        return True
