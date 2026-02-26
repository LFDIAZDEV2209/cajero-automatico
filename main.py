from modules.ATM.module import ATMmodule
from modules.utils.msg import MENU_USER
from modules.utils.screenController import deleteScreen, pauseScreen
from modules.auth.login import login
from modules.auth.register import register

def main():
    while True:
        deleteScreen()
        print(MENU_USER)
        option = input("Ingrese una opcion: ")
        match option:
            case "1":
                if login():
                    ATMmodule()
                else:
                    print("Credenciales incorrectas")
            case "2":
                if register():
                    print("Registro exitoso")
                else:
                    print("Registro fallido")
            case "3":
                print("Gracias por usar el cajero automático")
                break
            case _:
                print("Opción inválida")
        pauseScreen()

if __name__ == "__main__":
    main()
