import time
from home_screen.home_screen import select_screen

function_screen = select_screen()

class cadas_login:

    def login(self, param_login):
        email_cadastrado = "gabriel"
        senha_cadastrado = "gabriel"
        email = input(print(f"1 -  INSIRA SEU E-MAIL:..."))
        senha = input(print(f"2 - INSIRIA SUA SENHA:..."))
        
        if email == email_cadastrado and senha == senha_cadastrado:
            time.sleep(10)
            print(email_cadastrado, "parabens login relazado")

            sucess = function_screen.function_print(selec_print="tela home depois do")

            return True
        else:
            print(senha_cadastrado, "errou, abestado")
        return False


#Mover essa função para outro arquivo. 
    def cadastro(self, parametro_teste):
        
        cad_email = input(print("INSIRA SEU EMAIL"))
        cad_senha = input(print("INSIRA SUA SENHA"))

        print("CADASTRADO COM SUCESSO;")
        
        sair_function = input(print("SAIR DA FUNÇÃO"))
                
        result_text = "teste da variavel da funçã" + str(parametro_teste)
        return result_text