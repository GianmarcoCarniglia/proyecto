from datetime import datetime
from constructor import Constructor
from piloto import Piloto
from carrera import Carrera, Circuito, Location, Restaurante, Producto
from cliente import Cliente

import matplotlib.pyplot as plt
import random
from tabulate import tabulate

def funcion_menu():
    
    menu= int(input('A continuacion se presentara el menu de las opciones\ndisponibles:\nMarque el numero de la funcion que desea ejecutar\n1. Gestión de carreras y equipo \n2. Gestion de venta de entradas \n3. Gestion de asistencia a las carreras \n4. Gestion de restaurantes\n5. Gestion de venta de restaurantes\n6. Indicadores de gestion (estadisticas)\n7. Grafico \n8.Finalizar\n'))
    if menu==1:
        print('Gestion de carreras y equipo')   
    elif menu==2:
        print('Gestion de venta de entradas')
    elif menu==3:
        print('Gestion de asistencia a las carreras')
    elif menu==4:
        print('Gestion de Restaurantes')
    elif menu==5:
        print('Gestion de venta de Restaurantes')
    elif menu==6:
        print('Indicadores de gestion (estadisticas)')
    elif menu==7:
        print('Ver grafica')
    elif menu==8:
        print('Gracias, ha finalizado')
    else:
        print('Numero invalido')
        funcion_menu()
    return menu

'''Esta funcion va a desplegar las opciones que tiene el cliente'''

def gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location):

    menu=int(input('Marque el numero de la funcion que desee realizar\n 1. Buscar los constructores por país\n 2. Buscar los pilotos por constructor \n 3. Buscar a las carreras por país del circuito \n 4. Buscar todas las carreras que ocurran en un mes \n 5. Finalizar una carrera \n >'))
    if menu==1:
        print('Buscar los constructores por país')
        lista_pais_constructor= []
        for x in lista_constructor:
            print (x.nacionalidad)
        pais= input('Que pais desea buscar, ingrese su nombre exacto:\n>')
        
        
        for x in lista_constructor:
            if x.nacionalidad == pais:
                lista_pais_constructor.append(x)
        if len(lista_pais_constructor)>0:
            print('Los constructores de este pais son:\n')
            for item, y in enumerate(lista_pais_constructor):
                print(item+1)
                y.mostrar_constructor()
        else:
            print('Pais no tiene partidos registrados')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)





    elif menu==2:
        print('Buscar los pilotos por constructor')
       
        for x in lista_constructor:
            print (x.nombre_equipo)
        constructor= input('Que pilotos desea buscar, ingrese el nombre del constructor tal y como sale:\n>')
        
        lista=[]
        for j in lista_constructor:
            if constructor == j.nombre_equipo:
                for x in lista_piloto:
                    if j.id_equipo==x.nombre_equipo:
                        lista.append(x)
        if len(lista)> 0:
            for x in lista:
                x.mostrar_piloto()
        else:
            print('Constructor no existente')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
                #revisar los demas ifs
           





    elif menu==3:
        print('Buscar a las carreras por país del circuito')
        
        for i in lista_location:
            print(i.pais)

        pais_circuito= input('Que pais desea buscar, ingrese el nombre del pais exacto:\n')
        print('Las carreras que se van a correr en este pais son:\n')
        lista_2=[]
        for x in lista_location:
            if x.pais == pais_circuito:
                lista_2.append(x)
        if len(lista_2)> 0:
            for x in lista_2:
                x.mostrar_location()
        else:
            print('Pais no tiene circuitos registrados')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)


    elif menu==4:
        print('Buscar todas las carreras que ocurran en un mes')
        fecha=input('Ingrese el mes que desea buscar, en el formato 00\n Ejemplo: para escribir enero escribo "01"\n>')
        lista_3=[]
        separacion=[]
        # for i in lista_carrera:
        #     separacion.append(i.fecha_carrera)
        # for i in separacion:
        #     i.split('-')
        #     # ['ano', 'mes','dia']4
        #     if i[1]==fecha:
        #         lista_3.append(x)
        for i in lista_carrera:
            datetime_object = datetime.strptime(i.fecha_carrera, '%Y-%m-%d')
            if datetime_object.month == int(fecha):
                lista_3.append(i)
        if len(lista_3)> 0:
            for i in lista_3:
                i.mostrar_carrera()
        else:
            print('Mes no tiene circuitos registrados')
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
    elif menu==5:
        get_podio(lista_piloto, lista_carrera, lista_constructor)
    else:
        print('Numero invalido')
        gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
    return



