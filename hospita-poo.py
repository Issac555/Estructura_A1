import datetime


class Hospital:

    def __init__(self, nombre, direccion, camillas, medicos, enfermeros,
                 vehiculos, pacientes, capacidad, habitaciones,
                 areas, sillas, medicinas, equipos):

        self.nombre = nombre
        self.direccion = direccion
        self.camillas = camillas
        self.medicos = medicos
        self.enfermeros = enfermeros
        self.vehiculos = vehiculos
        self.pacientes = pacientes
        self.capacidad = capacidad
        self.habitaciones = habitaciones
        self.areas = areas
        self.sillas = sillas
        self.medicinas = medicinas
        self.equipos = equipos
        self.luz = True

    def mostrar_informacion(self):
        print("======== HOSPITAL ========")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Capacidad:", self.capacidad)
        print("Luz:", self.luz)

        print("\n--- Camillas ---")
        print(self.camillas)

        print("\n--- Médicos ---")
        print(self.medicos)

        print("\n--- Enfermeros ---")
        print(self.enfermeros)

        print("\n--- Vehículos ---")
        print(self.vehiculos)

        print("\n--- Pacientes ---")
        print(self.pacientes)

        print("\n--- Habitaciones ---")
        print(self.habitaciones)

        print("\n--- Áreas ---")
        print(self.areas)

        print("\n--- Sillas ---")
        print(self.sillas)

        print("\n--- Medicinas ---")
        print(self.medicinas)

        print("\n--- Equipos ---")
        print(self.equipos)


class Camillas:

    def __init__(self, disponibilidad, sistema, movilidad):
        self.disponibilidad = disponibilidad
        self.sistema = sistema
        self.movilidad = movilidad

    def __repr__(self):
        return f"Camilla({self.disponibilidad}, {self.sistema})"

    def __str__(self):
        return f"Disponibilidad: {self.disponibilidad}, Sistema: {self.sistema}, Movilidad: {self.movilidad}"


class Vehiculos:

    def __init__(self, tipo, pasajeros, placa):
        self.tipo = tipo
        self.pasajeros = pasajeros
        self.equipos = []
        self.placa = placa

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def __repr__(self):
        return f"Vehiculo({self.tipo}, {self.placa})"

    def __str__(self):
        return (
            f"Tipo: {self.tipo}\n"
            f"Pasajeros: {self.pasajeros}\n"
            f"Placa: {self.placa}\n"
            f"Equipos: {self.equipos}"
        )


class Habitaciones:

    def __init__(self, capacidad, climatizacion, visitas):
        self.capacidad = capacidad
        self.climatizacion = climatizacion
        self.visitas = visitas

    def __repr__(self):
        return f"Habitacion({self.capacidad})"

    def __str__(self):
        return f"Capacidad: {self.capacidad}, Climatización: {self.climatizacion}, Visitas: {self.visitas}"


class Medico:

    def __init__(self, especialidad, edad, nombre):
        self.especialidad = especialidad
        self.edad = edad
        self.nombre = nombre

    def __repr__(self):
        return f"Medico({self.nombre})"

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Especialidad: {self.especialidad}"


class Paciente:

    def __init__(self, nombre, edad, enfermedad):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad

    def __repr__(self):
        return f"Paciente({self.nombre})"

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Enfermedad: {self.enfermedad}"


class Area:

    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

    def __repr__(self):
        return f"Area({self.nombre})"

    def __str__(self):
        return f"Área: {self.nombre}, Capacidad: {self.capacidad}"


class Silla:

    def __init__(self, cantidad, material):
        self.cantidad = cantidad
        self.material = material

    def __repr__(self):
        return f"Silla({self.cantidad})"

    def __str__(self):
        return f"Cantidad: {self.cantidad}, Material: {self.material}"


class Medicina:

    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def __repr__(self):
        return f"Medicina({self.nombre})"

    def __str__(self):
        return f"Medicamento: {self.nombre}, Stock: {self.stock}"


class Equipo:

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def __repr__(self):
        return f"{self.nombre} ({self.estado})"

    def __str__(self):
        return f"Equipo: {self.nombre}, Estado: {self.estado}"


class HistorialClinico:

    def __init__(self, paciente, fecha, enfermedad, medico):
        self.paciente = paciente
        self.fecha = fecha
        self.enfermedad = enfermedad
        self.medico = medico

    def __str__(self):
        return (
            f"Paciente: {self.paciente.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Enfermedad: {self.enfermedad}\n"
            f"Médico: {self.medico.nombre}"
        )


# ===== OBJETOS =====

camilla1 = Camillas(True, "Hidráulica", True)

medico1 = Medico("Cardiología", 45, "Juan Pérez")

paciente1 = Paciente("Ana López", 30, "Gripe")

habitacion1 = Habitaciones(2, True, True)

area1 = Area("Emergencias", 50)

silla1 = Silla(100, "Plástico")

medicina1 = Medicina("Paracetamol", 500)

equipo1 = Equipo("Oxígeno", "Operativo")
equipo2 = Equipo("Camilla de traslado", "Operativa")
equipo3 = Equipo("Desfibrilador", "Operativo")

ambulancia1 = Vehiculos("Ambulancia", 4, "ABC-123")

ambulancia1.agregar_equipo(equipo1)
ambulancia1.agregar_equipo(equipo2)
ambulancia1.agregar_equipo(equipo3)

historial1 = HistorialClinico(
    paciente1,
    datetime.date.today(),
    paciente1.enfermedad,
    medico1
)

hospital1 = Hospital(
    "Roger & Teresa Hospital",
    "Coop. Amores y Dolores",
    camilla1,
    medico1,
    100,
    ambulancia1,
    paciente1,
    500,
    habitacion1,
    area1,
    silla1,
    medicina1,
    [equipo1, equipo2, equipo3]
)

hospital1.mostrar_informacion()

print("\n======== HISTORIAL CLÍNICO ========")
print(historial1)
