# Un diccionario guarda datos en:
# clave : valor

usuario = {
    "nombre": "Isaac",
    "edad": 19,
    "pais": "Ecuador"
}


# =========================
# ACCEDER A VALORES
# =========================

# Sirve para obtener un valor usando la clave

print(usuario["nombre"])

# Resultado:
# Isaac


# =========================
# MODIFICAR VALORES
# =========================

# Sirve para cambiar un valor

usuario["nombre"] = "Juan"

print(usuario)


# =========================
# AGREGAR NUEVOS DATOS
# =========================

# Sirve para agregar una nueva clave

usuario["correo"] = "juan@gmail.com"

print(usuario)


# =========================
# DEL
# =========================

# Sirve para eliminar una clave

del usuario["pais"]

print(usuario)


# =========================
# KEYS()
# =========================

# Sirve para obtener SOLO las claves

print(usuario.keys())

# Resultado:
# dict_keys(['nombre', 'edad', 'correo'])


# =========================
# VALUES()
# =========================

# Sirve para obtener SOLO valores

print(usuario.values())

# Resultado:
# dict_values(['Juan', 19, 'juan@gmail.com'])


# =========================
# ITEMS()
# =========================

# Sirve para obtener:
# clave y valor

print(usuario.items())

# Resultado:
# dict_items([('nombre', 'Juan'), ('edad', 19)])


# =========================
# RECORRER ITEMS()
# =========================

# Recorre clave y valor

for clave, valor in usuario.items():

    print(clave, valor)


# Resultado:
# nombre Juan
# edad 19


# =========================
# GET()
# =========================

# Sirve para obtener valores
# evitando errores

print(usuario.get("nombre"))

# Resultado:
# Juan


# Si la clave NO existe:
print(usuario.get("telefono"))

# Resultado:
# None


# =========================
# POP()
# =========================

# Sirve para eliminar una clave específica

usuario.pop("edad")

print(usuario)


# =========================
# CLEAR()
# =========================

# Sirve para vaciar TODO el diccionario

usuario.clear()

print(usuario)

# Resultado:
# {}