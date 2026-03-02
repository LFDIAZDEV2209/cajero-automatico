from modules.utils.msg import showTitle, showSuccess

def listAmount(currentUser: dict):
    """List the user's balance"""
    showTitle("Current balance")
    showSuccess(f"Actual balance: {currentUser['balance']}")
