lista_compra = []
salir = False

def anadir():
    """
    Pide al usuario introducir un producto. Si ya está en
    la lista de la compra, no hace nada y devuelve False.
    Si no está, lo añade y devuelve True.
    """
    producto = input("Introduce el producto: ")
    producto = producto.lower().strip()
    if producto in lista_compra:
        print(f"'{producto}' ya estaba en la lista")
    else:
        lista_compra.append(producto)

def eliminar():
    """
    Pide al usuario introducir un producto. Si ya está en
    la lista de la compra, lo elimina y devuelve True.
    Si no está, no hace nada y devuelve False.
    """
    producto = input("Introduce el producto a eliminar: ")
    producto = producto.lower().strip()
    try:
        if producto in lista_compra:
            lista_compra.remove(producto)
        else:
            raise IndexError(f"'{producto}' no está en la lista.")
    except IndexError as e:
        print("Error", e)


def ver_lista():
    """
    Imprime la lista de la compra o un mensaje si está vacía.
    """
    if len(lista_compra) == 0:
        print()
        print("La lista está vacía.")
        print()
    else:
        print()
        print("Lista de la compra:")
        print(sorted(lista_compra))
        print()

def vaciar():
    """
    Pide al usuario confirmar la operación. Si responde "s",
    vacía la cesta, si responde "n", cancela. Comprueba que
    la respuesta introducida es válida.
    """
    vaciar_ok = False

    while not vaciar_ok:
        try:
            respuesta = input("¿Estás seguro? (s/n)")
            if respuesta == "s":
                lista_compra.clear()
                vaciar_ok = True
            elif respuesta == "n":
                print("Operación cancelada.")
                vaciar_ok = True
            else:
                raise Exception("Opción inválida")
        except Exception as e:
            print("Error", e)


while not salir:
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver lista")
    print("4. Vaciar lista")
    print("5. Salir")

    try:
        opcion = input("Ingresa una opcion: ")
        if opcion == "1":
            anadir()
        elif opcion == "2":
            eliminar()
        elif opcion == "3":
            ver_lista()
        elif opcion == "4":
            vaciar()
        elif opcion == "5":
            print("¡Chao!")
            salir = True
        else:
            raise Exception("Opción inválida")
    except Exception as e:
        print("Error", e)
