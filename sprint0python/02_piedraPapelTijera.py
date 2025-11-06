import random

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

reglas = {
    "tijera": {"papel", "lagarto"},
    "papel": {"piedra", "spock"},
    "piedra": {"tijera", "lagarto"},
    "lagarto": {"spock", "papel"},
    "spock": {"piedra", "tijera"}
}

def resultado(jugada_usuario, jugada_CPU):
    if jugada_CPU in reglas[jugada_usuario]:
        return 1
    elif jugada_usuario in reglas[jugada_CPU]:
        return -1
    else:
        return 0

def mejor_de_n(rondas, rondas_usuario, rondas_CPU):
    if rondas_usuario >= rondas//2 + 1:
        print("¡Has ganado!")
        return 1
    elif rondas_CPU >= rondas//2 + 1:
        print("Has perdido...")
        return -1
    else:
        print(f"Usuario: {rondas_usuario}, CPU: {rondas_CPU}")
        return 0

def jugar(rondas, rondas_usuario, rondas_CPU):
    estado_partida = 0
    while estado_partida == 0:
        check_jugada = False
        while not check_jugada:
            try:
                jugada_usuario = input("¡Piedra, papel, tijera, lagarto, Spock!:")
                if jugada_usuario in opciones:
                    check_jugada = True
                else:
                    raise ValueError("Escoge entre 'piedra', 'papel', 'tijera', 'lagarto' o 'spock'.")
            except ValueError as e:
                print("Error", e)

        jugada_CPU = random.choice(opciones)
        print(f"CPU: {jugada_CPU}")

        resultado_ronda = resultado(jugada_usuario, jugada_CPU)

        if resultado_ronda == 1:
            rondas_usuario += 1
        elif resultado_ronda == -1:
            rondas_CPU += 1

        estado_partida = mejor_de_n(rondas, rondas_usuario, rondas_CPU)

partida = True
while partida:
    rondas_valido = False
    while not rondas_valido:
        try:
            entrada = input("¿Cuántas rondas quieres jugar?")
            rondas = int(entrada)
            if rondas > 0:
                rondas_valido = True
            else:
                raise ValueError("Escoge un entero positivo")
        except ValueError:
            print("Error: Escoge un entero positivo")
    rondas_usuario = 0
    rondas_CPU = 0

    jugar(rondas, rondas_usuario, rondas_CPU)

    check_otra_vez = False
    while not check_otra_vez:
        otra_vez = input("¿Quieres jugar otra vez? (s/n)")
        try:
            if otra_vez.lower() == "s":
                partida = True
                check_otra_vez = True
            elif otra_vez.lower() == "n":
                partida = False
                check_otra_vez = True
            else:
                raise ValueError("Escoge entre 'n' y 's'.")
        except ValueError as e:
            print("Error", e)
