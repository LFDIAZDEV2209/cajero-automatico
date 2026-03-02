from data import USERS
from modules.utils.screenController import pauseScreen


def register():
    print("Sign up")

    name = input("\nEnter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in USERS:
        if user["email"] == email:
            print("\nEmail already exists")
            pauseScreen()
            return False
        
    USERS.append({
        "id": len(USERS) + 1,
        "name": name,
        "email": email,
        "password": password,
        "balance": 0
    })

    return True
