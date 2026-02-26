def depositAmount(saldo:float):
    print("Depositar dinero")

    while True:
        try:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
        except ValueError:
            cantidad = -1
        if cantidad < 0:
            print("La cantidad a depositar debe ser mayor a 0")
            continue
        break

    saldo += cantidad
    return cantidad, saldo