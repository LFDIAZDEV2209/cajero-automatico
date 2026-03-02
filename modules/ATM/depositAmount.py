from modules.utils.msg import showTitle, showError, showSuccess, showInput
from modules.utils.corefiles import update_user, get_user_by_id


def depositAmount(currentUser: dict) -> None:
    """Deposit money into the user's account. Updates currentUser in place with fresh balance."""
    showTitle("Deposit money")

    while True:
        try:
            quantity = float(showInput("Enter the amount to deposit: "))
        except ValueError:
            showError("The amount to deposit must be a number")
            continue
        if quantity <= 0:
            showError("The amount to deposit must be greater than 0")
            continue
        break

    user_id = currentUser.get("id")
    new_balance = (currentUser.get("balance") or 0) + quantity
    if not update_user(user_id, {"balance": new_balance}):
        showError("Could not update balance")
        return

    # Refresh currentUser from DB so withdraw/list use correct balance
    updated = get_user_by_id(user_id)
    if updated:
        currentUser.update(updated)
    showSuccess(f"Amount deposited: {quantity}")
    showSuccess(f"Remaining balance: {currentUser.get('balance')}")
