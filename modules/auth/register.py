from modules.utils.msg import showTitle, showInput
from modules.utils.corefiles import add_user, read_json, get_user_by_email


def register() -> bool:
    """Register a new user. Returns True if successful."""
    users = read_json()
    showTitle("Sign up")

    name = showInput("Enter your name: ")
    email = showInput("Enter your email: ")
    password = showInput("Enter your password: ")

    if get_user_by_email(email):
        return False  # Email already registered

    next_id = max((u["id"] for u in users), default=0) + 1
    if add_user({
        "id": next_id,
        "name": name,
        "email": email,
        "password": password,
        "balance": 0.0
    }):
        return True
    else:
        return False
