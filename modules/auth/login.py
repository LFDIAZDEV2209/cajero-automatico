from data import USERS

def login():
    print("Iniciar sesión")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    for user in USERS:
        if user["email"] == email and user["password"] == password:
            print("Inicio de sesión exitoso")
            return True
    print("Credenciales incorrectas")
    return False    