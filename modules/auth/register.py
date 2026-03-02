from data import USERS
from modules.utils.screenController import pauseScreen
from modules.utils.msg import showError, showTitle, showInput


def register():
    """Register a new user"""
    showTitle("Sign up")

    name = showInput("Enter your name: ")
    email = showInput("Enter your email: ")
    password = showInput("Enter your password: ")

    for user in USERS:
        if user["email"] == email:
            showError("Email already exists")
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
