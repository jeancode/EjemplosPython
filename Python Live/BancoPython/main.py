
Dinero = 1000

def retirarFondos(monto):
    global Dinero
    Dinero -= monto

    #verificar el que monto a retirar no sea mayor al que tiene
    if monto > Dinero:
        print("No hay suficiente dinero")
        return False

    print("Retiraste $" + str(monto) + " y quedan $" + str(Dinero))


def depositarFondos(montos):
    global Dinero
    Dinero += montos

    print("Depositaste $" + str(montos) + " y quedan $" + str(Dinero))


def menu():
    print("1. Retirar fondos")
    print("2. Depositar fondos")
    print("3. Mirar saldo")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    

    if opcion == 1:
        monto = int(input("Ingrese el monto a retirar: "))
        retirarFondos(monto)
        menu()
    if opcion == 2:
        monto = int(input("Ingrese el monto a depositar: "))
        depositarFondos(monto);
        menu()
    if opcion == 3:
        print("Su saldo es de $" + str(Dinero))
        menu()
    if opcion == 4:
        print("Saliendo...")
        return
    



while(1):
    menu()
        