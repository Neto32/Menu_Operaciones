import numpy as np

def ingresar_vector():
    try:
        n = int(input("Ingrese la cantidad de números en el vector: "))
        vector = []
        for i in range(n):
            numero = float(input(f"Ingrese el número {i+1}: "))
            vector.append(numero)
        return np.array(vector)
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return ingresar_vector()

def mostrar_menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Producto Cruz")
    print("6. Salir")

def menu_operaciones():
    vector1 = ingresar_vector()
    vector2 = ingresar_vector()

    if len(vector1) != len(vector2):
        print("Los vectores deben tener la misma cantidad de números")
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona la operacion: ")

        if opcion == "1":
            resultado = vector1 + vector2
            print("R = ", resultado)
        elif opcion == "2":
            resultado = vector1 - vector2
            print("R = ", resultado)
        elif opcion == "3":
            resultado = vector1 * vector2
            print("R = ", resultado)
        elif opcion == "4":
            resultado = vector1 / vector2
            print("R = ", resultado)
        elif opcion == "5":
            if len(vector1) == 3:  # Verificar que ambos vectores sean de tamaño 3 para el producto cruz
                resultado = np.cross(vector1, vector2)
                print("R = ", resultado)
            else:
                print("Ambos vectores deben ser de tamaño 3 para el producto cruz.")
        elif opcion == "6":
            break

        else:
            print("NO valido")

if __name__ == "__main__":
    menu_operaciones()
