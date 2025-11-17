cuenta = {"nombre": "Ana", "Saldo": 1200.0}

def consultar_saldo():
    """
    Imprime en consola el Saldo de la cuenta
    """
    print()
    print(f"Saldo actual: {cuenta['Saldo']}")
    print()

def ingresar_dinero():
    """
    Pide introducir una cantidad, comprueba que es válida y la añade al Saldo
    """
    cantidad_ok = False
    while not cantidad_ok:
        try:
            entrada = input("Indica la cantidad a ingresar (0 para cancelar): ")
            cantidad = float(entrada)
            if cantidad == 0:
                print("Operación cancelada")
                cantidad_ok = True
            elif cantidad > 0:
                cuenta['Saldo'] += cantidad
                print(f"Saldo actual: {cuenta['Saldo']}")
                cantidad_ok = True
            else:
                raise ValueError("Escoge una cantidad numérica")
        except ValueError:
            print("Error: Escoge una cantidad numérica")

def retirar_dinero():
    """
    Pride introducir una cantidad, comprueba que es válida
    y menor que el Saldo disponible, y la resta del Saldo
    """
    cantidad_ok = False
    while not cantidad_ok:
        try:
            entrada = input("Indica la cantidad a retirar (0 para cancelar): ")
            cantidad = float(entrada)
            if cantidad == 0:
                print("Operación cancelada")
                cantidad_ok = True
            elif cantidad > cuenta['Saldo']:
                print("Saldo insuficiente.")
                cantidad_ok = True
            elif cantidad <= cuenta['Saldo'] and cantidad > 0:
                cuenta['Saldo'] -= cantidad
                print(f"Saldo actual: {cuenta['Saldo']}")
                cantidad_ok = True
            else:
                raise ValueError("Escoge una cantidad numérica")
        except ValueError:
            print("Error: Escoge una cantidad numérica")

salir = False
while not salir:
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    try:
        opcion = input("Ingresa una opcion: ")
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            ingresar_dinero()
        elif opcion == "3":
            retirar_dinero()
        elif opcion == "4":
            print("¡Chao!")
            salir = True
        else:
            raise Exception("Opción inválida")
    except Exception as e:
        print("Error", e)