import sys
import time
import os
from home_class01.home_class import cadas_login
from DB.conn import conn

# Variaveis
class1 = cadas_login()

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
    var_action = input(">> ")
    # Deixa todas as palavras minusculas
    var_action = var_action.lower()

    if var_action == "login":
        sucess = class1.login()
        time.sleep(0.5)
    elif var_action == "sair":
        print("SAINDO DO PROGRAMA !!!!")
        time.sleep(0.20)
        sys.exit(0)
