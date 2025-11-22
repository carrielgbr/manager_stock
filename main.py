import time
from home_class01.home_class import cadas_login

class1 = cadas_login()



print ("******************")
print ("OQUE IRÁ SER FEITO")
print ("0 - SAIR;")
print ("1 - LOGIN;")
print ("2 - CADASTRO;")

#fun_sair = input(print("aper"))
#fun_login = "login"

var_action = input(print(f"CADASTRAR OU LOGIN"))


if var_action == "login":
    sucess = class1.login(param_login="realizando o login")
    time.sleep(0.10)
elif var_action == "cadastro":
    sucess = class1.cadastro(parametro_teste="relaizando o cadastro")
    time.sleep(0.20)
else:
    print("SAINDO DO PROGRAMA; esse daqui")
    time.sleep(0.50)
    exit

