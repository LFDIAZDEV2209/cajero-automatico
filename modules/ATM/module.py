from modules.utils.screenController import deleteScreen, pauseScreen
from modules.utils.msg import MENU
from modules.ATM.listAmount import listAmount
from modules.ATM.whithdrawAmount import whithdrawAmount
from modules.ATM.depositAmount import depositAmount


def ATMmodule(currentUser: dict):
    while True:
        deleteScreen()
        print(MENU)
        option = input("Enter an option: ")
        match option:
            case "1":
                listAmount(currentUser)
            case "2":
                whithdrawAmount(currentUser)
            case "3":
                depositAmount(currentUser)
            case "4":
                print("\nThanks for using the ATM")
                break
            case _:
                print("\nInvalid option")
        pauseScreen()
