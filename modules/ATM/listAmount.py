from modules.utils.msg import showTitle, showSuccess
from modules.utils.corefiles import read_json

def listAmount(currentUser: dict):
    """List the user's balance"""
    showTitle("Current balance")
    users = read_json()
    for user in users:
        if user.get("id") == currentUser.get("id"):
            showSuccess(f"Actual balance: {user.get("balance")}")
            break
