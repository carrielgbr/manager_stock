import sys
import time
import variaveis_global
from db import usuarios
from login_cadastro_class.login_cadastro import Cadastro_logic
from home_class.home_screen import Home_screen


# Classes
cadastro_login = Cadastro_logic()
home_screen = Home_screen()
# Add admin
cadastro_login.add_admin()

# Funções
def tela_main():
    print()
    print("*" * 40)
    print("\tBem-vindo ao Manager Stock")
    print("*" * 40)
    print()
    print("0 - Login;")
    print("1 - Cadastro;")
    print("2 - Fechar Programa;")



# ================================ Inicio

#fun_sair = input(print("aper"))
#fun_login = "login"

while True:

    tela_main()

    # Ação do Usuário
    var_action = input(">>:   ")
    # Deixa todas as palavras minusculas
    var_action = var_action.lower()

    if var_action in ['0', 'login']:
        variaveis_global.usuario_logado_index = cadastro_login.login()
        if variaveis_global.usuario_logado_index != -1:
            home_screen.manager_home()

    elif var_action in ['1', 'cadastro']:
        cadastro_login.cadastro()

    elif var_action in ['2', 'sair']:
        print("SAINDO DO PROGRAMA !!!!")
        time.sleep(0.10)
        sys.exit(0)
