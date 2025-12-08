from users_screen.users_screen import user_screen
import time

screen_user = user_screen()

class select_screen:

    email_logado = ""

    def tela_manager_home(self):
        acoes = ['Usuarios', 'Estoque', 'Produto', 'Fornecedor', 'Cliente', 'Funcionario', 'Voltar', 'Sair']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")


    def manager_home(self, email_logado):

        self.email_logado = email_logado

        print(f"Bem-Vindo {self.email_logado}.")
        time.sleep(1)

        while True:

            self.tela_manager_home()
            enter_user = input(">> ")
            enter_user = enter_user.lower()

            #for enter_user in selec_var:
            if enter_user == 'usuarios':
                screen_user.screen_print()
            elif enter_user == 'estoque':
                print(enter_user, 'screen users')
            elif enter_user == 'produto':
                print(enter_user, 'screen users')
            elif enter_user == 'fornecedor':
                print (enter_user, 'screen users')
            elif enter_user == 'cliente':
                print (enter_user, 'screen users')
            elif enter_user == 'cliente':
                print (enter_user, 'screen users')
            elif enter_user == 'voltar':
                return
            elif enter_user == 'sair':
                exit(False)