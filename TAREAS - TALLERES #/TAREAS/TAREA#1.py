import datetime
from CALCULADORA import SistemaCalculadora

def ValidNumber(number):
    return number.lstrip("-").isdigit()

def Saludo(name):
    return f"Bienvenido {name}"

def Suma(num1, num2):
    return num1 + num2

def DobleTriple(number):
    return f"El doble es {number * 2}\nEl triple es {number * 3}"

def AreaRectangulo(base, altura):
    return base * altura

def CelsiusFahrenheit(cel):
    return (cel * 9/5) + 32

def MayorEdad(edad):
    return (
        f"Es mayor de edad ({edad})"
        if edad >= 18
        else f"No es mayor de edad ({edad})"
    )

def NumeroMayor(num1, num2):
    if num1 > num2:
        return f"{num1} es mayor que {num2}"
    elif num2 > num1:
        return f"{num2} es mayor que {num1}"
    else:
        return "Ambos números son iguales"

def CalcularPromedio(notas):
    return sum(notas) / len(notas)

def ParImpar(number):
    return (
        f"{number} es par"
        if number % 2 == 0
        else f"{number} es impar"
    )

def TipoNumero(number):
    if number > 0:
        return "El número es positivo"
    elif number < 0:
        return "El número es negativo"
    else:
        return "El número es cero"

def DescuentoCompra(compra):
    if compra > 100 and compra < 150:
        descuento = compra * 0.10
    elif compra >= 150:
        descuento = compra * 0.15
    else:
        descuento = 0
    total = compra - descuento
    return (
        f"El valor de la compra es {compra}\n"
        f"El descuento es {descuento}\n"
        f"El total a pagar es {total}"
    )

def CategoriaEdad(edad):
    if edad <= 12:
        return f"Tu edad actual es {edad}, eres un niño"
    elif edad >= 13 and edad <= 17:
        return f"Tu edad actual es {edad}, eres un joven"
    else:
        return f"Eres un adulto, tienes la edad actual de {edad}"

def ValidAcces(user_db, password_db, user, password):
    return (
        "Acceso permitido"
        if user.lower() == user_db and password == password_db
        else "Acceso denegado"
    )

def AñoBisiesto(year):
    return (
        f"El año {year} si es bisiesto"
        if year % 400 == 0 or year % 100 != 0 and year % 4 == 0
        else f"El año {year} no es bisiesto"
    )

def MayorTresNumeros(nums):
    return max(nums)

def ResultadoNotas(nota):
    if nota < 0 or nota > 10:
        return "La nota debe estar entre 0 y 10"
    if nota >= 9:
        return f"El estudiante tiene la nota de {nota} y el resultado es A (Excelente)"
    elif nota >= 7:
        return f"El estudiante tiene la nota de {nota} y el resultado es B (Bueno)"
    elif nota >= 5:
        return f"El estudiante tiene la nota de {nota} y el resultado es C (Regular)"
    else:
        return f"El estudiante tiene la nota de {nota} y el resultado es D (Reprobado)"

def ContarPositivos(numeros):
    positivos = 0
    for numero in numeros:
        if numero > 0:
            positivos += 1
    return positivos

def AdivinarNumero(adivinar, numero):
    if adivinar == numero:
        return f"Felicidades encontraste el número {adivinar}"
    elif numero > adivinar:
        return f"Estás cerca, te pasaste un poco {numero}"
    else:
        return f"Estás lejos, un poco más adelante quizás {numero}"

def EsPrimo(numero):
    if numero <= 1:
        return f"No es primo ({numero})"
    for i in range(2, numero):
        if numero % i == 0:
            return f"No es primo ({numero})"
    return f"Es primo ({numero})"

def Factorial(n):
    return 1 if n == 1 else n * Factorial(n - 1)