'''Funcion para obtener el podio de una carrera'''
def get_podio(pilotos, carreras, constructores):
    puntaje = {1:25,2:18,3:15,4:12,5:10,6:8,7:6,8:4,9:2,10:1}
    print('\nCarreras sin finalizar:')
    n_invalidos = []
    for i,carrera in enumerate(carreras):
        if carrera.podio == False:
            print('\t',i+1,carrera.nombre_carrera)
        else:
            n_invalidos.append(i+1)
    if len(n_invalidos) != len(carreras):
        choice = input('\nIngrese el numero correspondiente a la carrera a finalizar:\n>> ')
        while not choice.isnumeric() or int(choice) not in range (1,len(carreras)+1) or int(choice) in n_invalidos:
            choice = input('\nERROR - Opcion invalida\nPor favor ingrese el numero correspondiente a la carrera a finalizar:\n>> ')
        podio = random.sample(pilotos, 10)       
        contador = 1
        for piloto in podio:
            piloto.puntaje += puntaje[contador]
            contador += 1
        for constructor in constructores:
            for pilot in constructor.pilotos:
                if pilot in podio:
                    constructor.puntaje += pilot.puntaje
        carreras[int(choice)-1].podio = podio
        print(f"\nPodio final para la carrera {carreras[int(choice)-1].nombre_carrera}")
        l=[]
        for i, piloto in enumerate(podio):
            pi = piloto.nombre_piloto +' '+ piloto.apellido_piloto
            sc= puntaje[i+1]
            d= [i+1 ,pi, sc]
            l.append(d)
        print(tabulate(l,headers=['Posicion','Piloto','Puntaje']))
        return pilotos, constructores, carreras
    else:
        print('\nYa se han finalizado todas las carreras!')        
        return pilotos, constructores, carreras




def gestion_2(lista_carrera):
    
    
    nombre = input('Cual es su nombre:\n')
    apellido = input('Cual es su apellido:\n')
    edad = input('Cual es su edad:\n')
    while not edad.isnumeric():
        edad = input('Cual es su edad:\n')
    ci = input('Cual es su cedula:\n')
    while not ci.isnumeric():
        ci = input('Cual es su cedula:\n')
    for i in lista_carrera:
        Carrera.mostrar_carrera(i)
    carrera_ronda = input('Ingrese la ronda de la carrera que quiere ver:\n')
    
    for i in lista_carrera:
        if  carrera_ronda == i.ronda:
            entrada = int(input('Que tipo de entrada desea 0. General= 150$ 1. VIP=340$ y tendras acceso al restaurante\n'))
            id_entrada = ci
            print(' a continuacion se le mostrara el mapa, las D son asientos disponibles y las O son asientos ocupados')

            if entrada == 0:

                asiento = mostrar_asientos (i.mapa['general'][0], i.mapa['general'][1])

            else:

                asiento = mostrar_asientos (i.mapa['vip'][0], i.mapa['vip'][1])




            
    if entrada==0:
        entrada='General'
        costo=150
        descuento=costo
        if ondulados (ci)==0:
            descuento=costo*0.5
            print(f'Tuvo un descuento del 50%, el precio de su entrada ahora es {descuento}')

    elif entrada==1:
        entrada='VIP'
        costo=340
        descuento=costo
        if ondulados(ci)==0:
            descuento=costo*0.5
            print(f'Tuvo un descuento del 50%, el precio de su entrada ahora es {descuento}')

    else:

        print('numero invalido')
        gestion_2(lista_carrera)

    confirmacion=int(input('Desea confirmar su compra:\n1. Si\n2. No\n'))
    
    if confirmacion==1:

        



        print(f'{nombre} {apellido}')
        print (f'{entrada} {id_entrada}')
        print(f'Asiento:{asiento}')
        iva=descuento*0.16
        total=descuento*1.16

        print(f'Subtotal: {costo}')
        print(f'Despues del descuento: {descuento}')
        print(f'iva= {iva}')
        print(f'Total: {total}')
        print(f'Gracias por su compra')
        usuario=Cliente(nombre, apellido, edad, ci, entrada, id_entrada, costo, False)
        

    elif confirmacion==2:
        funcion_menu()

    else:
        print('numero invalido')
        gestion_2(lista_carrera)




    return usuario



def mostrar_asientos(filas, columnas):
    asientos = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("D")
        asientos.append(fila)

    for i in range(filas):
        for j in range(columnas):
            print(asientos[i][j], end=" ")
        print()

    fila = int(input("Seleccione una fila: "))
    columna = int(input("Seleccione una columna: "))
    asiento=[fila, columna]
    if asientos[fila-1][columna-1] == "O":
        print("Este asiento ya está ocupado.")
    else:
        asientos[fila-1][columna-1] = "O"
        print("Asiento reservado exitosamente.")

    print("Gracias por usar nuestro sistema de reservas.")
    return asiento

