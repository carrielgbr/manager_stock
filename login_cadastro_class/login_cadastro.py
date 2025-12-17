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
            input_email = input("E-mail: ")
            if input_email == variaveis_global.voltar_flair:
                return -1
            input_senha = input("Senha: ")
            if input_senha == variaveis_global.voltar_flair:
                return -1

            index = self.usuario_auth(input_email, input_senha)
            if index != -1:
                return index
            else:
                print("Login e/ou senha incorreto!")

    # Mover essa função para outro arquivo.
    def cadastro(self):

        usuario = {}
        cad_email = ""
        cad_senha = ""

        while True:
            cad_email = input("Insira seu Email: ")
            if cad_email == variaveis_global.voltar_flair:
                return
            elif not self.usuario_existe(cad_email):
                print("Já existe um usuário com esse email.")
                continue

            while True:
                cad_senha = input("Insira a senha: ")
                if cad_senha == variaveis_global.voltar_flair:
                    return
                cad_senha_nov = input("Insira a senha novamente: ")
                if cad_senha == variaveis_global.voltar_flair:
                    return
                if cad_senha_nov == cad_senha:
                    break
                else:
                    print("As senhas não coincidem, tente novamente.")
            break

        usuario["email"] = cad_email
        usuario["senha"] = cad_senha



        db.usuarios.append(usuario.copy())
        usuario.clear()

        print("CADASTRADO COM SUCESSO;")
        time.sleep(1.5)

    def usuario_existe(self, email):

        for index, usuario in enumerate(db.usuarios):
            if usuario["email"] == email:
                return index
        return -1

    def usuario_auth(self, email, senha):

        for index, usuario in enumerate(db.usuarios):
            if usuario["email"] == email and usuario["senha"] == senha:
                return index
        return -1