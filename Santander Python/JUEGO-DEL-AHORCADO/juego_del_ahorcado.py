

import random


def obtener_palabra_secreta() -> str:
    palabras=['python','javascript','java','angular','django','tensorflow','react','typescript','git','flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta,letras_adivinadas):
    adivinado=''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado+=letra
        else:
            adivinado += "_"

    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas=[]
    intentos=8
    juego_terminado=False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta,letras_adivinadas), "La cantidad de letras de la palabra es: ",len(palabra_secreta))

    while not juego_terminado and intentos >0:
        adivinanza = input("Introduce una letras: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra valida(solo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"¡ Muy bien has acertado ,la letra '{adivinanza}' esta presente en la palabra")
            else:
                intentos -=1
                print(f"Lo siento mucho la letra '{adivinanza}' no esta presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos")
        progreso_actual=mostrar_progreso(palabra_secreta,letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado=True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Felicitaciones has ganado!, La palabra completa: '{palabra_secreta}'")

    if intentos == 0:
        palabra_secreta=palabra_secreta.capitalize()
        print(f"Lo sentimos mucho se te ha terminado los intentos, la palabra secreta era '{palabra_secreta}'")

juego_ahorcado()
