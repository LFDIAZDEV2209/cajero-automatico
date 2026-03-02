from data import USERS
from modules.utils.screenController import pauseScreen
from modules.utils.msg import showSuccess, showTitle, showInput

def login():
    showTitle("Log in")

    email = showInput("Enter your email: ")
    password = showInput("Enter your password: ")

    for user in USERS:
        if user["email"] == email and user["password"] == password:
            showSuccess("Log in successful")
            pauseScreen()
            return True, user
    
    return False, None
