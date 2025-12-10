import sys
import time
import os
from login_cadastro_class.login_cadastro import Cadastro_logic
from home_class.home_screen import Home_screen

# Variaveis
success = ""

# Classes
cadastro_login = Cadastro_logic()
home_screen = Home_screen()

# Funções
def tela_main():
    print()
    print("*" * 40)
    print("\tBem-vindo ao Manager Stock")
    print("*" * 40)
    print()
    print("0 - Sair;")
    print("1 - Login;")
    print("2 - Cadastro;")



# ================================ Inicio

#fun_sair = input(print("aper"))
#fun_login = "login"

while (True):

    tela_main()

    # Ação do Usuário
    var_action = input(">>:   ")
    # Deixa todas as palavras minusculas
    var_action = var_action.lower()

    if var_action == "login":
        success = cadastro_login.login()
        if success:
            home_screen.manager_home()

    elif var_action == "cadastro":
        cadastro_login.cadastro()

    elif var_action == "sair":
        print("SAINDO DO PROGRAMA !!!!")
        time.sleep(0.10)
        sys.exit(0)

