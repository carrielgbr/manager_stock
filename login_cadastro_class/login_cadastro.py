import time

class Cadastro_logic:

    email_logado = ""
    senha_logado = ""

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

        if len(self.usuarios) <= 0:
            print("Não há nenhum usuário cadastrado no sistema.")
            print("Por favor, cadastre-se para acessar o sistema.")
            time.sleep(4)
            return False

        self.login_tela()
        input_email = input("E-mail: ")
        input_senha = input("Senha: ")

        if self.usuario_existe(input_email, input_senha):
            self.email_logado = input_email
            self.senha_logado = input_senha
            return True
        else:
            print("Errou, abestado!")
        return False

    # Mover essa função para outro arquivo.
    def cadastro(self):

        cad_email = input("Insira seu Email: ")
        while True:
            cad_senha = input("Insira a senha: ")
            cad_senha_nov = input("Insira a senha novamente: ")
            if cad_senha_nov == cad_senha:
                break

        self.usuario["email"] = cad_email
        self.usuario["senha"] = cad_senha

        self.usuarios.append(self.usuario.copy())
        self.usuario.clear()

        print("CADASTRADO COM SUCESSO;")
        time.sleep(1.5)

    def usuario_existe(self, email, senha):

        for usuario in self.usuarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                return True

        return False