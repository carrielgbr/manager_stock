import time

print ("******************")
print ("OQUE IRÁ SER FEITO")
print ("0 - SAIR")
print ("1 - LOGIN")

#fun_sair = input(print("aper"))
#fun_login = "login"

fun_action = input(print("sair ou login, escolha um dos dois"))


if fun_action == "login":
    print ("Login feito seu animal:  ")
    time.sleep(0.10)
    exit
else:
    print("SAINDO DO PROGRAMA;")
    time.sleep(0.50)
    exit
