def depositAmount(saldo: float):
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

    saldo += cantidad
    return cantidad, saldo
