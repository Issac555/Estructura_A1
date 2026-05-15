def ValidNumber(number):
    return number.isdigit()

def MenuExercices():
    print("===== MENÚ =====")
    print("1. Saludo")
    print("2. Suma")
    print("3. Doble y Triple")
    print("4. Área Rectángulo")
    print("5. Celsius a Fahrenheit")
    print("6. Mayor de edad")
    print("7. Número mayor")

    menu = input("Ingrese la opcion del menu: ")

    if ValidNumber(menu):
        menu = int(menu)

        match menu:

            case 1:
                name = input("Ingrese su nombre: ")
                if name.isalpha():
                    print(f"Bienvenido {name}")
                else:
                    print("Ingrese solo letras")
            case 2:
                num1 = input("Ingrese el primer numero: ")
                num2 = input("Ingrese el segundo numero: ")
                if ValidNumber(num1) and ValidNumber(num2):
                    print(f"La suma es {int(num1) + int(num2)}")
                else:
                    print("Ingrese números enteros")
            case 3:
                num1 = input("Ingrese un numero: ")

                if ValidNumber(num1):
                    num1 = int(num1)
                    print(f"El doble es {num1 * 2}")
                    print(f"El triple es {num1 * 3}")
                else:
                    print("Ingrese números enteros")
            case 4:
                base = input("Ingrese la base: ")
                altura = input("Ingrese la altura: ")
                if ValidNumber(base) and ValidNumber(altura):
                    print(f"El área es {int(base) * int(altura)}")
                else:
                    print("Ingrese números enteros")
            case 5:
                cel = input("Ingrese grados Celsius: ")

                if ValidNumber(cel):
                    cel = int(cel)
                    fahrenheit = (cel * 9/5) + 32
                    print(f"{cel}°C = {fahrenheit}°F")
                else:
                    print("Ingrese números enteros")
            case 6:
                edad = input("Ingrese su edad: ")

                if ValidNumber(edad):
                    edad = int(edad)
                    if edad >= 18:
                        print(f"Es mayor de edad ({edad})")
                    else:
                        print(f"No es mayor de edad ({edad})")
                else:
                    print("Ingrese números enteros")
            case 7:
                num1 = input("Ingrese el primer numero: ")
                num2 = input("Ingrese el segundo numero: ")

                if ValidNumber(num1) and ValidNumber(num2):
                    num1 = int(num1)
                    num2 = int(num2)
                    if num1 > num2:
                        print(f"{num1} es mayor que {num2}")
                    elif num2 > num1:
                        print(f"{num2} es mayor que {num1}")
                    else:
                        print("Ambos números son iguales")
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
                    promedio = sum(notas) / len(notas)
                    print(f"Las notas son {notas}")
                    print(f"El promedio es {promedio}")
            case 9:
                num1 = input("Ingrese un numero: ")
                if ValidNumber(num1):
                    num1 = int(num1)

                    if num1 % 2 == 0:
                        print(f"{num1} es par")
                    else:
                        print("Es impar")
                else:
                    print("Ingrese números enteros")
            case 10:
                num1 = input("Ingrese un numero: ")
                if num1.lstrip("-").isdigit():
                    num1 = int(num1)
                    if num1 > 0:
                        print("El número es positivo")
                    elif num1 < 0:
                        print("El número es negativo")
                    else:
                        print("El número es cero")
                else:
                    print("Ingrese un número válido")
            case 11:
                compra = input("Ingrese el total de su compra: ")
                if ValidNumber(compra):
                    compra = int(compra)
                    if compra > 100 and compra < 150:
                        descuento = compra * 0.10
                        total = compra - descuento
                        print(f"El valor de la compra es {compra}")
                        print(f"El descuento es {descuento}")
                        print(f"El total a pagar es {total}")
                    elif compra >= 150:
                        descuento = compra * 0.15
                        total = compra - descuento
                        print(f"El valor de la compra es {compra}")
                        print(f"El descuento es {descuento}")
                        print(f"El total a pagar es {total}")
                    else:
                        print(f"El valor de la compra es {compra}")
                        print("No aplica descuento")
                else:
                    print("Ingrese números enteros")
            case 12:
                edad = input("Ingrese tu edad actual: ")
                if edad.isdigit():
                    edad = int(edad)
                    if edad <= 12:
                        print(f"Tu edad actual es, {edad}, eres un niño ")
                    elif edad > 13 < 18:
                        print(f"Tu edad actual es, {edad}, eres un Joven ")
                    else:
                        print(f"Eres un adulto, tiene la edad actual de {edad} ")
                else:
                    print("Ingrese un número válido")
            case 13:
                user_db = "isaac"
                password_db = "python123"
                contador = 0
                while  contador < 3:
                    user = input("Ingrese tu nombre de usuario: ")
                    password = input("Ingrese tu contraseña: ")
                    if user.isalpha():
                        if user.lower() == user_db and password == password_db:
                            print("Accedo permitido")
                            break
                        else:
                            contador += 1
                            print(f"Accedo denegado ({contador}/3)")
                    else:
                        print("Ingrese solo letras en el usuario")
            case 14:
                year = input("Ingresa tu año de nacimiento:")
                if ValidNumber(year):
                    year = int(year)
                    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
                        print(f"El año si es bisiesto ({year})")
                    else:
                        print(f"El año no es bisiesto({year}")
                else:
                    print("Ingrese numeros enteros")
            case _:
                print("Opción inválida")

    else:
        print("Ingrese solo números en el menú")

MenuExercices()