import time
import variaveis_global

class Cadastro_logic:

    usuario = {}
    usuarios = []

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

        if len(self.usuarios) <= 0:
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

            index = self.usuario_existe(input_email, input_senha)
            if index != -1:
                return index
            else:
                print("Login e/ou senha incorreto!")

    # Mover essa função para outro arquivo.
    def cadastro(self):

        cad_email = input("Insira seu Email: ")
        if cad_email == variaveis_global.voltar_flair:
            return

        while True:
            cad_senha = input("Insira a senha: ")
            if cad_senha == variaveis_global.voltar_flair:
                return
            cad_senha_nov = input("Insira a senha novamente: ")
            if cad_senha == variaveis_global.voltar_flair:
                return
            if cad_senha_nov == cad_senha:
                break

        self.usuario["email"] = cad_email
        self.usuario["senha"] = cad_senha

        self.usuarios.append(self.usuario.copy())
        self.usuario.clear()

        print("CADASTRADO COM SUCESSO;")
        time.sleep(1.5)

    def usuario_existe(self, email, senha):

        for index, usuario in enumerate(self.usuarios):
            if usuario["email"] == email and usuario["senha"] == senha:
                return index
        return -1