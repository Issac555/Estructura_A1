# =========================
# upper()
# =========================

# .upper()
# Convierte texto a mayúsculas

texto = "hola"

print(texto.upper())


# =========================
# lower()
# =========================

# .lower()
# Convierte texto a minúsculas

texto = "HOLA"

print(texto.lower())


# =========================
# replace()
# =========================

# .replace()
# Reemplaza texto

texto = "Hola Juan"

print(texto.replace("Juan", "Pedro"))


# =========================
# isdigit()
# =========================

# .isdigit()
# Verifica si son números

numero = "123"

print(numero.isdigit())


# =========================
# isalpha()
# =========================

# .isalpha()
# Verifica si son letras

texto = "Juan"

print(texto.isalpha())


# =========================
# lstrip()
# =========================

# .lstrip()
# Elimina caracteres al inicio

numero = "-15"

print(numero.lstrip("-"))


# =========================
# split()
# =========================

# .split()
# Divide texto en lista

texto = "Juan Pedro Maria"

print(texto.split())


# =========================
# join()
# =========================

# .join()
# Une listas en texto

nombres = ["Juan", "Pedro"]

print(" - ".join(nombres))


# =========================
# strip()
# =========================

# .strip()
# Elimina espacios al inicio y final

texto = "   hola   "

print(texto.strip())


# =========================
# startswith()
# =========================

# .startswith()
# Verifica cómo inicia texto

texto = "Hola"

print(texto.startswith("H"))


# =========================
# endswith()
# =========================

# .endswith()
# Verifica cómo termina texto

texto = "Hola"

print(texto.endswith("a"))


# =========================
# find()
# =========================

# .find()
# Busca posición de un texto

texto = "Hola Juan"

print(texto.find("Juan"))


# =========================
# capitalize()
# =========================

# .capitalize()
# Primera letra en mayúscula

texto = "python"

print(texto.capitalize())


# =========================
# title()
# =========================

# .title()
# Convierte cada palabra con inicial mayúscula

texto = "hola mundo"

print(texto.title())


# =========================
# swapcase()
# =========================

# .swapcase()
# Invierte mayúsculas y minúsculas

texto = "Hola"

print(texto.swapcase())


# =========================
# count()
# =========================

# .count()
# Cuenta repeticiones

texto = "hola hola"

print(texto.count("hola"))


# =========================
# center()
# =========================

# .center()
# Centra texto

texto = "Hola"

print(texto.center(10))


# =========================
# zfill()
# =========================

# .zfill()
# Rellena con ceros

numero = "5"

print(numero.zfill(3))


# =========================
# in
# =========================

# in
# Busca elementos

nombres = ["Juan", "Pedro"]

print("Juan" in nombres)


# =========================
# not in
# =========================

# not in
# Verifica que NO exista

nombres = ["Juan", "Pedro"]

print("Maria" not in nombres)


# =========================
# abs()
# =========================

# abs()
# Devuelve valor absoluto

print(abs(-10))


# =========================
# round()
# =========================

# round()
# Redondea números

print(round(10.567, 2))


# =========================
# sorted()
# =========================

# sorted()
# Ordena temporalmente

numeros = [5, 1, 9]

print(sorted(numeros))


# =========================
# zip()
# =========================

# zip()
# Une listas

nombres = ["Juan", "Pedro"]
edades = [19, 20]

print(list(zip(nombres, edades)))