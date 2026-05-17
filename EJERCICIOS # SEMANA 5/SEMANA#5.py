import datetime

def asistente():
  a = 10
  b = 20
  return (a+b)
resp = asistente()
print(resp)

n = input("Nombre: ")
e = int(input("Edad: "))
c = input("Ciudad: ")

def saludi(name, edad, ciudad):
    return f"Hola soy {name}, soy de la ciudad de {ciudad} y tengo {edad} años"

pres = saludi(n, e, c)
print(pres)

def numero():
    number = 10
    bol = False
    if number % 2 == 0:
        bol = True
    else:
        bol = False
    return bol
pres2 = numero()
print(pres2)

def lista():
    b = []
    a = [i for i in range(1, 11)]
    for e in a:
        if e % 2 == 0:
            b.append(e)
    return b

resp = lista()
print(resp)


def nombre():
    names = ["Isaac", "Pedro", "Ismael", "Rock"]
    a = []

    for i in names:
        if len(i) % 2 == 0:
            a.append(i)
    return a

resp = nombre()
print(resp)
