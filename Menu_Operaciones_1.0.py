def suma_numeros(numeros):
    return sum(numeros)

def resta_numeros(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        resultado -= numeros[i]
    return resultado

def multiplicacion_numeros(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def division_numeros(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[i] != 0:
            resultado /= numeros[i]
        else:
            return "Error: No divisible entre cero"
    return resultado

n = int(input("Ingrese los números usar: "))

numeros = []

for i in range(n):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

while True:
    print("\nSelecciona una opcion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación: ")

    if opcion == "5":
        break

    if opcion in ("1", "2", "3", "4"):
        if opcion == "1":
            resultado = suma_numeros(numeros)
        elif opcion == "2":
            resultado = resta_numeros(numeros)
        elif opcion == "3":
            resultado = multiplicacion_numeros(numeros)
        elif opcion == "4":
            resultado = division_numeros(numeros)

        print("Resultado:", resultado)
    else:
        print("ERROR")
