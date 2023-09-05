def producto_escalar(v1, v2):
    if len(v1) != len(v2):
        return "Error: Los vectores deben tener la misma longitud"
    
    resultado = 0
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]
    
    return resultado

n = int(input("Ingrese la longitud de los vectores: "))

vector1 = []
vector2 = []

print("Ingrese los elementos del primer vector:")
for i in range(n):
    num = float(input(f"Ingrese el elemento {i + 1}: "))
    vector1.append(num)

print("Ingrese los elementos del segundo vector:")
for i in range(n):
    num = float(input(f"Ingrese el elemento {i + 1}: "))
    vector2.append(num)

while True:
    print("\nSelecciona una opción:")
    print("1. Producto Escalar")
    print("2. Salir")

    opcion = input("Ingresa el número de la operación: ")

    if opcion == "2":
        break

    if opcion == "1":
        resultado = producto_escalar(vector1, vector2)
        print("Producto Escalar:", resultado)
    else:
        print("ERROR")