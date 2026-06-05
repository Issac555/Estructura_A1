computadora = {
     "marca" : "ThinkCentre",
     "procesador" : "Intel Core 7",
     "RAM": 16,
     "alamacenamiento": "1T de espacio",
     "case" : "negro",
     "pantalla" : "DELL",
     "mouse" : "negro",
     "teclado" : "negro"     
}

aire = {
     "marca" : "LG",
     "btu" : 36,
     "color" : "blanco"
}

router = {
     "marca" : "Claro",
     "alcance" : 350
}

laboratorio = {
     "mesa" : "Muebles.SA",
     "silla" : "Muebles.SA",
     "computadora" : computadora,
     "A/C" : aire,
     "internet" : router
}

print(laboratorio["A/C"]["marca"])



#########################################################################

cama = {
     "marca": "AL2SZ",
     "plazas" : 2,
     "color" : "negro"
}

escritorio = {
     "dimensiones" : "100x30",
     "color" : "beige",
     "silla" : "negra",
     "computador" : computadora,
     "router" : router
}

closet = {
     "dimensiones" : "5x7",
     "color" : "blanco",
     "puertas" : 2
}

mascota = {
     "tipo" : "perro",
     "color" : "negro",
     "raza" : "Chihuaha",
     "nombre" : "Rocky"
}

habitacion = {
     "cama" : cama,
     "escritorio": escritorio,
     "closet": closet,
     "mascota" : mascota     
}




#################################DELIVERY####################################


local = {
     "nombre" : "KFC - MALL DEL SOL",
     "tipo" : "Fast Food",
     "metodos" : ["efectivo", "debito", "credito"],
     "presa" : ["crispy", "original"],
     "ubicacion" : "MALL DEL SOL P/B"
}


empleador = {
     "nombre" : "Neixer Obregon",
     "vehiculo" : "bicicleta",
     "metodo" : "Efectivo",
     "ubcicacion" : local["ubicacion"]
}

pedido = {
     
     "delivery" : empleador,
     "estado" : "En camino",
     "tiempo" : 5,
     "propina" : "3%", 
     "compra" : "MARTES LOCO KFC - 9 presas por 10.00$",
     "precio" : 10,
     "metodo" : "Efectivo"
     
}


cliente = {
     "nombre" : "GOL D ROGER",
     "DNI" : "0999332211",
     "lugar" : "KFC",
     "direc" : "Martha de Roldos",
     "metodos" : ["efectivo", "transferencias"],
     "estado": pedido
     
}

class local:
     def __init__(self, nombre, direccion, tiempo_espera, tipo_comida, hora_apertura, hora_cierre):
         self.nombre = nombre
         self.direccion = direccion
         self.tiempo_espera = tiempo_espera
         self.tipo_comida = tipo_comida
         self.hora_apertura = hora_apertura
         self.hora_cierre = hora_cierre

         print(nombre, direccion, tiempo_espera,
               tipo_comida, hora_apertura, hora_cierre)
     def __str__(self):
        return f""
     
local3 = local('rukito', 'Av.25 Julio', 5, 'DRIKN & GRILL', 10, 22)
print(local3)
class Colaborador:
     def __init__(self, nombre, numero, nacionalidad, tipo_vehiculo):
          self.nombre = nombre
          self.numero = numero
          self.nacionalidad = nacionalidad
          self.tipo_vehiculo = tipo_vehiculo
          
          print(nombre, numero, nacionalidad, tipo_vehiculo)
       
nuevo_colaborador = Colaborador("Neixer", 15325435, "Indio", "Bus")


