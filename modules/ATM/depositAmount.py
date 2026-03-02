def depositAmount(currentUser: dict):
    print("Depositar dinero")

    while True:
        try:
            cantidad = float(input("\nIngrese la cantidad a depositar: "))
        except ValueError:
            cantidad = -1
        if cantidad < 0:
            print("\nLa cantidad a depositar debe ser mayor a 0")
            continue
        break

    currentUser["saldo"] += cantidad
    print("Cantidad depositada:", cantidad)
    print("Saldo actual:", currentUser["saldo"])
