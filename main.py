def calcular_mcd(a, b):
    if b == 0:
        return a
    else:
        return calcular_mcd(b, a % b)

def repetir_cadena(palabra, veces):
    if veces == 0:
        return ""
    else:
        return palabra + " " + repetir_cadena(palabra, veces - 1)

def contar_letra(cadena, letra):
    cadena = list(cadena)
    if len(cadena) == 0:
        return 0
    else:
        if cadena[0] == letra:
            cadena.pop(0)
            return 1 + contar_letra(cadena, letra)
        else:
            cadena.pop(0)
            return 0 + contar_letra(cadena, letra)

def convertir_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return convertir_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

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
            while True:
                try:
                    a = int(input("Ingrese el primer número: "))
                    b = int(input("Ingrese el segundo número: "))
                    mcd = calcular_mcd(a, b)
                    print(f"El MCD de {a} y {b} es: {mcd}")
                    break
                except ValueError:
                    print("Ingrese números válidos.")

        case "2":
            while True:
                try:
                    palabra = input("Ingrese la palabra: ")
                    veces = int(input("Cuantas veces?: "))
                    resultado = repetir_cadena(palabra, veces)
                    print(f"La cadena repetida es: {resultado}")
                    break
                except ValueError:
                    print("Ingrese datos validos.")

        case "3":
            while True:
                try:
                    cadena = input("Ingrese la cadena: ")
                    letra = input("Ingrese la letra: ")
                    veces = contar_letra(cadena, letra)
                    palabra = "vez"
                    if veces > 1:
                        palabra = "veces"

                    print(f"La letra '{letra}' aparece {veces} {palabra}.")
                    break
                except ValueError:
                    print("Ingrese datos válidos.")

        case "4":
            while True:
                try:
                    decimal = int(input("Ingrese un número: "))
                    binario = convertir_binario(decimal)
                    print("El resultado es:", binario)
                    break
                except ValueError:
                    print("Ingrese datos validos.")

        case "5":
            while True:
                try:
                    numero = int(input("Ingrese un número: "))
                    digitos = contar_digitos(numero)
                    print(f"El número tiene {digitos} dígitos.")
                    break
                except ValueError:
                    print("Ingrese un número válido.")

        case "0":
            print("Saliendo del programa...")
            exit()
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")

    main()

main()