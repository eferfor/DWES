# El programa elige un número secreto al azar y el usuario debe adivinarlo.
# En cada intento, el programa dice si el número es más alto o más bajo.

import random

def adivinaElNumero():
    print("El programa pensará un número entre 1 y un máximo que tú elijas. \
    Intenta adivinarlo con la menor cantidad de intentos posible.")

    nivel_valido = False
    numero = -1

    while(not nivel_valido):
        nivel = input("Escoge una dificultad (fácil, medio o difícil):")

        if nivel == "fácil":
            print("El número estará entre 1 y 20")
            numero = random.randint(1, 20)
            nivel_valido = True
        elif nivel == "medio":
            print("El número estará entre 1 y 100")
            numero = random.randint(1, 100)
            nivel_valido = True
        elif nivel == "dificil":
            print("El número estará entre 1 y 1000")
            numero = random.randint(1, 1000)
            nivel_valido = True

    contador = 0
    acertado = False

    print("Empieza el juego 👉")
    while(not acertado):
        print("Introduce un número:")

        intento = input()
        try:
            intento = int(intento)

            if intento == numero:
                contador += 1
                acertado = True
            elif intento < numero:
                contador += 1
                print("Demasiado bajo")
            elif intento > numero:
                contador += 1
                print("Demasiado alto")

        except ValueError:
            print("El valor debe ser un número.")
            continue

    if acertado:
        print(f"¡Felicidades! Adivinaste en {contador} intentos.")


jugar = True

while jugar:
    adivinaElNumero()
    print("¿Quieres jugar otra vez? (s/n)")
    respuesta = input()

    try:
        if respuesta.lower() == "s":
            continue
        elif respuesta.lower() == "n":
            jugar = False
        else:
            raise ValueError("Introduce 's' o 'n'")
    except ValueError as e:
        print("Error:", e)

print("Chao!")