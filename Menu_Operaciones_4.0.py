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
            return "Error"
    return resultado

def producto_escalar(v1, v2):
    if len(v1) != len(v2):
        return "Error"
    
    resultado = 0
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]
    
    return resultado

n = int(input("Ingresa los números: "))

numeros = []

for i in range(n):
    num = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(num)

while True:
    print("\nSelecciona una opcion:")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Producto Escalar")
    print("6.- Salir")

    opcion = input("Operacion: ")

    if opcion == "6":
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
        
        print("Resultado: ", resultado)
    elif opcion == "5":
        v1 = []
        v2 = []
        
        print("Ingresa los numeros del primer vector:")
        for i in range(n):
            num = float(input(f"Ingrese el numero {i + 1}: "))
            v1.append(num)
        
        print("Ingresa los numeros del segundo vector:")
        for i in range(n):
            num = float(input(f"Ingrese el numero {i + 1}: "))
            v2.append(num)
        
        resultado = producto_escalar(v1, v2)
        print("Producto Escalar: ", resultado)
    else:
        print("ERROR")
