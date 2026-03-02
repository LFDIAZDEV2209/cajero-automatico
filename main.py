from modules.ATM.module import ATMmodule
from modules.utils.msg import showTitle, showLoginMenu, showError, showSuccess
from modules.utils.screenController import deleteScreen, pauseScreen
from modules.utils.corefiles import initialize_json
from modules.auth.login import login
from modules.auth.register import register


def main() -> None:
    """Main function"""
    initialize_json()
    while True:
        deleteScreen()
        showTitle("Welcome to the ATM Riwi")
        option = showLoginMenu()
        match option:
            case 1:
                isAuth, currentUser = login()
                if isAuth:
                    ATMmodule(currentUser)
                else:
                    showError("Credentials incorrects")
            case 2:
                if register():
                    showSuccess("Sign up successful")
                else:
                    showError("Sign up failed")
            case 3:
                showSuccess("Thanks for using the ATM")
                break
            case _:
                showError("Invalid option")
        pauseScreen()


if __name__ == "__main__":
    main()
