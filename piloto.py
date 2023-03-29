import requests

class Piloto():
    def __init__(self, id_piloto, numero_permanente, codigo, nombre_equipo, nombre_piloto, apellido_piloto, fecha_de_nacimiento, nacionalidad_piloto, puntaje):
        self.id_piloto = id_piloto
        self.numero_permanente = numero_permanente
        self.codigo = codigo
        self.nombre_equipo = nombre_equipo
        self.nombre_piloto = nombre_piloto
        self.apellido_piloto = apellido_piloto
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.nacionalidad_piloto = nacionalidad_piloto
        self.puntaje=puntaje

    def leer_piloto():
        piloto_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json')
        piloto_url = piloto_url.json()
        lista_piloto=[]
        for x in piloto_url:
            piloto=Piloto(x['id'], x['permanentNumber'], x['code'], x['team'], x['firstName'], x['lastName'], x['dateOfBirth'], x['nationality'], 0)
            lista_piloto.append(piloto)
        return lista_piloto

    def mostrar_piloto(self):
        print(f' Nombre: {self.nombre_piloto}\n Apellido: {self.apellido_piloto}\n Fecha de nacimiento: {self.fecha_de_nacimiento}\n Lugar de nacimiento: {self.nacionalidad_piloto}\n Numero: {self.numero_permanente}\n Puntaje: {self.puntaje}\n\n\n')