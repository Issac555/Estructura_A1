bass = 3

print(type(bass))

a = "Isaac"
f = "Vega"
e = "19"
c = "Guayaquil"
i = "5"

print("Mi nombre es" + a + "" + f + "tengo " + e + "años" + "Soy de la ciudad de " + c + "y somos " + i + "integrantes de mi familia")


def sumar(a, b):
    return a + b
resultado = sumar(3, 2)
print(resultado)


def mayorEdad(a):
    if a < 18:
        return print("Es menor de edad")
    else :
        return print("Es mayor de edad")

mayorEdad(19)
