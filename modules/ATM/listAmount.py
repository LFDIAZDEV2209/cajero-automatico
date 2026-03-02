from modules.utils.msg import showTitle, showSuccess

def listAmount(currentUser: dict):
    showTitle("Current balance")
    showSuccess(f"Actual balance: {currentUser['balance']}")
