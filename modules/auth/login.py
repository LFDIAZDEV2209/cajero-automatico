
from modules.utils.msg import showSuccess, showTitle, showInput
from modules.utils.corefiles import get_user_by_email
from modules.utils.screenController import pauseScreen

def login():
    """Login a user"""
    showTitle("Log in")

    email = showInput("Enter your email: ")
    password = showInput("Enter your password: ")

    user = get_user_by_email(email)
    if user and user.get("password") == password:
        showSuccess("Log in successful")
        pauseScreen()
        return True, user
    else:
        return False, None
