# Cuenta cuántas veces existe un valor

numeros = [1, 2, 2, 3]

print(numeros.count(2))

# Obtiene posición de un valor

numeros = [5, 8, 10]

print(numeros.index(8))

# Recorre elementos uno a uno

notas = [8, 7, 10]

for nota in notas:
    print(nota)


# Obtiene índice y valor

for i, nota in enumerate(notas):
    print(i, nota)


# Busca elementos

notas = [8, 7, 10]

if 7 in notas:
    print("Existe")


# Ordena listas

numeros = [5, 1, 9]
numeros.sort()

print(numeros)


texto = "hola"

print(texto.upper())