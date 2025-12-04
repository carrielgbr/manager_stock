#from home_class01.home_class import cadas_login
import time
#function_login = cadas_login()

class select_screen:

    email_logado = ""

    def tela_manager_home(self):
        acoes = ['Usuarios', 'Estoque', 'Produto', 'Fornecedor', 'Cliente', 'Funcionario', 'Voltar', 'Sair']
        for i in range(len(acoes)):
            print(f"{i} - {acoes[i]}")


    def manager_home(self, email_logado):

        self.email_logado = email_logado

        #usuarios_1 = "usuarios"
        #estoque_2 = "estoque"
        #produto_3 = "produto"
        #Cliente_5 = "cliente"
        #funcionario_6 = "funcioanrios"

        print(f"Bem-Vindo {self.email_logado}.")
        time.sleep(1)

        while True:

            self.tela_manager_home()
            enter_user = input(">> ")
            enter_user = enter_user.lower()

            #for enter_user in selec_var:
            if enter_user == 'usuarios':
                print(enter_user, 'screen users')
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