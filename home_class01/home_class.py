class cadas_login:

    def login(self, param_login):
        email_cadastrado = "Gabriel"
        senha_cadastrado = "Gabriel"
        email = input(print(f"1 -  INSIRA SEU E-MAIL:..."))
        senha = input(print(f"2 - INSIRIA SUA SENHA:..."))
        
        if email == email_cadastrado and senha == senha_cadastrado:
            print(email_cadastrado, "parabens login relazado")
            return True
        else:
            print(senha_cadastrado, "errou, abestado")
        return False

    def cadastro(self, parametro_teste):
        
        cad_email = input(print"INSIRA SEU EMAIL")
        cad_senha = input(print"INSIRA SUA SENHA")

        print("CADASTRADO COM SUCESSO;")
        
        sair_function = input(print("SAIR DA FUNÇÃO"))
                
        result_text = "teste da variavel da funçã" + str(parametro_teste)
        return result_text