import random


def juego_adivinanza():
    # Generar numero aleatorio
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Mensaje de bienvenida e instrucciones
    print("Bienvenido al juego de adivinanza de numero")
    print("Debes adivinar un numero del 1 al 100")
    print("Intenta adivinarlo")

    while not adivinado:
        # Solicitar un numero del 1 al 100
        adivinanza = input("introduce un numero del 1 al 100: ")
        # Verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # pasando de string a number
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"el numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"el numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"Felicitaciones el numero secreto era {adivinanza} y lo haz logrado en {intentos} intentos"
                )
        else:
            print("Por favor ingresa un numero del 1 al 100")

juego_adivinanza()
