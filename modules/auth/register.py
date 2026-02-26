from data import USERS

def register():
    print("Registrarse")
    name = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    for user in USERS:
        if user["email"] == email:
            print("El email ya está registrado")
            return False
    USERS.append({
        "id": len(USERS) + 1,
            "name": name,
            "email": email,
            "password": password
        })
    print("Registro exitoso")
    return True