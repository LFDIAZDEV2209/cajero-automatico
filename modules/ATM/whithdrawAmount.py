def whithdrawAmount(saldo:float):
    print("Retirar dinero")

    while True:
        try:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
        except ValueError:
            cantidad = -1
        if cantidad < 0:
            print("La cantidad a retirar debe ser mayor a 0")
            continue
        if cantidad > saldo:
            print("Fondos insuficientes")
            continue
        break
    return cantidad, saldo - cantidad