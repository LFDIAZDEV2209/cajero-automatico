from modules.utils.screenController import deleteScreen, pauseScreen
from modules.utils.msg import MENU
from modules.ATM.listAmount import listAmount
from modules.ATM.whithdrawAmount import whithdrawAmount
from modules.ATM.depositAmount import depositAmount


def ATMmodule(mySaldo: float):
    while True:
        deleteScreen()
        print(MENU)
        option = input("Ingrese una opcion: ")
        match option:
            case "1":
                listAmount(mySaldo)
            case "2":
                cantidad, mySaldo = whithdrawAmount(mySaldo)
                print(
                    f"\nRetiro de {cantidad} realizado correctamente. Nuevo saldo: {mySaldo}")
            case "3":
                cantidad, mySaldo = depositAmount(mySaldo)
                print(
                    f"\nDeposito de {cantidad} realizado correctamente. Nuevo saldo: {mySaldo}")
            case "4":
                print("\nGracias por usar el cajero automático")
                break
            case _:
                print("\nOpción inválida")
        pauseScreen()
