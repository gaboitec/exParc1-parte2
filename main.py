def calcular_mcd(a, b):
    if b == 0:
        return a
    else:
        return calcular_mcd(b, a % b)


def main():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Calcular MCD de dos números")
    print("2. Repetir una cadena N veces")
    print("3. Contar las veces que aparece una letra en una cadena")
    print("4. Convertir decimal a binario")
    print("5. Contar los digitos de un número")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            mcd = calcular_mcd(a, b)
            print(f"El MCD de {a} y {b} es: {mcd}")