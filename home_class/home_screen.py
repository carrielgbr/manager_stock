from home_class.home_user.home_user import home_user_teste 
from home_estoque.screen_estoque import screen_estoque
import time

estoque_screen = screen_estoque()

class Home_screen:

    email_logado = ""

    def tela_manager_home(self):
        acoes = ['Usuarios', 'Estoque', 'Produto' ,'Sair']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")

    def manager_home(self):

        print("=" * 40)
        print("TELA DE GERENCIAMENTO DE TELAS")
        print("=" * 40)
        print()
        time.sleep(1)

        while True:

            self.tela_manager_home()
            enter_user = input(">> ")
            enter_user = enter_user.lower()

            if enter_user == 'usuarios':
                user_screen = home_user_teste(self)
                user_screen.fun_user()
            elif enter_user == 'estoques':
                user_screen = screen_estoque()
                user_screen.tela_estoque()
            elif enter_user == 'produto':
                print(enter_user, 'screen produto')
            elif enter_user == 'voltar':
                return
            elif enter_user == 'sair':
                exit(False)