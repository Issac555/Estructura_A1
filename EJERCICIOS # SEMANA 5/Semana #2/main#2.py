#define un total de compras, saca el iva y el valor toda de este


def BuyPrice(price):
    priceVAT = price * 0.15
    priceTotal = price + priceVAT
    return price, priceVAT, priceTotal
price, vat, total = BuyPrice(100)
print(f"The price is {price}, the VAT is {vat}, total is {total}")


#defina un tiempo de llamada, los 5 primeros tiene un valor y si se sobre pasa esos minutos tengan otro precio

def call_cost(minutes):
    base_price = 0.50
    extra_price = 0.30

    if minutes <= 5:
        total = minutes * base_price
    else:
        total = (5 * base_price) + ((minutes - 5) * extra_price)

    return total

# Crea un programa en Python que calcule el costo de un parqueadero según estas reglas:
#
# 📋 Reglas
# La primera hora cuesta $1.00
# Las siguientes horas (hasta 5 horas) cuestan $0.75 cada una
# Si pasa de 5 horas, cada hora adicional cuesta $0.50
# El máximo a pagar es $10.00

def parking_cost(hours):
    if hours <= 1:
        total = 1.00

    elif hours <= 5:
        total = 1.00 + (hours - 1) * 0.75

    else:
        total = 1.00 + (4 * 0.75) + (hours - 5) * 0.50

    # aplicar máximo
    if total > 10:
        total = 10.00

    return total

# Uso for

names = ["Ana", "Marcela", "Isaac", "Marta", "Diego"]
for i in names:
    print(i)


#suma
numeros = [4, 7, 2, 9, 1]
suma = 0
for i in numeros:
    suma = suma + i
print("La suma es:", suma)


#mayor
mayor = 1
for i in numeros:
    if i >= mayor:
        mayor = i
print("La mayor es:", mayor)

#pares

par = 0
for i in numeros:
    if i % 2 == 0:
        par = par + 1
print(f"Los pares son {par}")

# aprovado
notas = [7, 3, 9, 5, 10]
aprobados = 0
reprobados = 0
for i in notas:
    if i >= 7:
        aprobados = aprobados + 1
        print(f"Aprovado con {i}")
    else:
        reprobados = reprobados + 1
        print(f"Reprovado con {i}")
print(f"El total de reprobados {reprobados} y aprobados {aprobados}")

# nombres mayuscula
nombres = ["juan", "maria", "pedro"]

for i in nombres:
    print(f"El nombre es {i.upper()}")

# pares y impares en diferente lista
numbers = [8, 9, 7, 10, 6]
pares = []
impares = []
for i in numbers:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"Los pares son {pares} y los impares son {impares}")

#contar palabras
palabras = ["hola", "python", "casa"]

c = 0
for i in palabras:
    for letras in i:
        c = c + 1
print(f"Total de letras {c}")


## Menu productos

product = ["Leche", "Azucar", "Arroz", "Pan"]


def ShownProducts():
    for i in product:
        print(f"Productos disponibles: {i}")
ShownProducts()

def AddProducts(name):
    product.append(name)
    print(f"Se añadio el producto {name}")
    for i in product:
        print(f"Productos disponibles es: {i}")
AddProducts(name = input("Ingrese su nombre: "))

def DeleteProducts(name):
    product.remove(name)
    for i in product:
        print(f"Productos disponibles es: {i}")
DeleteProducts(name = input("Ingrese su nombre: "))