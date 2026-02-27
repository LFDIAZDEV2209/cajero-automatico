from data import USERS
from modules.utils.screenController import pauseScreen


def register():
    print("Registrarse")
    name = input("\nIngrese su nombre: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    for user in USERS:
        if user["email"] == email:
            print("\nEl email ya está registrado")
            pauseScreen()
            return False
    USERS.append({
        "id": len(USERS) + 1,
        "name": name,
        "email": email,
        "password": password,
        "saldo": 0
    })
    return True
