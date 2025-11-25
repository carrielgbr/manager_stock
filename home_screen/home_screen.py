#from home_class01.home_class import cadas_login

#function_login = cadas_login()

class select_screen:

    def function_print(self, selec_print):
        #usuarios_1 = "usuarios"
        #estoque_2 = "estoque"
        #produto_3 = "produto"
        #Cliente_5 = "cliente"
        #funcionario_6 = "funcioanrios"

        selec_var = ['usuarios', 'estoque', 'produto', 'fornecedor', 'cliente', 'funcionario']

        print ("1 - Usuarios: ")
        print ("2 - Estoque: ")
        print ("3 - Produto: ")
        print ("4 - Fornecedor: ")
        print ("5 - Clientes: ")
        print ("6 - Funcionarios: ")


        enter_user = input(print("--SELECIONE OQUE VOCE QUER FAZER--"))

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
        else:
            print('erro otario')