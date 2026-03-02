from modules.utils.msg import showTitle, showError, showSuccess, showInput

def depositAmount(currentUser: dict):
    """Deposit money into the user's account"""
    showTitle("Deposit money")

    while True:
        try:
            quantity = float(showInput("Enter the amount to deposit: "))
        except ValueError:
            showError("The amount to deposit must be a number")
            continue
        if quantity < 0:
            showError("The amount to deposit must be greater than 0")
            continue
        break

    currentUser["balance"] += quantity
    showSuccess(f"Amount deposited: {quantity}")
    showSuccess(f"Remaining balance: {currentUser['balance']}")
