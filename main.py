import sys
import time
import variaveis_global
from login_cadastro_class.login_cadastro import Cadastro_logic
from home_class.home_screen import Home_screen
from home_produto.screen_produto import screen_produto

# Classes
produto_screen = screen_produto()
cadastro_login = Cadastro_logic()
home_screen = Home_screen()

if __name__ == "__main__":
    screen = screen_produto()

# Funções
def tela_main():
    print()
    print("*" * 40)
    print("\tBem-vindo ao Manager Stock")
    print("*" * 40)
    print()
    print("0 - Fechar Programa;")
    print("1 - Login;")
    print("2 - Cadastro;")



# ================================ Inicio

#fun_sair = input(print("aper"))
#fun_login = "login"

while True:

    tela_main()

    # Ação do Usuário
    var_action = input(">>:   ")
    # Deixa todas as palavras minusculas
    var_action = var_action.lower()

    if var_action in ['1', 'login']:
        variaveis_global.usuario_logado_index = cadastro_login.login()
        if variaveis_global.usuario_logado_index != -1:
            home_screen.manager_home()

    elif var_action in ['2', 'cadastro']:
        cadastro_login.cadastro()

    elif var_action in ['0', 'sair']:
        print("SAINDO DO PROGRAMA !!!!")
        time.sleep(0.10)
        sys.exit(0)