def ondulados(ci):
    
        ondulado = True
        contador = 0
        par = list(str(ci))[0]
        inpar = list(str(ci))[1]

        if par == inpar:
            print (f'The number {ci} is not an ondulated number.')
        else:
            for x in str(ci):
                if (contador+2)%2 == 0:
                    if x != par:
                        ondulado = False
                    contador +=1
                elif (contador+2) %2 !=0:
                    if x != inpar:
                        ondulado = False
                    contador += 1
            if ondulado == True:
                return 0
            else:
                return 1




def gestion_3(cliente):
    ci=input('Ingrese su cedula: ')
    for usuario in cliente:
        if ci==usuario.id_entrada:
            if usuario.acceso==False:
                usuario.acceso=True
                print('El ticket es valido')
            else:
                print ('Ya alguien uso esta entrada')
        else: 
            print ('El ticket se ingreso incorrectamente')
            gestion_3(cliente)
    return

'''a cada cliente le convertimos su numero de cedula en numero de ticket y lo guardamos como atributo de ese cliente
para que cada ticket sea un numero unico. en esta funcion le solicitamos su cedula y verificamos que se haya vendido un ticket
con ese numero y luego verificamos que no haya sido usado'''





def gestion_4(lista_producto):
    menu=input('Marque el numero de la funcion que desee realizar\n 1. Buscar productos por nombre\n 2. Buscar productos por tipo \n 3. Buscar productos por rango de precio \n')
    resultado = 0
    if menu=='1':
        print('Buscar productos por nombre')
        nombre=input('Ingrese el nombre del producto: ')
        for x in lista_producto:
            if getattr(x,'nombre') == nombre:
                print('Se encontro el siguiente producto')
                nombre_producto = getattr(x,'nombre')
                precio = getattr(x,'precio')
                tipo = getattr(x,'tipo')
                print(f'Nombre: {nombre_producto} \n Precio: {precio}\n Tipo: {tipo}')
                resultado = 1
                break
        if resultado != 1:
            print('No se encontro ningun resultado')
            resultado = 0
    if menu=='2':
        print('Buscar productos por tipo: Las opciones son "alimento" o "bebida"')
        tipo=input('Ingrese el tipo del producto: ')
        for x in lista_producto:
            tipo_arr = getattr(x,'tipo') 
            tipo_primero = tipo_arr.split(":")[0]
            tipo_segundo = tipo_arr.split(":")[1]
            if tipo_primero == 'drink':
                t = 'bebida'
            else:
                t = 'alimento'
            if t == tipo:
                nombre_producto = getattr(x,'nombre')
                precio = getattr(x,'precio')
                print(f'Nombre: {nombre_producto} \n Precio: {precio}\n Subcategoria: {tipo_segundo}')
                resultado = 1
        if resultado != 1:
            print('No se encontro ningun resultado')
            resultado = 0
    if menu=='3':
        print('Buscar productos por rango de precio')
        rango_inferior=input('Ingrese rango inferior: ')
        if rango_inferior.isnumeric() == False:
            print('Rango inferior is not numeric. Try again')
            return
        rango_superior=input('Ingrese rango superior: ')
        if rango_superior.isnumeric()== False:
            print('Rango superior is not numeric. Try again')
            return
        for x in lista_producto:
            precio = float(getattr(x,'precio'))
            if (precio >= float(rango_inferior)) & (precio <= float(rango_superior)):
                nombre_producto = getattr(x,'nombre')
                tipo = getattr(x,'tipo')
                print(f'Nombre: {nombre_producto} \n Precio: {precio}')
                resultado = 1
        if resultado != 1:
            print('No se encontro ningun resultado')
            resultado = 0
    return

'''en esta funcion le mostraremos al usuarios los productos disponibles por nombre, por tipo o por rango de precio. 
agregamos todos los productos a una lista con una funcion definida en la clase estadio. le solicitamos al usuario 
lo que desea buscar y con un for buscamos en todos los objetos de la lista el atributo a buscar y mostramos todos
los productos que sean = a lo que solicito el cliente '''

def Numero_Perfecto(ci):
	suma = 0
	for i in range(1,int(ci)):
		if (int(ci) % (i) == 0):
			suma += (i)
	if int(ci) == suma:
		return True
	else:
		return False

