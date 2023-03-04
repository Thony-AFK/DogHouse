from clases.carta import Carta
#valquiria = Carta(10000) 
#print(str(valquiria.vida))

#bubumon = Carta(-999) 
#print(str(bubumon.vida))

# Importar la librería 'os' para poder interactuar con el sistema operativo
import os

# Función para limpiar la pantalla
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú y obtener la opción seleccionada
def menu():
    clear()
    print("Selecciona una opción:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

    opcion = input("Ingresa el número de la opción que deseas: ")
    return opcion

# Bucle principal del programa
while True:
    opcion = menu()

    if opcion == "1":
        # Lógica para la opción 1
        print("Has seleccionado la opción 1")
        input("Presiona enter para continuar...")
    elif opcion == "2":
        # Lógica para la opción 2
        print("Has seleccionado la opción 2")
        input("Presiona enter para continuar...")
    elif opcion == "3":
        # Salir del programa
        clear()
        print("¡Hasta pronto!")
        break
    else:
        # Opción inválida
        input("Opción inválida. Presiona enter para continuar...")
