from modules.utils.screenController import deleteScreen, pauseScreen
from modules.utils.msg import showTitle, showError, showSuccess
from modules.utils.msg import showMenu
from modules.ATM.listAmount import listAmount
from modules.ATM.whithdrawAmount import whithdrawAmount
from modules.ATM.depositAmount import depositAmount


def ATMmodule(currentUser: dict):
    while True:
        deleteScreen()
        showTitle("ATM Riwi")
        option = showMenu()
        match option:
            case 1:
                listAmount(currentUser)
            case 2:
                whithdrawAmount(currentUser)
            case 3:
                depositAmount(currentUser)
            case 4:
                showSuccess("Thanks for using the ATM")
                break
            case _:
                showError("Invalid option")
        pauseScreen()
