def depositAmount(currentUser: dict):
    print("Deposit money")

    while True:
        try:
            cantidad = float(input("\nEnter the amount to deposit: "))
        except ValueError:
            cantidad = -1
        if cantidad < 0:
            print("\nThe amount to deposit must be greater than 0")
            continue
        break

    currentUser["balance"] += cantidad
    print("Amount deposited:", cantidad)
    print("Current balance:", currentUser["balance"])
