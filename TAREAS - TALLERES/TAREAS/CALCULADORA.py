
def Sumar(valor1, valor2):
    return valor1 + valor2

def Restar(valor1, valor2):
    return valor1 - valor2

def Multiplicar(valor1, valor2):
    return valor1 * valor2

def Dividir(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "No se puede dividir para cero"

def Potencia(valor1, valor2):
    return valor1 ** valor2

def RaizCuadrada(valor1):
    return valor1 ** 0.5

def ValidNumber(number):
    return number.lstrip("-").isdigit()

def Valores():
    valor1 = input("Ingrese el primer número: ")
    valor2 = input("Ingrese el segundo número: ")
    if ValidNumber(valor1) and ValidNumber(valor2):
        return int(valor1), int(valor2)
    else:
        print("Ingrese solo números válidos")
        return None, None

def MenuCalculadora():
    print("\n===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")

def SistemaCalculadora():
    while True:
        MenuCalculadora()
        opc = input("Seleccione una opción: ")
        if ValidNumber(opc):
            opc = int(opc)
            match opc:
                case 1:
                    valor1, valor2 = Valores()
                    if valor1 is not None:
                        print(f"Resultado: {Sumar(valor1, valor2)}")
                case 2:
                    valor1, valor2 = Valores()
                    if valor1 is not None:
                        print(f"Resultado: {Restar(valor1, valor2)}")
                case 3:
                    valor1, valor2 = Valores()
                    if valor1 is not None:
                        print(f"Resultado: {Multiplicar(valor1, valor2)}")
                case 4:
                    valor1, valor2 = Valores()
                    if valor1 is not None:
                        print(f"Resultado: {Dividir(valor1, valor2)}")
                case 5:
                    valor1, valor2 = Valores()
                    if valor1 is not None:
                        print(f"Resultado: {Potencia(valor1, valor2)}")
                case 6:
                    valor1 = input("Ingrese un número: ")
                    if ValidNumber(valor1):
                        valor1 = int(valor1)
                        print(f"Resultado: {RaizCuadrada(valor1)}")
                    else:
                        print("Ingrese solo números válidos")
                case 7:
                    print("Saliendo de la calculadora...")
                    break
                case _:
                    print("Opción inválida")
        else:
            print("Ingrese solo números enteros")