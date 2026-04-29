
numb = int(input("Ingresa la temperatura de clima actual"))

def CheckTemp(temp):
    if temp < 10:
        return print(f"El clima es frio {temp}")
    elif temp >= 10 and temp < 25:
        return print(f"El clima esta templado {temp}")
    elif temp >= 25 and temp < 35:
        return print(f"El clima es caluroso {temp}")
    else:
        return print(f"El clima es extramadamente caluroso {temp}")

CheckTemp(numb)


# 2 - 2. Solicitar al usuario que ingrese el total de una llamada en minutos.
# Los primeros 5 minutos de la llamada tiene x valor, pasado del 5 minuto ese valor incrementa.


name_user = input("Ingresa tu nombre de tu usuario")
time_call = int(input("Ingresa el tiempo de llamada"))


def CheckTimeCall(time, name):

    max_time = 5
    if time > max_time:
        subtraction = time - max_time
        cash_min = max_time * 0.25
        cash_max = subtraction * 0.50
        print(f"Bienvenido {name} al sistema de saldo")
        print(f"El total de los 5 primeros minutos son {cash_min} y el valor de tiempo añadido ({subtraction}) es de {cash_max}")
        print(f"El total a pagar es de { cash_max + cash_min}")
    else:
        cash_min = max_time * 0.25
        print(f"Bienvenido {name} al sistema de saldo")
        print(f"El total de los 5 primeros minutos son {cash_min}, total a pagar es de {cash_min}")

CheckTimeCall(time_call, name_user)