def MenuExercices():
    print("========== MENÚ ==========")
    print("1. Solicitar el nombre del usuario y mostrar un saludo.")
    print("2. Pedir dos números y mostrar su suma.")
    print("3. Pedir un número y mostrar su doble y triple.")
    print("4. Solicitar los lados de un rectángulo y calcular su área.")
    print("5. Convertir grados Celsius a Fahrenheit.")
    print("6. Pedir edad y mostrar si es mayor de edad.")
    print("7. Comparar dos números y mostrar cuál es mayor.")
    print("8. Calcular el promedio de 3 notas.")
    print("9. Determinar si un número es par o impar.")
    print("10. Determinar si un número es positivo, negativo o cero.")
    print("11. Calcular descuento según monto de compra.")
    print("12. Validar edad y mostrar categoría.")
    print("13. Validar usuario y contraseña.")
    print("14. Presentar menú con opciones básicas.")
    print("15. Validar si un año es bisiesto.")
    print("16. Calcular el mayor de 3 números.")
    print("17. Evaluar nota de estudiante.")
    print("18. Usar operador ternario para validar acceso.")
    print("19. Mostrar números del 1 al 10 con for.")
    print("20. Sumar números hasta ingresar 0.")
    print("21. Mostrar tabla de multiplicar.")
    print("22. Contar números positivos en un arreglo.")
    print("23. Juego de adivinar número.")
    print("24. Crear función para calcular promedio.")
    print("25. Función para determinar número primo.")
    print("26. Función recursiva para factorial.")
    print("27. Sistema completo de calculadora.")
    print("==========================")

    menu = input("Ingrese la opcion del menu: ")

    if ValidNumber(menu):
        menu = int(menu)

        match menu:

            case 1:
                name = input("Ingrese su nombre: ")
                if name.isalpha():
                    print(Saludo(name))
                else:
                    print("Ingrese solo letras")

            case 2:
                num1 = input("Ingrese el primer numero: ")
                num2 = input("Ingrese el segundo numero: ")
                if ValidNumber(num1) and ValidNumber(num2):
                    print(f"La suma es {Suma(int(num1), int(num2))}")
                else:
                    print("Ingrese números enteros")

            case 3:
                number = input("Ingrese un numero: ")
                if ValidNumber(number):
                    print(DobleTriple(int(number)))
                else:
                    print("Ingrese números enteros")

            case 4:
                base = input("Ingrese la base: ")
                altura = input("Ingrese la altura: ")
                if ValidNumber(base) and ValidNumber(altura):
                    print(f"El área es {AreaRectangulo(int(base), int(altura))}")
                else:
                    print("Ingrese números enteros")

            case 5:
                cel = input("Ingrese grados Celsius: ")
                if ValidNumber(cel):
                    print(f"{cel}°C = {CelsiusFahrenheit(int(cel))}°F")
                else:
                    print("Ingrese números enteros")

            case 6:
                edad = input("Ingrese su edad: ")
                if ValidNumber(edad):
                    print(MayorEdad(int(edad)))
                else:
                    print("Ingrese números enteros")

            case 7:
                num1 = input("Ingrese el primer numero: ")
                num2 = input("Ingrese el segundo numero: ")
                if ValidNumber(num1) and ValidNumber(num2):
                    print(NumeroMayor(int(num1), int(num2)))
                else:
                    print("Ingrese números enteros")

            case 8:
                notas = []
                for i in range(3):
                    nota = input(f"Ingrese la nota {i + 1}: ")
                    if ValidNumber(nota):
                        notas.append(int(nota))
                    else:
                        print("Ingrese números enteros")
                if len(notas) == 3:
                    print(f"El promedio es {CalcularPromedio(notas)}")

            case 9:
                number = input("Ingrese un numero: ")
                if ValidNumber(number):
                    print(ParImpar(int(number)))
                else:
                    print("Ingrese números enteros")

            case 10:
                number = input("Ingrese un numero: ")
                if ValidNumber(number):
                    print(TipoNumero(int(number)))
                else:
                    print("Ingrese números enteros")

            case 11:
                compra = input("Ingrese el total de su compra: ")
                if ValidNumber(compra):
                    print(DescuentoCompra(int(compra)))
                else:
                    print("Ingrese números enteros")

            case 12:
                edad = input("Ingrese tu edad actual: ")
                if ValidNumber(edad):
                    print(CategoriaEdad(int(edad)))
                else:
                    print("Ingrese números enteros")

            case 13:
                user = input("Ingrese tu nombre de usuario: ")
                password = input("Ingrese tu contraseña: ")
                print(ValidAcces("isaac", "python123", user, password))

            case 14:
                print("===== MENÚ =====")
                print("1. SALUDAR")
                print("2. MOSTRAR FECHA")
                print("3. SALIR")

                option = input("Selecciona una opción: ")

                if ValidNumber(option):
                    option = int(option)

                    match option:
                        case 1:
                            name = input("Ingrese su nombre: ")
                            if name.isalpha():
                                print(Saludo(name))
                            else:
                                print("Ingrese solo letras")

                        case 2:
                            print(datetime.datetime.now())

                        case 3:
                            print("Saliendo del programa.")

                        case _:
                            print("Opción inválida")
                else:
                    print("Ingrese números enteros")

            case 15:
                year = input("Ingrese un año: ")
                if ValidNumber(year):
                    print(AñoBisiesto(int(year)))
                else:
                    print("Ingrese números enteros")

            case 16:
                nums = []
                for i in range(3):
                    num = input(f"Ingrese el numero {i + 1}: ")
                    if ValidNumber(num):
                        nums.append(int(num))
                    else:
                        print("Ingrese números enteros")
                if len(nums) == 3:
                    print(f"El número mayor es {MayorTresNumeros(nums)}")

            case 17:
                nota = input("Ingrese la nota: ")
                if ValidNumber(nota):
                    print(ResultadoNotas(int(nota)))
                else:
                    print("Ingrese números enteros")

            case 18:
                user = input("Ingrese el usuario: ")
                password = input("Ingrese la contraseña: ")
                print(ValidAcces("isaac", "python123", user, password))

            case 19:
                for i in range(1, 11):
                    print(i)

            case 20:
                suma = 0
                while True:
                    number = input("Ingrese números a sumar (0 para salir): ")
                    if ValidNumber(number):
                        number = int(number)
                        if number == 0:
                            break
                        suma += number
                    else:
                        print("Ingrese números enteros")
                print(f"La suma total es {suma}")

            case 21:
                numero = input("Ingrese un numero: ")
                if ValidNumber(numero):
                    numero = int(numero)
                    for i in range(1, 13):
                        print(f"{numero} * {i} = {numero * i}")
                else:
                    print("Ingrese números enteros")

            case 22:
                arreglo = input("Ingrese la longitud del arreglo: ")
                if ValidNumber(arreglo):
                    arreglo = int(arreglo)
                    numeros = []

                    for i in range(arreglo):
                        numero = input(f"Ingrese el número {i + 1}: ")

                        if ValidNumber(numero):
                            numeros.append(int(numero))
                        else:
                            print("Ingrese números enteros")

                    print(f"Cantidad de positivos: {ContarPositivos(numeros)}")
                else:
                    print("Ingrese números enteros")

            case 23:
                adivinar = 999
                numero = input("Ingrese un numero: ")

                if ValidNumber(numero):
                    print(AdivinarNumero(adivinar, int(numero)))
                else:
                    print("Ingrese números enteros")

            case 24:
                notas = []

                for i in range(3):
                    nota = input(f"Ingrese la nota {i + 1}: ")

                    if ValidNumber(nota):
                        notas.append(int(nota))
                    else:
                        print("Ingrese números enteros")

                if len(notas) == 3:
                    print(f"El promedio es {CalcularPromedio(notas)}")

            case 25:
                numero = input("Ingrese un numero: ")

                if ValidNumber(numero):
                    print(EsPrimo(int(numero)))
                else:
                    print("Ingrese números enteros")

            case 26:
                numero = input("Ingrese un factorial: ")

                if ValidNumber(numero):
                    print(Factorial(int(numero)))
                else:
                    print("Ingrese números enteros")

            case 27:
                SistemaCalculadora()

            case _:
                print("Opción inválida")

    else:
        print("Ingrese solo números en el menú")

MenuExercices()