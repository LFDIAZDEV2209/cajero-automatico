def whithdrawAmount(currentUser: dict):
    print("Withdraw money")

    while True:
        try:
            cantidad = float(input("\nEnter the amount to withdraw: "))
        except ValueError:
            cantidad = -1
        if cantidad < 0:
            print("\nThe amount to withdraw must be greater than 0")
            continue
        if cantidad > currentUser["balance"]:
            print("\nInsufficient funds")
            continue
        break

    currentUser["balance"] -= cantidad
    print("Amount withdrawn:", cantidad)
    print("Remaining balance:", currentUser["balance"])
