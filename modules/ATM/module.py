from modules.utils.screenController import deleteScreen, pauseScreen
from modules.utils.msg import MENU
from modules.ATM.listAmount import listAmount
from modules.ATM.whithdrawAmount import whithdrawAmount
from modules.ATM.depositAmount import depositAmount
from data import USERS

def ATMmodule():
    saldo = USERS[0]["saldo"]
    while True:
        deleteScreen()
        print(MENU)
        option = input("Ingrese una opcion: ")
        match option:
            case "1":
                listAmount(saldo)
            case "2":
                cantidad, saldo = whithdrawAmount(saldo)
                print(f"Retiro de {cantidad} realizado correctamente. Nuevo saldo: {saldo}")
            case "3":
                cantidad, saldo = depositAmount(saldo)
                print(f"Deposito de {cantidad} realizado correctamente. Nuevo saldo: {saldo}")
            case "4":
                print("Gracias por usar el cajero automático")
                break
            case _:
                print("Opción inválida")
        pauseScreen()
