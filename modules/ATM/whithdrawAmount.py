def whithdrawAmount(saldo: float):
    print("Retirar dinero")

    while True:
        try:
            cantidad = float(input("\nIngrese la cantidad a retirar: "))
        except ValueError:
            cantidad = -1
        if cantidad < 0:
            print("\nLa cantidad a retirar debe ser mayor a 0")
            continue
        if cantidad > saldo:
            print("\nFondos insuficientes")
            continue
        break
    return cantidad, saldo - cantidad
