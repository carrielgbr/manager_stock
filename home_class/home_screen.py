from home_class.home_user.home_user import home_user_teste
from home_estoque.screen_estoque import screen_estoque
from home_produto.screen_produto import screen_produto
import variaveis_global
import time

estoque_screen = screen_estoque()
produto_screen = screen_produto()


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

            if enter_user == 'usuarios' or enter_user == '0':
                user_screen = home_user_teste(self)
                user_screen.fun_user()
            elif enter_user == 'estoques' or enter_user == '1':
                user_screen = screen_estoque()
                user_screen.tela_estoque()
            elif enter_user == 'produto' or enter_user == '2':
                user_screen = screen_produto()
                user_screen.tela_produto()
            elif enter_user == 'voltar' or enter_user == '3':
                return
            elif enter_user == 'sair':
                variaveis_global.usuario_logado_index = -1
                break
