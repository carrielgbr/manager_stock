import time
from home_screen.home_screen import select_screen

function_screen = select_screen()


class cadas_login:
    email_logado = ""
    senha_logado = ""

    def login_tela(self):
        print()
        print("*" * 40)
        print("\tTela de Login")
        print("*" * 40)
        print()

    # Tela de Login
    def login(self):

        email_cadastrado = "gabriel"
        senha_cadastrado = "gabriel"

        self.login_tela()
        input_email = input("E-mail: ")
        input_senha = input("Senha: ")

        if input_email == email_cadastrado and input_senha == senha_cadastrado:

            self.email_logado = input_email
            self.senha_logado = input_senha

            function_screen.manager_home(self.email_logado)
            return
        else:
            print(senha_cadastrado, "errou, abestado")
        return

    # Mover essa função para outro arquivo.
    def cadastro(self, parametro_teste):

        cad_email = input(print("INSIRA SEU EMAIL"))
        cad_senha = input(print("INSIRA SUA SENHA"))

        print("CADASTRADO COM SUCESSO;")

        sair_function = input(print("SAIR DA FUNÇÃO"))

        result_text = "teste da variavel da funçã" + str(parametro_teste)
        return result_text