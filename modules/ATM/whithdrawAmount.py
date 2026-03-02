from modules.utils.msg import showSuccess, showTitle, showInput, showError
from modules.utils.corefiles import update_user, get_user_by_id


def withdrawAmount(currentUser: dict) -> None:
    """Withdraw money from the user's account. Updates currentUser in place with fresh balance."""
    showTitle("Withdraw money")

    balance = currentUser.get("balance") or 0
    while True:
        try:
            quantity = float(showInput("Enter the amount to withdraw: "))
        except ValueError:
            showError("The amount to withdraw must be a number")
            continue
        if quantity <= 0:
            showError("The amount to withdraw must be greater than 0")
            continue
        if quantity > balance:
            showError("Insufficient funds")
            continue
        break

    user_id = currentUser.get("id")
    new_balance = balance - quantity
    if not update_user(user_id, {"balance": new_balance}):
        showError("Could not update balance")
        return

    # Refresh currentUser from DB so next operations use correct balance
    updated = get_user_by_id(user_id)
    if updated:
        currentUser.update(updated)
    showSuccess(f"Amount withdrawn: {quantity}")
    showSuccess(f"Remaining balance: {currentUser.get('balance')}")