def gestion_5(clientes):
    cedula_existe = False
    total = 0
    subtotal = 0
    es_descuento = False
    descuento = 0
    comida_sistema = False
    if not clientes:
        print("No hay clientes registrados \n\n")
        return
    cedula=input('Ingrese su cedula\n')
    for i in clientes:
        if i.ci==cedula:
            cedula_existe = True
            if i.entrada=='General':
                print ('No puede comprar porque su entrada es general')
            elif i.entrada=='VIP':
                print('Bienvenidos al restaurante')
                perfecto=Numero_Perfecto(i.ci)

                if perfecto == True:
                    print ('Obtendras un 15% de descuento')
                    es_descuento = True
                if int(i.edad)<18:
                    print ('Este cliente no puede consumir bebidas alcoholicas pq es menor de edad')
                print("Lista de productos")
                while True:
                    for x in lista_producto:
                            precio = float(getattr(x,'precio'))
                            nombre_producto = getattr(x,'nombreproducto')
                            adicional = getattr(x,'adicional')
                            tipo = getattr(x,'tipo')
                            cantidad = getattr(x,'cantidad')
                            if (int(i.edad)<18) & (adicional == "alcoholic"):
                                pass
                            else:
                                print(f'Nombre: {nombre_producto}, Precio: {precio}, Adicional: {adicional}')
                    comidaseleccionada=input('Que comida/bebida deseas comprar:\n')
                    cant=input('Cantidad:\n')
                    for x in lista_producto:
                            if getattr(x,'nombreproducto') == comidaseleccionada:
                                comida_sistema = True
                                precio = float(getattr(x,'precio'))
                                nombre_producto = getattr(x,'nombreproducto')
                                cantidad = getattr(x,'cantidad')
                                break
                    if comida_sistema == False: 
                        print("La comida escrita no se encuentra en el sistema")
                    continuar=input('Desea culminar la compra o continuar comprando? Seleccione 0 para Salir y 1 para continuar:\n')
                    subtotal = precio*int(cant) + subtotal
                    if int(continuar) == 0:
                        if es_descuento == True:
                            descuento = subtotal*0.15
                        total = subtotal - descuento
                        print("Subtotal:" + str(subtotal))
                        print("Descuento:" + str(descuento))
                        print("Total:" + str(total))
                        continuar=input('Estas de acuerdo con la compra. Presione 1 si estas de acuerdo, 0 si no:\n')
                        return
    if cedula_existe == False: 
        print ('La cedula no existe')
    return 

'''Para comprar productos de restaurantes verificamos que sea cliente vip y le mostramos todos los productos disponibles  con un for 
y el metodo getattr donde obtenemos el value del key solicitado de cada atributo, el usuario elige su producto. buscamos su precio en
el sistema si tiene algun descuento se lo decimos y descontamos y le mostramos la factura '''


def gestion_6():
    menu=int(input('Marque el numero de la funcion que desee realizar\n 1. \n 2. \n 3. \n 4. \n 5. \n 6. \n 7. \n'))
    if menu== 1:
        pass
    if menu == 2:
        pass 
    if menu == 3:
        pass
    if menu == 4:
        pass 
    if menu == 5:
        pass
    if menu == 6:
        pass 
    if menu == 7:
        pass

def grafica():
    print('Bebidas vs Comidas')
    # creating the dataset
    data = {'Bebidas':20, 'Comidas':15}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Bebidas")
    plt.ylabel("Comidas")
    plt.title("Cantidad de comidas/Bebidas que ofrece el restaurante")
    plt.show()


lista_constructor = Constructor.leer_constructor()
lista_piloto = Piloto.leer_piloto()
lista_circuito = Circuito.leer_circuito()
lista_carrera = Carrera.leer_carrera()
lista_location = Location.leer_location()
lista_producto = Producto.leer_producto()
for i in lista_constructor:
    pilotos = []
    for j in lista_piloto:
        if j.nombre_equipo == i.id_equipo:
                pilotos.append(i)
    i.pilotos = pilotos

def main():
    print('')
    print('/***************************/')
    print('/* Bienvenidos a Formula 1 */')
    print('/***************************/')
    print('')

    clientes=[]
    cliente = []
    entradas_general = []
    entradas_vip = []

    while True:
        menu=funcion_menu()

        if menu==1:
            gestion_1(lista_constructor, lista_piloto, lista_circuito, lista_carrera, lista_location)
            
        elif menu==2:
            usuario = gestion_2(lista_carrera)
            cliente.append(usuario)
            if usuario.entrada=='General':
                entradas_general.append(usuario)
            elif usuario.entrada=='VIP':
                entradas_vip.append(usuario)
        elif menu==3:
            gestion_3(cliente)
            
        elif menu==4:
            gestion_4(lista_producto)
            
        elif menu==5:
            gestion_5(clientes)

        elif menu==6:
            gestion_6()

        elif menu==7:
            grafica()

        elif menu==8:
            print(' _________________________')
            print('/\                        \\')
            print('\_|    Gracias y          |')
            print('  |      hasta luego      |')
            print('  |  _____________________|_')
            print('  \_/______________________/')
            break

main()