from home_class.home_user.home_user import home_user_teste 
import time

class Home_screen:

    email_logado = ""

    def tela_manager_home(self):
        acoes = ['Usuarios', 'Estoque', 'Produto', 'Fornecedor', 'Funcionario', 'Voltar', 'Sair']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")

    def manager_home(self):

        print(f"Bem-Vindo \'Teste\'.")
        print()
        time.sleep(1)

        while True:

            self.tela_manager_home()
            enter_user = input(">> ")
            enter_user = enter_user.lower()

            if enter_user == 'usuarios':
                user_screen = home_user_teste(self)
                user_screen.fun_user()
            elif enter_user == 'estoque':
                print(enter_user, 'screen users')
            elif enter_user == 'produto':
                print(enter_user, 'screen users')
            elif enter_user == 'fornecedor':
                print (enter_user, 'screen users')
            elif enter_user == 'funcionario':
                print (enter_user, 'screen users')
            elif enter_user == 'voltar':
                return
            elif enter_user == 'sair':
                exit(False)