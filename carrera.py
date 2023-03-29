import requests

class Carrera():
    def __init__(self, ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos):
        self.ronda = ronda
        self.nombre_carrera = nombre_carrera
        self.fecha_carrera = fecha_carrera
        self.mapa = mapa
        self.podio = podio
        self.asistencia = asistencia
        self.boletos_vendidos = boletos_vendidos
        self.mapa_vendidos = mapa_vendidos

    def leer_carrera():
        carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
        carrera_url = carrera_url.json()
        lista_carrera=[]
        for x in carrera_url:
            carrera=Carrera(x['round'], x['name'], x['date'], x['map'], False, 0, 0, [])
            lista_carrera.append(carrera)
        return lista_carrera
    
    def mostrar_carrera(self):
        print(f' Ronda: {self.ronda}\n Nombre de la carrera: {self.nombre_carrera}\n Fecha de carrera: {self.fecha_carrera}\n\n\n\n')


class Circuito(Carrera):
    def __init__(self, ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos, id_circuito, nombre_circuito):
        super().__init__(ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos)
        self.id_circuito = id_circuito
        self.nombre_circuito = nombre_circuito

    def leer_circuito():
        carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
        carrera_url = carrera_url.json()
        lista_circuito=[]
        for x in carrera_url:
            circ= x['circuit']
            circuito=Circuito(x['round'], x['name'], x['date'], x['map'], False, 0, 0, [], circ['circuitId'], circ['name'])
            lista_circuito.append(circuito)
        return lista_circuito
    
    def mostrar_circuito(self):
        print(f' Ronda: {self.ronda}\n Nombre de la carrera: {self.nombre_carrera}\n Fecha de carrera: {self.fecha_carrera}\n ID de circuito: {self.id_circuito}\n Nombre de circuito: {self.nombre_circuito}\n\n\n\n')
    

class Location(Circuito):
    def __init__(self, ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos, id_circuito, nombre_circuito, latitud, longitud, location_circuito, pais):
        super().__init__(ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos, id_circuito, nombre_circuito)
        self.latitud = latitud
        self.longitud = longitud
        self.location_circuito = location_circuito
        self.pais = pais
        
    def leer_location():
        carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
        carrera_url = carrera_url.json()
        lista_location=[]
        for x in carrera_url:
            loc= x['circuit']['location']
            circ= x['circuit']
            location=Location(x['round'], x['name'], x['date'], x['map'], False, 0, 0, [], circ['circuitId'], circ['name'], loc['lat'], loc['long'], loc['locality'], loc['country'])
            lista_location.append(location)
        return lista_location
    
    def mostrar_location(self):
        print(f' Ronda: {self.ronda}\n Nombre de la carrera: {self.nombre_carrera}\n Fecha de carrera: {self.fecha_carrera}\n ID de circuito: {self.id_circuito}\n Nombre de circuito: {self.nombre_circuito}\n Pais: {self.pais}\n Localidad: {self.location_circuito}\n Latitud: {self.latitud}\n Longitud: {self.longitud}\n\n\n\n')
    


class Restaurante(Carrera):
    def __init__(self, ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos, nombre_restaurante):
        super().__init__(ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos)
        self.nombre_restaurante = nombre_restaurante

    def leer_restaurante():
        carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
        carrera_url = carrera_url.json()
        lista_restaurante=[]
        for x in carrera_url:
            rest= x['restaurants']
            restaurante=Restaurante(x['round'], x['name'], x['date'], x['map'], False, 0, 0, [], rest['name'])
            lista_restaurante.append(restaurante)
        return lista_restaurante
    
    def mostrar_restaurante(self):
        print(f' Ronda: {self.ronda}\n Nombre de la carrera: {self.nombre_carrera}\n Fecha de carrera: {self.fecha_carrera}\n Nombre de restaurante: {self.nombre_restaurante}\n\n\n\n')
    





class Producto(Restaurante):
    def __init__(self, ronda, nombre_carrera, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos, nombre_restaurante, nombre_producto, tipo_producto, precio_producto):
        super().__init__(ronda, nombre_carrera, nombre_restaurante, fecha_carrera, mapa, podio, asistencia, boletos_vendidos, mapa_vendidos)
        self.nombre = nombre_producto
        self.tipo = tipo_producto
        self.precio = precio_producto

    def leer_producto():
        carrera_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
        carrera_url = carrera_url.json()
        lista_producto=[]
        for x in carrera_url:
            rest= x['restaurants']
            for r in rest:
                prod = r['items']
                for p in prod:
                    producto=Producto(x['round'], x['name'], x['date'], x['map'], False, 0, 0, [], r['name'], p['name'], p['type'], p['price'])
                lista_producto.append(producto)
        return lista_producto




    def mostrar_producto(self):
        print(f' Nombre Restaurante: {self.nombre_restaurante}\n Producto: {self.nombre_producto}\n Tipo de producto: {self.tipo_producto}\n Precio: {self.precio_producto}\n\n\n\n')
              