bass = 3

print(type(bass))

def Elderly(age):
    if age > 18 and age % 2 == 0: #Detecta si es mayor de edad y es divisible
        print("Is he/she of legal age and is divisible by two")
    elif age > 18 and age % 2 != 0: #Detecta si es menor de edad y no es divible
        print("Is he/she of legal age and is not divisible by two")
    elif age <= 18 and age % 2 == 0: #Detecta si es menor o igual y si es divisible
        print("He/she is not of legal age and is divisible by two")
    else: #Detecta que no es mayor de edad y no es divible
        print("He/she is not of legal age and is not divisible by two")

Elderly(20)