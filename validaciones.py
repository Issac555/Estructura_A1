def campo_vacio(valor):
    return valor is None or str(valor).strip() == ""


def validar_campos_obligatorios(datos):
    for campo, valor in datos.items():
        if campo_vacio(valor):
            return False, f"El campo '{campo}' es obligatorio."

    return True, "Datos válidos."


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje)

        if not campo_vacio(valor):
            return valor

        print("Este campo no puede estar vacío.")


def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)

        try:
            return int(valor)
        except ValueError:
            print("Debe ingresar un número entero válido.")


def pedir_decimal(mensaje):
    while True:
        valor = input(mensaje)

        try:
            return float(valor)
        except ValueError:
            print("Debe ingresar un número decimal válido.")


def generar_id_secuencial(registros):
    if len(registros) == 0:
        return 1

    ultimo_id = max(registro["id"] for registro in registros)
    return ultimo_id + 1
