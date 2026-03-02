from modules.utils.screenController import deleteScreen, pauseScreen
from modules.utils.msg import showTitle, showError, showSuccess
from modules.utils.msg import showMenu
from modules.utils.corefiles import get_user_by_id
from modules.ATM.listAmount import listAmount
from modules.ATM.whithdrawAmount import withdrawAmount
from modules.ATM.depositAmount import depositAmount


def ATMmodule(currentUser: dict) -> None:
    """ATM main menu. currentUser is refreshed from DB at each loop."""
    while True:
        updated = get_user_by_id(currentUser.get("id"))
        if updated:
            currentUser.update(updated)
        deleteScreen()
        showTitle("ATM Riwi")
        option = showMenu()
        match option:
            case 1:
                listAmount(currentUser)
            case 2:
                withdrawAmount(currentUser)
            case 3:
                depositAmount(currentUser)
            case 4:
                showSuccess("Thanks for using the ATM")
                break
            case _:
                showError("Invalid option")
        pauseScreen()
