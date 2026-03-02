from modules.utils.msg import showSuccess, showTitle, showInput, showError

def whithdrawAmount(currentUser: dict):
    showTitle("Withdraw money")

    while True:
        try:
            quantity = float(showInput("Enter the amount to withdraw: "))
        except ValueError:
            showError("The amount to withdraw must be a number")
            continue
        if quantity < 0:
            showError("The amount to withdraw must be greater than 0")
            continue
        if quantity > currentUser["balance"]:
            showError("Insufficient funds")
            continue
        break

    currentUser["balance"] -= quantity
    showSuccess(f"Amount withdrawn: {quantity}")
    showSuccess(f"Remaining balance: {currentUser['balance']}")
