class select_screen:

    def function_print(self, selec_print):
        usuarios_1 = "usuarios"
        estoque_2 = "estoque"
        produto_3 = "produto"
        fornecedor_4 = "fornecedor"
        cliente_5 = "cliente"
        funcionario_6 = "funcioanrios"

        print ("1 - Usuarios: ")
        print ("2 - Estoque: ")
        print ("3 - Produto: ")
        print ("4 - Fornecedor: ")
        print ("5 - Clientes: ")
        print ("6 - Funcionarios: ")


        enter_user = input(print("--SELECIONE OQUE VOCE QUER FAZER--"))

        if enter_user == usuarios_1:
            print("seleção correta de usuario:  ")
        else:
            print("erro de seleção")
        if enter_user == estoque_2:
            print("selecao correta de estoque:  ")
        else:
            print("erro de seleção")
        if enter_user == produto_3:
            print("seleção correta: ")
        else: 
            print("erro de selecao produto")
        if enter_user == fornecedor_4:
            print("seleção correta fornecedor")
        else:
            print("erro de seleção")
        if enter_user == cliente_5:
            print("seleção correta de cliente ")
        else:
            print("erro de seleção")
        if enter_user == funcionario_6:
            print("seleçao correta ")