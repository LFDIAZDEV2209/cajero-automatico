from data import USERS
from modules.utils.screenController import pauseScreen


def login():
    print("\nIniciar sesión")
    email = input("\nIngrese su email: ")
    password = input("Ingrese su contraseña: ")
    for user in USERS:
        if user["email"] == email and user["password"] == password:
            print("\nInicio de sesión exitoso")
            pauseScreen()
            return True, user["saldo"]
    print("\nCredenciales incorrectas")
    pauseScreen()
    return False
