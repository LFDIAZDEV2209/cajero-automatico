from modules.ATM.module import ATMmodule
from modules.utils.msg import MENU_USER
from modules.utils.screenController import deleteScreen, pauseScreen
from modules.auth.login import login
from modules.auth.register import register


def main():
    while True:
        deleteScreen()
        print(MENU_USER)
        option = input("Enter an option: ")
        match option:
            case "1":
                isAuth, currentUser = login()
                if isAuth:
                    ATMmodule(currentUser)
                else:
                    print("Credentials incorrects")
            case "2":
                if register():
                    print("Sign up successful")
                else:
                    print("Sign up failed")
            case "3":
                print("\nThanks for using the ATM")
                break
            case _:
                print("Invalid option")
        pauseScreen()


if __name__ == "__main__":
    main()
