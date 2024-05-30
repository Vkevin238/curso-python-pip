import random

def obtener_opcion_usuario():
    while True:
        opcion = input("Elige piedra, papel o tijera: ").lower()
        if opcion in ['piedra', 'papel', 'tijera']:
            return opcion
        else:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")

def obtener_opcion_computadora():
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate!"
    elif (opcion_usuario == 'piedra' and opcion_computadora == 'tijera') or \
         (opcion_usuario == 'papel' and opcion_computadora == 'piedra') or \
         (opcion_usuario == 'tijera' and opcion_computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def jugar():
    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()
        print("Tu elección:", opcion_usuario)
        print("Elección de la computadora:", opcion_computadora)
        print(determinar_ganador(opcion_usuario, opcion_computadora))
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

jugar()
