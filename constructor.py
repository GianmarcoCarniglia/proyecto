import requests

class Constructor():
    def __init__(self, nombre_equipo, id_equipo, nacionalidad, puntaje, pilotos):
        self.nombre_equipo = nombre_equipo
        self.id_equipo = id_equipo
        self.nacionalidad = nacionalidad
        self.puntaje = puntaje
        self.pilotos=pilotos
        # preguntar self.referencia_pilotos = referencia_pilotos

    def leer_constructor():
        constructor_url = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json')
        constructor_url = constructor_url.json()
        lista_constructor=[]
        for x in constructor_url:
            constructor=Constructor(x['name'], x['id'], x['nationality'], 0, [])
            lista_constructor.append(constructor)
        return lista_constructor

    def mostrar_constructor(i):
        print(f' Equipo: {i.nombre_equipo}\n Numero de equipo: {i.id_equipo}\n Pais del equipo: {i.nacionalidad}\n Puntaje: {i.puntaje}\n\n\n')