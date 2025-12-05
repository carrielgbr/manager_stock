import sys
import time
from home_class01.home_class import cadas_login
from DB.conn import conn

class1 = cadas_login()

print ("******************")
print ("OQUE IRÁ SER FEITO")
print ("0 - SAIR;")
print ("1 - LOGIN;")
#print ("2 - CADASTRO;")

#fun_sair = input(print("aper"))
#fun_login = "login"

var_action = input(print(f"SAIR OU LOGIN"))


if var_action == "login":
    sucess = class1.login(param_login="realizando o login")
    time.sleep(0.3)
else:
    print("SAINDO DO PROGRAMA !!!!")
    time.sleep(0.20)
    sys.exit(0)



